# LinkedIn Jobs Scraper using Selenium (handles JavaScript-heavy sites)
# Perfect when BeautifulSoup alone doesn't work

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
driver.get("https://www.linkedin.com/jobs/search/?keywords=python&location=Worldwide")

time.sleep(5)
job_cards = driver.find_elements(By.CLASS_NAME, "base-card")

for card in job_cards[:10]:
    try:
        title = card.find_element(By.TAG_NAME, "h3").text
        company = card.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
        location = card.find_element(By.CLASS_NAME, "job-search-card__location").text
        print(f"{title} | {company} | {location}")
    except:
        continue

driver.quit()
