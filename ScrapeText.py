from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver(url):
    """Get driver"""
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage") #Linux interference
    options.add_argument("no-sandbox") #sandboxing disabled
    options.add_argument("disable-blink-features=AutomationControlled")

    options.add_experimental_option("excludeSwitches", ["enable-automation"]) #avoid detection from webpages

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


def main():
    driver = get_driver("https://automated.pythonanywhere.com")
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/h1[1]")
    return element.text


print(main())





