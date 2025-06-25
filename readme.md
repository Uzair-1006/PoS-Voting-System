# 🗳️ PoS-Based Voting System using Blockchain (FastAPI + RSA)

This project demonstrates a **Proof of Stake (PoS)**-based secure voting mechanism where each voter's stake determines their voting weight. It uses **RSA public/private keys** for identity and signature verification to ensure that each vote is authenticated, unique, and tamper-proof.


## 🚀 Features

- 🔒 RSA key-based voter identity and signature verification
- 🧠 Stake-weighted voting
- 📜 Prevention of duplicate votes
- ⚡ FastAPI backend
- 💻 HTML + JS frontend
- 🧪 Cryptographic vote validation


## 🔐 Security Measures

- **Voter Public Key Registry**: Only pre-registered public keys can vote
- **Digital Signature**: Every vote is signed with voter's private key and verified using RSA
- **One Vote per Voter**: A flag prevents double voting
- **Vote Weighting**: Each vote carries a stake value (e.g., 50, 40, etc.)


## 🧰 Project Structure

pos-voting-system/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── routes/vote.py # Vote endpoint
│ ├── utils/crypto.py # Signature verification logic
│ ├── models/wallet.py # Wallet (key generation & signing)
│ └── data/voters.py # Predefined voter stakes & keys
├── frontend/
│ └── index.html # UI for submitting vote
├── requirements.txt # Dependencies
└── README.md


## ⚙️ How to Run the Project

### 🐍 1. Setup Python environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

▶️ 2. Run FastAPI server

cd app
uvicorn main:app --reload --port 8000

The API will be available at: http://localhost:8000

🌐 3. Open Frontend
Just open frontend/index.html in a browser. Make sure you're using the correct API URL in the fetch() call (e.g., http://localhost:8000/vote/).

📥 Example Dependencies (requirements.txt)

fastapi
uvicorn
pycryptodome
pydantic

🧪 Example Flow
A wallet is generated for a voter.

Voter signs the message:

message = public_key + candidate_name + "VOTE"
Frontend sends { senderPublicKey, voteFor, signature } to backend.

Backend verifies signature, checks registry, and accepts or rejects the vote.

📌 Future Improvements
Candidate registration & results endpoint

Frontend vote history

Database integration (SQLite/Postgres)

Blockchain integration for vote immutability

🛡️ Disclaimer
This is an educational prototype. Real-world voting systems require much more rigorous security, auditing, and legal oversight.

🧑‍💻 Developed by
Shaik Uzair Ahmed
Uzair-1006 : Github Id

