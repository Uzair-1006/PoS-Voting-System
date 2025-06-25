
from blockchain.transaction.Wallet import Wallet

# Create 5 voters
voter1 = Wallet()
voter2 = Wallet()
voter3 = Wallet()
voter4 = Wallet()
voter5 = Wallet()

# Save their public keys
print("Voter 1:", voter1.public_key_string())
print("Voter 2:", voter2.public_key_string())
print("Voter 3:", voter3.public_key_string())
print("Voter 4:", voter4.public_key_string())
print("Voter 5:", voter5.public_key_string())
# Voter signs their vote
data_to_sign = voter1.public_key_string() + "Alice" + "VOTE"
signature = voter1.sign(data_to_sign)
print("Signature:", signature)
