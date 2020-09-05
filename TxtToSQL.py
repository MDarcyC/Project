import time, pandas, numpy, os, glob, sqlalchemy
import mysql
import mysql.connector as mysql
from pathlib import Path
from sqlalchemy import create_engine


file = open("20200102.txt")
#print(query)
engine = create_engine('mysql://example:example@localhost/stockinfo') #Creates database connection
data = pandas.read_csv(file, sep=",", header=None)  #Reads a given file, separates the data and adds to dataframe
data.columns = ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume'] #Defines Column Names for Dataframe
#Need to add function to clean datum pieces
#Convert datum to appropriate string format
data.to_sql("stocks", engine, if_exists='append') #to table STOCKS, using current DB connection, append to SQL
#print(data)

file.close()
x = input()#Pause to test program runs through,i know theres a better way
time.sleep(1) #||
