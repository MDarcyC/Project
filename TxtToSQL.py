import time, pandas, numpy, os, glob, sqlalchemy
import mysql
import mysql.connector as mysql
from pathlib import Path
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

engine = create_engine('mysql://test.test@localhost/stockinfo', echo = True) #Creates database connection

def name_to_date(inputFile):
    YY = inputFile[0:4]
    MM = inputFile[4:6]
    DD = inputFile[6:8]
    dateFormat = YY + "-" + MM + "-" + DD
    return dateFormat

def table_to_query(inputFile):
    meta = MetaData()
    inputFile = str(inputFile)
    query = Table(inputFile, meta,
       Column('index', Integer),
       Column('ticker', String(20)),
       Column('date', Date),
       Column('open', Integer),
       Column('high', Integer),
       Column('low', Integer),
       Column('close', Integer),
       Column('volume', Integer))
    meta.create_all(engine)
    print("MSQL")

def file_to_db(inputFile, directory):
    inputfile = directory + inputFile
    datef = name_to_date(inputFile)
    file = open(inputfile)
    data = pandas.read_csv(file, sep=",")  #Reads a given file, separates the data and adds to dataframe
    file.close()
    data.columns = ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume'] #Defines Column Names for Dataframe
    for i, row in data.iterrows():
        data.at[i,'date'] = pandas.to_datetime(i)
        data.at[i,'date'] = datef
        ticker = data.at[i,'date']
        data.at[i,'date'] = str(ticker)
        Table = inputFile[0:8]
    table_to_query(Table)
    data.to_sql(Table, engine, if_exists='append') #to table STOCKS, using current DB connection, append to SQL
    print(data)

startpath = 'Data/'
basepath = os.listdir(startpath) #Displays all subfolders in /Data/
for x in basepath:
    i = startpath + x + "/" #Creates a new directory query for next directory readthrough
    folderfiles = os.listdir(i) # lists all the files in a folder
    for y in folderfiles:
            if ".txt" in y:
                file_to_db(y,i)
            else:
                break

time.sleep(1) #||
