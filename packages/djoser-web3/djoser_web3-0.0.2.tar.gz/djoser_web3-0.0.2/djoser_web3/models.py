from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator,MinValueValidator
from slugify import slugify
from django.db.models.signals import post_save
import requests
from django.conf import settings
activecampaign_url = settings.ACTIVE_CAMPAIGN_URL
activecampaign_key = settings.ACTIVE_CAMPAIGN_KEY
from djoser.signals import  user_registered
import uuid,json
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
import requests

# from apps.product.models import ProductsLibrary, WishlistProductsLibrary

def user_profile_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'users/{0}/profile.jpg'.format(str(uuid.uuid4()))

def user_banner_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    banner_pic_name = 'users/{0}/banner.jpg'.format(str(uuid.uuid4()))


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        item={}
        item['id']=str(user.id)
        item['email']=user.email
        item['username']=user.username

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.role="Admin"
        user.verified=True
        user.become_seller=True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    roles = (
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('helper', 'Helper'),
        ('editor', 'Editor'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    stripe_customer_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_account_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_payment_id = models.CharField(max_length=100, blank=True, null=True)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    agreed = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    become_seller = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=roles, default='customer')
    verified = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'agreed']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        counter = 1
        while UserAccount.objects.filter(slug=self.slug).exists():
            self.slug = f"{self.slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='profile')

    picture = models.ImageField(default='users/user_default_profile.png',  upload_to='media/users/pictures/', blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(default='users/user_default_bg.jpg', upload_to='media/users/banners/' , blank=True, null=True, verbose_name='Banner')

    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)

    facebook = models.CharField(max_length=80, null=True, blank=True)
    twitter = models.CharField(max_length=80, null=True, blank=True)
    instagram = models.CharField(max_length=80, null=True, blank=True)
    linkedin = models.CharField(max_length=80, null=True, blank=True)
    youtube = models.CharField(max_length=80, null=True, blank=True)
    github = models.CharField(max_length=80, null=True, blank=True)


class Wallet(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='wallet')

    # Ethereum Wallet
    address = models.CharField(max_length=255, unique=True)
    private_key = models.CharField(max_length=255, unique=True)
    private_key_hash = models.CharField(max_length=255, unique=True)

    savings = models.DecimalField(max_digits=1000, decimal_places=2, default=0, blank=False)
    product_sales = models.DecimalField(max_digits=1000, decimal_places=2, default=0, blank=False)
    course_sales = models.DecimalField(max_digits=1000, decimal_places=2, default=0, blank=False)
    total_earnings = models.DecimalField(max_digits=1000, decimal_places=2, default=0, blank=False)
    total_spent = models.DecimalField(max_digits=1000, decimal_places=2, default=0, blank=False)
    total_transfered = models.DecimalField(max_digits=1000, decimal_places=2, default=0, blank=False)
    total_received = models.DecimalField(max_digits=1000, decimal_places=2, default=0, blank=False)

    save_card = models.BooleanField(default=False)


class Transaction(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    tx_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.tx_hash


class Transactions(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    transactions = models.ManyToManyField(Transaction, blank=True)
    def __str__(self):
        return self.user.email


def post_user_registered(request, user ,*args, **kwargs):
    #1. Definir usuario que ser registra
    user = user
    #2. Crear cliente en stripe
    stripe_customer = stripe.Customer.create(
        email=user.email,
        name=user.first_name+" "+user.last_name
    )
    #3 Agegar Stripe Customer ID a Modelo de Usuario
    user.stripe_customer_id = stripe_customer["id"]
    user.save()

    #4 Crear Stripe Connect Account ID
    connect_account = stripe.Account.create(
        type = "express",
        capabilities={"card_payments": {"requested": True}, "transfers": {"requested": True}},
    )
    user.stripe_account_id = connect_account["id"]
    user.save()

    Profile.objects.create(user=user)


    from eth_account import Account
    import secrets
    import hashlib

    # 1. Define the user to be registered
    user = user

    # 2. Create a wallet and transactions object
    wallet = Wallet.objects.create(user=user)
    transactions = Transactions.objects.create(user=user)

    # 3. Generate a private key and create an Ethereum account
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)

    # 4. Hash the private key
    private_key_hash = hashlib.sha256(private_key.encode()).hexdigest()

    # 5. Save the wallet information to the database
    wallet.private_key_hash = private_key_hash
    wallet.address = acct.address
    wallet.save()

user_registered.connect(post_user_registered)


