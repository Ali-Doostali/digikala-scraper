from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# chromedriver path
driver_path = "E:/projects/dgkala-scraper/chromedriver.exe"

# Browser settings
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the page
    driver.get("https://www.digikala.com/product/dkp-12924184/")
    print("صفحه باز شد!")
    
    # Wait for the page to load completely
    time.sleep(5)

    # Find the price tag
    price_tag = driver.find_element(By.CSS_SELECTOR, "span.text-h4")
    if price_tag:
        price = price_tag.text.strip()
        print(f"price: {price}")
        
        #  Save to CSV
        data = {"product": "Samsung S23 FE phone", "price": price}
        df = pd.DataFrame([data])
        df.to_csv("prices.csv", index=False, encoding="utf-8-sig")
        print("save to price.csv!")
    else:
        print("Price tag not found!")

finally:
    # Close the browser
    driver.quit()