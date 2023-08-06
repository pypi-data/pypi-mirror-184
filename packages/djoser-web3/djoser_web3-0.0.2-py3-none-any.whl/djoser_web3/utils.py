from .models import Wallet

def get_private_key(private_key_hash):
    # Query the database for the wallet with the matching private key hash
    wallet = Wallet.objects.get(private_key_hash=private_key_hash)
    
    # Return the private key
    return wallet.private_key