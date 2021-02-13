from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random

# Main swithces_______________________________________________

HEADLESS = True

# Main functions _______________________________________________

class WebScrapper():

    @staticmethod
    def getCurrentPrice(ticker):
        driver = CheckHeadless()

        website = "https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker + "&.tsrc=fin-srch"
        driver.get(website)

        full_xpath = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]"
        current_price = driver.find_element_by_xpath(full_xpath)

        return current_price.text
        driver.quit()

    @staticmethod
    def checkDailyLosers():
        driver = CheckHeadless()

        website = "https://finance.yahoo.com/screener/predefined/day_losers"
        driver.get(website)

        link = driver.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[1]/td[1]/a')
        new_link = link.get_attribute('href')

        website = new_link
        driver.get(website)

        full_xpath = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span[1]"
        current_price = driver.find_element_by_xpath(full_xpath)

        return current_price.text

    @staticmethod #not finished
    def getTopNewsHeadlines(ticker): #not finished
        driver = CheckHeadless()

        website = "https://google.com"
        driver.get(website)

        full_xpath = "/html/body/div[2]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input"
        search = driver.find_element_by_xpath(full_xpath)

        google_search = ticker + " news"
        for letter in google_search:
            search.send_keys(letter)
            time.sleep(random_number_gen())

        search.send_keys(Keys.ENTER)
        time.sleep(1)

        driver.quit()

### secondary functions ################################################

def CheckHeadless():
    # if boolen == None:
    if HEADLESS == True:
        options = Options()
        options.headless = True
        path = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(path, options=options)
        return driver
    else:
        path = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(path)
        return driver

def random_number_gen():
    random_9 = float(random.randrange(1, 5) / 10)
    random_1 = float(random.randrange(0, 1))
    return random_1 + random_9




