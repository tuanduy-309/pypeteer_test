import asyncio
import requests
from pyppeteer import connect

async def start_profile():
    token = 'eyJhbGciOiJIUzUxMiJ9.eyJicGRzLmJ1Y2tldCI6Im1seC1icGRzLXByb2QtZXUtMSIsImVtYWlsIjoiYW5oZW0zMDkyMDAyQGdtYWlsLmNvbSIsImlzQXV0b21hdGlvbiI6ZmFsc2UsIm1hY2hpbmVJRCI6IiIsInByb2R1Y3RJRCI6Im11bHRpbG9naW4iLCJzaGFyZElEIjoiY2JlMTM4MDAtYmJhZi00YzhmLTgwYjMtMTk3Zjg5NjM5NGYyIiwidXNlcklEIjoiNWI1ZDA5MWQtZDYxZi00MzkwLWJjODgtNzM0NzcyY2Q2Y2UwIiwidmVyaWZpZWQiOnRydWUsIndvcmtzcGFjZUlEIjoiMzlmZWI1YWEtYTkxZS00NDFhLTk4MDQtZmYyZTE0NzZmM2NkIiwid29ya3NwYWNlUm9sZSI6Im93bmVyIiwianRpIjoiZGE4MzY3YWUtZDk3YS00NDdkLThlZWEtNzk1ZjYyMGU1ZWU2Iiwic3ViIjoiTUxYIiwiaXNzIjoiNWI1ZDA5MWQtZDYxZi00MzkwLWJjODgtNzM0NzcyY2Q2Y2UwIiwiaWF0IjoxNzAxMzUzNzg1LCJleHAiOjE3MDEzNTczODV9.C_Lit7ruNeQt-bGKNKxpd4Dz5-COR4d1WzmfgNDEZHzYtIqrqUXZ3F7JDG51jPB4tsziGz4e97W8MWeCVTz0Tw'  # Replace with your JWT token
    profile_id = '941e8526-b877-40e8-8257-187e453f88cb'  # Replace with existing browser profile ID
    folder_id = '/home/profiles'  # Replace with existing browser profile folder ID

    url = f'https://launcher.mlx.yt:45001/api/v1/profile/f/{folder_id}/p/{profile_id}/start?automation_type=puppeteer'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    json_response = response.json()
    return json_response['status']['message']

async def demo():
    browser_port = await start_profile()
    print('Browser port:', browser_port)
    browser_url = f'http://127.0.0.1:{browser_port}'
    print('Browser URL:', browser_url)

    browser = await connect(browserWSEndpoint=browser_url, defaultViewport=None)
    page = await browser.newPage()
    await page.goto('https://multilogin.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(demo())