# 🗳️ Proof-of-Stake Voting System

A decentralized voting system built using Python and FastAPI where voters participate by signing their votes with RSA-based public-private key pairs. The influence of a vote is determined by the **stake** each voter holds.

---

## 📦 Features

- ✅ **Stake-based Voting Power**: Each voter has a predefined stake that determines their vote weight.
- 🔐 **Cryptographic Signature Verification**: Every vote is digitally signed with the voter's private key and verified using their public key.
- 🗂️ **Voter Registry**: Only registered voters with public keys are allowed to vote.
- 🚫 **Double Voting Prevention**: Once a voter casts their vote, they are marked as `has_voted: True`.
- 🌐 **CORS-enabled API**: Built with FastAPI and can communicate with frontend clients via REST.

---

## 🔧 Project Structure

pos-voting/
├── app/
│ ├── main.py # FastAPI app initialization
│ ├── routes/
│ │ └── vote.py # Vote endpoint logic
│ ├── data/
│ │ └── voters.py # Voter registry with stakes
│ ├── utils/
│ │ └── crypto.py # Signature verification logic
│ └── wallet/
│ └── wallet.py # Wallet class to generate keys and signatures
├── sample_txn.py # Script to generate sample voters and votes
├── static/
│ └── index.html # Frontend vote submission form
└── README.md # This file


---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Install dependencies:

```bash
pip install fastapi uvicorn pycryptodome


🧠 Security Measures Implemented
| Area                      | Measure                                                              |
| ------------------------- | -------------------------------------------------------------------- |
| 🔏 Authentication         | Votes must be signed with voter's private key                        |
| 🧾 Signature Verification | Backend uses `SHA256 + RSA` to verify that sender signed the message |
| 🔒 Voter Whitelisting     | Only registered voters with known public keys can cast a vote        |
| ⛔ Double Voting Block     | Voters can only vote once (`has_voted = True` after voting)          |
| 📊 Weighted Votes         | Each voter's vote is weighted by their "stake" value                 |

{
  "transaction": {
    "senderPublicKey": "-----BEGIN PUBLIC KEY-----\\nMIGfMA0G...QAB\\n-----END PUBLIC KEY-----",
    "voteFor": "Alice",
    "type": "VOTE",
    "signature": "4ba87e98...fede70"
  }
}

🌍 API Endpoint
| Method | URL      | Description                    |
| ------ | -------- | ------------------------------ |
| POST   | `/vote/` | Submits a vote for a candidate |

📈 Future Enhancements
 Add a /results/ endpoint to tally votes by stake.

 Include vote deadlines.

 Add persistent storage (DB or blockchain-like ledger).

 Show real-time voting stats on frontend.

 Anonymous voting option using zero-knowledge proof (ZKP).

Developed by Uzair-1006