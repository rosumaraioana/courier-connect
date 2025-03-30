import httpx
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")
PHPSESSID = os.getenv("PHPSESSID")
TOKEN = os.getenv("TOKEN")

def fetch_data(url, session_id, token):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    }
    cookies = {
        "CTOKENA": TOKEN,
        "PHPSESSID": PHPSESSID,
    }
    data = {
        "source": [{"country": "RO", "lat": 46, "lng": 25}],
        "destination": [{"country": "DE", "lat": 51.5, "lng": 10.5}],
        "extendedRange": 0,
        "loadingDate": "30-03-2025",
        "loadingInterval": 9,
        "requiredTruck": [],
        "spotlightOnly": False,
        "_errorNames": {},
    }

    with httpx.Client() as client:
        response = client.post(url, headers=headers, cookies=cookies, json=data)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    data = fetch_data(API_URL, session_id=PHPSESSID, token=TOKEN)
    print(data)
