from fastapi import APIRouter
from utils.fetcher import fetch_coins

router = APIRouter()

# Define plan limits
PLAN_LIMITS = {
    "basic": 10,
    "pro": 100,
    "ultra": 1000,
    "mega": 10000
}

@router.get("/{plan}")
def get_coins(plan: str):
    """
    Fetch top coins based on subscription plan:
    - basic = 10
    - pro = 100
    - ultra = 1000
    - mega = 10000
    """
    plan = plan.lower()
    if plan not in PLAN_LIMITS:
        return {"error": "Invalid plan. Use: basic, pro, ultra, mega."}

    limit = PLAN_LIMITS[plan]
    data = fetch_coins(limit)

    return {
        "plan": plan,
        "limit": limit,
        "coins": data
    }
