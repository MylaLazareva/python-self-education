from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открыть браузер Chrome и перейти на сайт Rozetka
    driver = webdriver.Chrome()
    driver.get("https://rozetka.com.ua/")

    # Подождать, пока страница загрузится
    time.sleep(20)

    # Найти и нажать на кнопку регистрации
    button = driver.find_element(By.XPATH, ("/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button"))
    button.click()

    # Подождать, пока форма загрузится
    time.sleep(20)

    # Найти и нажать на кнопку "Войти"
    submit_button = driver.find_element(By.XPATH, ("/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[2]"))
    submit_button.click()

    # Подождать, пока форма загрузится
    time.sleep(20)

    # Найти и заполнить поле имени
    name_field = driver.find_element(By.CSS_SELECTOR, "#registerUserName")
    name_field.send_keys("Мила")
    time.sleep(2)

    # Найти и заполнить поле фамилии
    last_name_field = driver.find_element(By.CSS_SELECTOR, "#registerUserSurname")
    last_name_field.send_keys("Мина")
    time.sleep(2)

    # Найти и заполнить поле телефона
    phone_field = driver.find_element(By.CSS_SELECTOR, "#registerUserPhone")
    phone_field.send_keys("0661234567")
    time.sleep(2)

    # Найти и заполнить поле электронной почты
    email_field = driver.find_element(By.CSS_SELECTOR, "#registerUserEmail")
    email_field.send_keys("Wl123@gmail.com")
    time.sleep(2)

    # Найти и заполнить поле пароля
    password_field = driver.find_element(By.CSS_SELECTOR, "#registerUserPassword")
    password_field.send_keys("QwezxC123098")
    time.sleep(5)

    # Найти и нажать на кнопку "Зарегистрироваться"
    register_submit_button = driver.find_element(By.XPATH, ("/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-register/div/form/fieldset/div[8]/button[1]"))
    register_submit_button.click()

    # Подождать, пока страница загрузится
    time.sleep(40)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Закрыть браузер
    driver.quit()




#   python task_10.py