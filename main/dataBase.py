# from mysql import connector
import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="5359Root!@12",
        database="testdatabase"
    )

# mycursor.execute("CREATE TABLE Companies (name VARCHAR(50), ticker TINYTEXT, TargetPrice mediumint UNSIGNED, CompanyID int PRIMARY KEY AUTO_INCREMENT)")
        # db.commit()

# mycursor.execute("DELETE FROM companies WHERE name = 'tesla'")
        # db.commit()



class DataBase():

    def savedatatosql(self, name, ticker, TargetPrice):

        mycursor = db.cursor()
        mycursor.execute("INSERT INTO Companies (name, ticker, TargetPrice) VALUES (%s,%s,%s)", (name, ticker, TargetPrice))
        db.commit()

    def showAllCOmpanies():

        mycursor = db.cursor()
        mycursor.execute("SELECT name, ticker, TargetPrice FROM Companies")
        results = mycursor.fetchall()
        return results

    def pulltickerandprices():
        mycursor = db.cursor()
        mycursor.execute("SELECT ticker, TargetPrice FROM Companies")

        myresults = mycursor.fetchall()
        return myresults

    def deleteCompany(self, ticker):
        pass
