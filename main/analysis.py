from main.dataBase import DataBase
from main.webScrapper import WebScrapper
from main.textApplication import *



class Analysis():

    @staticmethod
    def compareCurrentCompaniesToTarget():
        list = DataBase.pulltickerandprices()

        ticker_list, target_list = zip(*list)
        dict = {}

        for index, ticker in enumerate(ticker_list):

            current_price = WebScrapper.getCurrentPrice(ticker)
            price = current_price.replace(",", "")
            price = float(price)

            if price > target_list[index]:
                dict[ticker_list[index]] = (f"The price is over the target by ${round((price - target_list[index]), 2)}")
            else:
                dict[ticker_list[index]] = (f"The price is under the target by ${round((target_list[index] - price), 2)}")

        return dict

            # if float(price) <= float(Target_list[index]):
            #     sendTextMessage(f"the price of {t} currently is ${price}")
            # else:
            #     sendTextMessage("no major change")