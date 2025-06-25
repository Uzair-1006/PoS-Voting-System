from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api_v1.routes import router
# from api.utils.log_middleware import LogMiddleware

app = FastAPI(
    title="PoS Voting API",
    docs_url="/api/docs"
)

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # During dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(LogMiddleware)

# Inject a dummy node object for now
class DummyNode:
    def __init__(self):
        self.transaction_pool = []

app.state.node = DummyNode()

app.include_router(router, prefix="/api")
