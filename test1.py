# import requests
# api_key = "fbd40ed206978699b24da2592c06ec88"  # Thay thế bằng API Key của bạn
# profile_id = "jc45nr0"    # Thay thế bằng ID của Profile muốn sử dụng

# # The sample passed the test in selenium version 3.141.0

import requests,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ads_id = "jc45nr0"
# http://local.adspower.net:50325 Script can go to Profile Management-> click Settings-> click Cache folder-> local_api file to obtain API address
open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

resp = requests.get(open_url).json()
if resp["code"] != 0:
    print(resp["msg"])
    print("please check ads_id")
    sys.exit()

chrome_driver = resp["data"]["webdriver"]
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.sephora.com/beauty/giftcards?fbclid=IwAR0Hsmt_4rRsaTpvUFgCTtRrQqAsJ--XRYbRl-tz9JZ9Z2mwgItywdmkm1U")

# print(driver.title)
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
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/button"))).click()

for i in range(32):
    print(i)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/main/div/div/div[11]/div/div[2]/div/div[2]/div/div/div/form/div[1]/div/div/input"))).send_keys(data[i][0])
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div/div[11]/div/div[2]/div/div[2]/div/div/div/form/div[2]/div/div/input").send_keys(data[i][1])
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/main/div/div/div[11]/div/div[2]/div/div[2]/div/div/div/form/button"))).click()
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[4]//button"))).click()
    except:
        pass
    cash = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/main/div/div/div[11]/div/div[2]/div/div[2]/div/div/div/p[2]")))
    print(cash.text)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div/div[11]/div/div[2]/div/div[2]/div/div/div/form/div[2]/div/div/input").clear()
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/main/div/div/div[11]/div/div[2]/div/div[2]/div/div/div/form/div[1]/div/div/input").clear()
    time.sleep(1)
driver.quit()
requests.get(close_url)