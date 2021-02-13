# from mysql import connector
import mysql.connector
from passwords import password_MySQL


### Initilize DataBase ###_______________________________________________

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password_MySQL,
        database="testdatabase"
    )
mycursor = db.cursor()

class DataBase:

    @staticmethod
    def savedatatosql(name, ticker, TargetPrice):
        mycursor.execute("INSERT INTO Companies (name, ticker, TargetPrice) VALUES (%s,%s,%s)", (name, ticker, TargetPrice))
        db.commit()

    @staticmethod
    def deleteCompany(ticker):

        mycursor.execute(f"DELETE FROM Companies WHERE ticker = '{ticker}'")
        db.commit()

    @staticmethod
    def showAllCOmpanies():

        mycursor.execute("SELECT name, ticker, TargetPrice FROM Companies")
        results = mycursor.fetchall()
        return results

    @staticmethod
    def pulltickerandprices():

        mycursor.execute("SELECT ticker, TargetPrice FROM Companies")
        myresults = mycursor.fetchall()
        return myresults

    @staticmethod
    def getListOfCompanies():
        mycursor.execute("SELECT name FROM Companies")
        myresults = mycursor.fetchall()
        new_list = []
        for company in myresults:
            company_1 = list(company)
            new_list.append(company_1)
        return new_list

### Secondary Functions ###_____________________________________________



### saved/not finished code ###_______________________________________________

def notes():
    mycursor.execute("CREATE TABLE Companies (name VARCHAR(50), ticker TINYTEXT, TargetPrice mediumint UNSIGNED, CompanyID int PRIMARY KEY AUTO_INCREMENT)")
    db.commit()