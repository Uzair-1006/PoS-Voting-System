from pydantic import BaseModel

class VoteTransaction(BaseModel):
    senderPublicKey: str
    voteFor: str
    type: str = "VOTE"
    signature: str

class VotePayload(BaseModel):
    transaction: VoteTransaction
