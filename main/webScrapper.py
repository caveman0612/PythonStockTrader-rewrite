from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random

def random_number_gen():
    random_9 = float(random.randrange(4, 9) / 10)
    random_1 = float(random.randrange(0, 1))
    return random_1 + random_9

class WebScrapper():

    def getCurrentPrice(self, ticker):
        self.ticker = ticker
        headless = True

        if headless == True:
            options = Options()
            options.headless = True
            path = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(path, options=options)
        else:
            path = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(path)

        website = "https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker + "&.tsrc=fin-srch"
        driver.get(website)

        full_xpath = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]"
        current_price = driver.find_element_by_xpath(full_xpath)

        return current_price.text
        driver.quit()

    def getTopNewsHeadlines():
        headless = True
        ticker = "TSLA" + " news"

        if headless == True:
            options = Options()
            options.headless = True
            path = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(path, options=options)
        else:
            path = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(path)

        website = "https://google.com"
        driver.get(website)

        # search = driver.find_element_by_class_name("gLFyf gsfi")

        full_xpath = "/html/body/div[2]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input"
        search = driver.find_element_by_xpath(full_xpath)

        for letter in ticker:
            search.send_keys(letter)
            time.sleep(random_number_gen())

        search.send_keys(Keys.ENTER)
        time.sleep(1)

        xpath = '//*[@id="rso"]/div[2]/div[1]/div[2]/div[2]/div/span/span'
        articles = driver.find_elements_by_xpath(xpath)
        print(type(articles))
        print(articles)



        driver.quit()