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

# Product List
products = [
    {"name": "Samsung Galaxy S23 FE", "url": "https://www.digikala.com/product/dkp-12924184/"},
    {"name": "Samsung Galaxy A54", "url": "https://www.digikala.com/product/dkp-11346304/"},
    {"name": "Samsung Galaxy S24 Ultra", "url": "https://www.digikala.com/product/dkp-13714776/"},
    {"name": "Samsung Galaxy A55", "url": "https://www.digikala.com/product/dkp-14851833/"}
]

# List to store data
data = []

try:
    for product in products:
        print(f"Scrapping: {product['name']}")
        
        # Open the product page
        driver.get(product["url"])
        time.sleep(5)  # Wait for the page to load

        # Find the price tag
        try:
            price_tag = driver.find_element(By.CSS_SELECTOR, "span.text-h4")
            price = price_tag.text.strip()
            print(f"price {product['name']}: {price}")
        except:
            price = "Price not found"
            print(f"price for {product['name']} Not found!")

        # Add to data list
        data.append({"product": product["name"], "price": price})

finally:
    # Add to data list
    driver.quit()

# Save data in CSV
df = pd.DataFrame(data)
df.to_csv("prices.csv", index=False, encoding="utf-8-sig")
print("Data saved in prices.csv!")