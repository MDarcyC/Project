import time
import pandas
import numpy

#Ticker, Date, Open, High, Low, Close, Volume.
#Comment with #
#print("Hello, World!")

file = open("2020jan/20200102.txt")
def getPriceInfo(inputFile):
    zvalue = []
    for x in inputFile: #Layer loop for reading lines
        line = file.readline()  #Gets line as a string
        lineArray = line.split(",") #Turns String to Array
        zvalue.append(lineArray[1:6])
    return zvalue
tickerInfo = getPriceInfo(file)
print(tickerInfo)
file.close()

file = open("2020jan/20200102.txt")
def getTicker(inputFile):
    rvalue = []
    for x in inputFile: #Layer loop for reading lines
        line = file.readline()  #Gets line as a string
        lineArray = line.split(",") #Turns String to Array
        rvalue.append(lineArray[0])
    return rvalue
listOfTickers = getTicker(file)
print(listOfTickers)
file.close()





def read(inputFile):
    for x in inputFile: #Layer loop for reading lines
        line = file.readline()  #Gets line as a string
        lineArray = line.split(",")
        print(lineArray)
        return lineArray




#    return zvalue
#        line = lineArray.append(line.replace(","," ").split())  #Appends "Quotes" for ticker field rendering it as a string












#data = pandas.DataFrame(file, columns=['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

#print(array)

#print(data)
file.close()
x = input()
time.sleep(1)
