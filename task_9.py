from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.random.org/coins/")

# Wait for the page to load
time.sleep(10)

# Find and select the number of coins to flip
select = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="num"]'))
select.select_by_value('1')

# Find and select the type of coin to flip
select = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="cur"]'))
options = select.options
coin_index = random.randint(1, len(options)-1)
select.select_by_index(coin_index)

# Click the "Flip Coin(s)" button
button = driver.find_element(By.CSS_SELECTOR, 'input[value="Flip Coin(s)"]')
button.click()

# Wait for the coin flip animation to finish
time.sleep(60)

# Close the browser
driver.quit()



#python task_9.py