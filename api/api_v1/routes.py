from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.crypto import verify_signature  # Make sure this path is correct
from data.voters import voters  # Contains registered voters and their stakes

router = APIRouter()

class VoteInput(BaseModel):
    transaction: dict

@router.post("/vote/")
async def vote_endpoint(payload: VoteInput, request: Request):
    tx = payload.transaction
    sender = tx.get("senderPublicKey")
    candidate = tx.get("voteFor")
    sig = tx.get("signature")
    tx_type = tx.get("type", "VOTE")

    if not sender or not candidate or not sig:
        return JSONResponse(status_code=422, content={"error": "Missing required transaction fields ❌"})

    message = sender + candidate + tx_type

    # ✅ 1. Check if sender is a registered voter
    if sender not in voters:
        return JSONResponse(status_code=403, content={"error": "Voter not registered ❌"})

    # ✅ 2. Check if voter has already voted
    if voters[sender]["has_voted"]:
        return JSONResponse(status_code=403, content={"error": "You have already voted ❌"})

    # ✅ 3. Verify the digital signature
    if not verify_signature(sender, message, sig):
        return JSONResponse(status_code=400, content={"error": "Invalid signature ❌"})

    # ✅ 4. Mark voter as voted and return stake info
    voters[sender]["has_voted"] = True
    stake = voters[sender]["stake"]

    return {
        "message": "✅ Vote accepted",
        "stake": stake,
        "voted_for": candidate
    }
