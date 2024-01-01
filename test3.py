import asyncio
import selenium_dolphin as dolphin
from selenium_dolphin import DolphinAPI
from pyppeteer import connect
import time
from bs4 import BeautifulSoup
import requests
import pyautogui as pag


response = dolphin.run_profile(232437541)
port = response['automation']['port']
ws_endpoint = response['automation']['wsEndpoint']

async def main():
    browser = await connect(browserWSEndpoint=f'ws://127.0.0.1:{port}{ws_endpoint}')

    pages = await browser.pages()
    page = pages[0]

    # await page.goto("https://www.sephora.com/beauty/giftcards?fbclid=IwAR0Hsmt_4rRsaTpvUFgCTtRrQqAsJ--XRYbRl-tz9JZ9Z2mwgItywdmkm1U")
    await asyncio.sleep(3)
    while True:    
        try:
            await page.click('#modal0Dialog > button > svg')
        except:
            break
    await asyncio.sleep(1)
    data = [
    ("6215889101468712", "62176209"),
    ("6300173914574145", "79632819"),
    ("6300174436919227", "02281505"),
    ("6300174287384994", "06305834"),
    ("6215889322305007", "96745729"),
    ("6300174388049580", "80239163"),
    ("6300174188650043", "49245499"),
    ("6300174250367451", "59327866"),
    ("6215889952547591", "83005594"),
    ("6215889999256596", "03327243"),
    ("6300174212167328", "91791802"),
    ("6215889244573252", "83794651"),
    ("6300173926945146", "41338944"),
    ("6300174424886722", "25190107"),
    ("6300174428356588", "15341337"),
    ("6215889465747611", "49065779"),
    ("6300173905502279", "00044362"),
    ("6215889591585756", "75490651"),
    ("6300173965774411", "15584971"),
    ("6300174234914938", "06079099"),
    ("6300174202286366", "67066739"),
    ("6215889690459659", "02510451"),
    ("6215889255860173", "13244763"),
    ("6300174229447905", "64704555"),
    ("6215889317566202", "26049034"),
    ("6300174443297652", "32148667"),
    ("6300174383408885", "38937435"),
    ("6300173952405079", "29184658"),
    ("6300174445305438", "41252907"),
    ("6300174430028686", "89080939"),
    ("6215889144626083", "45530155"),
    ("6215890012795584", "41254169")
]
    for i in range(32):
        x = data[i][0]
        y = data[i][1]
        await asyncio.sleep(1)
        
        await page.type('#gcCardNumber', x)
        await page.type('#gcPinNumber', y)
        await asyncio.sleep(1)

        await page.click('body > div:nth-child(3) > div > div > main > div > div > div:nth-child(10) > div > div.css-0 > div > div:nth-child(2) > div > div > div > form > button')
        await asyncio.sleep(2)
        await page.waitForSelector('#solver-button', {'visible': True})

        await page.click('#solver-button')        
        # while True:
        #     try:
        #         pag.click(pag.locateCenterOnScreen('captcha.png', grayscale=True, confidence=.8))
        #         pag.sleep(0.5)
        #         pag.moveTo(x= 200, y= 200)
        #         time.sleep(2)
        #     except:
        #         break

        await asyncio.sleep(2)
        
        data1 = await page.evaluate('document.querySelector("#gcCardNumber").value')
        await asyncio.sleep(2)

        try:
            data2 = await page.evaluate('''() => {const element = document.querySelector('[data-at="balance_msg"]');return element ? element.innerText : null;}''')
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
        # await asyncio.sleep(90)
        
    input("Enter")

    await browser.close()

    dolphin.close_profile(232437541)

asyncio.run(main())