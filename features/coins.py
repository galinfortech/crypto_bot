from fastapi import APIRouter
from utils.fetcher import fetch_top_coins

router = APIRouter()

# Plan-to-limit mapping
PLAN_LIMITS = {
    "basic": 5,
    "pro": 25,
    "ultra": 50,
    "mega": 100
}

@router.get("/coins/{plan}")
async def get_coins(plan: str):
    if plan not in PLAN_LIMITS:
        return {"error": "Invalid plan. Choose basic, pro, ultra, or mega."}

    limit = PLAN_LIMITS[plan]
    coins = await fetch_top_coins(limit)
    return {
        "plan": plan,
        "limit": limit,
        "coins": coins
    }
