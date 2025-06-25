class Transaction:
    def __init__(self, senderPublicKey, voteFor, type, signature):
        self.senderPublicKey = senderPublicKey
        self.voteFor = voteFor
        self.type = type  # Should be "VOTE"
        self.signature = signature

    def to_dict(self):
        return {
            "senderPublicKey": self.senderPublicKey,
            "voteFor": self.voteFor,
            "type": self.type,
            "signature": self.signature
        }
