from tkinter import *
from dataBase import DataBase

def openGui():
    root = Tk()

    name_var = StringVar()
    ticker_var = StringVar()
    price_var = StringVar()

    def submit():
        name = name_entry.get()
        ticker = ticker_entry.get()
        TargetPrice = price_var.get()

        DataBase.savedatatosql(name, ticker, TargetPrice)

        #resets the entry fields
        name_var.set("")
        ticker_var.set("")
        price_var.set("")

    #************************ GUI compentents********************

    #creating a label for company and iserting it on page
    name_label = Label(root, text="company")
    name_label.grid(row=0, column=0)

    #company name entry and insert
    name_entry = Entry(root, textvariable = name_var)
    name_entry.grid(row=0, column=1)

    #creating a label for ticker and iserting it on page
    ticker_label = Label(root, text="Ticker Symbol")
    ticker_label.grid(row=1, column=0)

    #company name entry and insert
    ticker_entry = Entry(root, textvariable = ticker_var)
    ticker_entry.grid(row=1, column=1)

    #stock price of company label
    price_label = Label(root, text="target price")
    price_label.grid(row=2, column=0)

    #stock price of company entry
    price_entry = Entry(root, textvariable=price_var)
    price_entry.grid(row=2, column=1)

    #submit button
    submit_button = Button(root, text="submit", command=submit)
    submit_button.grid(row=3, column=1)

    root.mainloop()