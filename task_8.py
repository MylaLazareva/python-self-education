from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver
s = Service(r'C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Load the page
driver.get('https://www.random.org/dice/')

# Wait for the roll dice button to become clickable
wait = WebDriverWait(driver, 120)
roll_dice_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Roll Dice"]')))

# Click the roll dice button
roll_dice_button.click()

# Sleep for 1 minute to keep the result on the screen

time.sleep(60)

# Close the browser
driver.quit()





#python task_8.py