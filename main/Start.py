# from display import openGui

from main.dataBase import DataBase
# from textApplication import sendTextMessage
from main.analysis import Analysis
from main.webScrapper import WebScrapper



ticker = 'TSLA'

print(Analysis.compareCurrentCompaniesToTarget())

# Webscrapper ___________________________________________________

# TSLA = WebScrapper.getCurrentPrice(ticker)
# print(TSLA)

# daily = WebScrapper.checkDailyLosers()
# print(daily)

# Database checker ______________________________________________

# companies_all = DataBase.showAllCOmpanies()
# print(companies_all)

# DataBase.deleteCompany("SRNE")

# DataBase.savedatatosql("Telsa", "TSLA", 820)
