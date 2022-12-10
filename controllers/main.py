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


def login():
    driver.get("https://chat.openai.com/chat")
    async_find('//*[@id="__next"]/div/div/div[4]/button[1]').click()
    async_find('//*[@id="username"]').send_keys("victor.barcelos.tech@gmail.com")
    async_find("/html/body/main/section/div/div/div/form/div[2]/button").click()
    async_find('//*[@id="password"]').send_keys("B4rc3l0s?*")
    async_find("/html/body/main/section/div/div/div/form/div[2]/button").click()
    async_find('//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button').click()
    async_find(
        '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]'
    ).click()
    async_find(
        '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]'
    ).click()
