import requests

BASE_URL = "https://api.coingecko.com/api/v3"

def fetch_coins(limit: int):
    """
    Fetch top coins from CoinGecko by market cap.
    :param limit: how many coins to return (10, 100, 1000, 10000)
    :return: cleaned list of coins with useful fields
    """
    url = f"{BASE_URL}/coins/markets"
    params = {
        "vs_currency": "usd",               # get prices in USD
        "order": "market_cap_desc",         # sort by market cap
        "per_page": limit,                  # number of coins to return
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        coins = response.json()
        # Clean output so it’s easier to read
        cleaned = [
            {
                "rank": i + 1,
                "symbol": coin["symbol"].upper(),
                "name": coin["name"],
                "price_usd": coin["current_price"],
                "market_cap_usd": coin["market_cap"],
                "change_24h_pct": coin["price_change_percentage_24h"]
            }
            for i, coin in enumerate(coins)
        ]
        return cleaned
    else:
        return {"error": f"Failed to fetch data from CoinGecko (status {response.status_code})"}
