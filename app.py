from fastapi import FastAPI
from features.coins import router as coins_router

app = FastAPI(
    title="Crypto Market Data Bot",
    description="Bot that provides crypto market data by subscription plan",
    version="1.0.0"
)

# Register routes
app.include_router(coins_router, prefix="/coins", tags=["Coins"])

@app.get("/")
def root():
    return {"message": "Welcome to the Crypto Bot API 🚀"}
