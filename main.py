from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\chromedriver_win32\chromedriver.exe"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

headers = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

URL ="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

response = requests.get(URL, headers=headers)

print(response)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_prices = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX")

price_list = [price.get_text().split("+")[0] for price in all_prices]

print(f"price list: {price_list}")

all_address = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link")

address_list = [address.get_text() for address in all_address]

print(f"address list: {address_list}")

all_link_elements = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link", href=True) # 👉️ Find <a> tag that have a href attr

all_links = []

for link in all_link_elements:
    href = link['href']
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

print(f"all links: {all_links}")
#print(a_tag['href']) # 👉️ Print href

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdpFvi2fygiNgk1XGKtDE4V4wwlcBFy_GFXU5Xe8BP4XCQJUQ/viewform")
    time.sleep(1)

    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[n])
    time.sleep(2)

    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[n])
    time.sleep(2)

    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(all_links[n])
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    time.sleep(4)

driver.quit()