import time, pandas, numpy, os, glob, sqlalchemy
import mysql
import mysql.connector as mysql
from pathlib import Path
from sqlalchemy import create_engine

engine = create_engine('mysql://example:example@localhost/stockinfo') #Creates database connection

def filetodb(inputFile, directory):
    inputfile = directory + inputFile
    file = open(inputfile)
    data = pandas.read_csv(file, sep=",")  #Reads a given file, separates the data and adds to dataframe
    data.columns = ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume'] #Defines Column Names for Dataframe
    dataframetest = data.loc[:]    #Need to add function to clean datum pieces
    print(dataframetest)
    file.close()

startpath = 'Data/'
basepath = os.listdir(startpath) #Displays all subfolders in /Data/
for x in basepath:
    i = startpath + x + "/" #Creates a new directory query for next directory readthrough
    folderfiles = os.listdir(i) # lists all the files in a folder
    for y in folderfiles:   #for each file in folder files
            if ".txt" in y: #y is the name of the text file
                filetodb(y,i)

    #Convert datum to appropriate numerical format
    #Add table with correct table format
    #data.to_sql(table, engine, if_exists='append') #to table STOCKS, using current DB connection, append to SQL


#def dbadd(filename, date):
    #Format create table query with proper column FORMATS


#def createdatabase(date):


file.close()
x = input()#Pause to test program runs through,i know theres a better way
time.sleep(1) #||
