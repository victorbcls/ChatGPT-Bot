from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.support.expected_conditions import _find_element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from unidecode import unidecode

import read

driver = webdriver.Chrome()
driver.set_window_position(2000, 0)  # Pra abrir no segundo monitor
EMAIL = "chatgpt login"
PASSWORD = "chatgpt password"


def async_find(value, element_type=By.XPATH):
    return WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((element_type, value))
    )


def login():
    driver.get("https://chat.openai.com/chat")
    async_find('//*[@id="__next"]/div/div/div[4]/button[1]').click()
    async_find('//*[@id="username"]').send_keys(EMAIL)
    async_find("/html/body/main/section/div/div/div/form/div[2]/button").click()
    async_find('//*[@id="password"]').send_keys(PASSWORD)
    async_find("/html/body/main/section/div/div/div/form/div[2]/button").click()
    async_find('//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button').click()
    async_find(
        '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]'
    ).click()
    async_find(
        '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]'
    ).click()


def ask(question):
    async_find(
        '//*[@id="__next"]/div/div[1]/main/div[2]/form/div/div[2]/textarea'
    ).send_keys(question, Keys.ENTER)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="__next"]/div/div[1]/main/div[2]/form/div/div[1]/button',
            )
        )
    )
    resposta = async_find(
        '//*[@id="__next"]/div/div[1]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]'
    ).text
    filename = read.readAndSave(resposta)
    driver.refresh()
    return filename
