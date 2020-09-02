import time
import pandas
import numpy

#Ticker, Date, Open, High, Low, Close, Volume.
#Comment with #
print("Hello, World!")
a = "Hello"


file = open("2020jan/20200102.txt")
for x in file:
    #Gets line as a string
    line = file.readline()
    #Appends "Quotes" for ticker field rendering it as a string
    # MAY BE OBSOLETE
#    line = line[:0] + "'" + line[0:]
#    line = line[:4] + "'" + line[4:]
    print(line)
    #For each character in the line array replace
    for y in line:
         array = []
#        index = []
         #Creates array from the seperated text by "," symbol
         array.append(line.replace(","," ").split())
#        #pandas.Series(array[5], index=['Ticker','Date','Open','High','Low','Close','Volume'])
#         print(array)


        #Mini Array for each line assigns columns to temporary array
    #frameLine = pandas.DataFrame(line)
    #index=['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
#    print(line)

#data = pandas.DataFrame(file, columns=['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

#print(array)

#print(data)
file.close()
time.sleep(100)
