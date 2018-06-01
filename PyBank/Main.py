import os
import csv

with open(input("What is the name of the file: "), 'rU') as input_file:
    readCSV = csv.reader(input_file, delimiter=',')
    values = []
    dates = []
    header = next(readCSV)
    for row in readCSV:
        value = row[1]
        date = row[0]
        dates.append(date)
        values.append(float(value))
    print('File Name: ' + str(input_file), file=open('FinancialBudget.txt', 'a+'))
    print('Financial Analysis', file=open('FinancialBudget.txt', 'a+'))
    print('Financial Analysis')
    print('-------------------------------', file=open('FinancialBudget.txt', 'a+'))
    print('-------------------------------')
    totMon = len(dates)
    print('Total Months: ' + str(totMon), file=open('FinancialBudget.txt', 'a+'))
    print('Total Months: ' + str(totMon))
    theSum = sum(values)
    print('Total Revenue: ' + str(theSum), file=open('FinancialBudget.txt', 'a+'))
    print('Total Revenue: ' + str(theSum))
    totAv = sum(values)/float(len(dates))
    print('Average Revenue Change: ' + str(totAv), file=open('FinancialBudget.txt', 'a+'))
    print('Average Revenue Change: ' + str(totAv))
    maxVal = max(values)
    indMax = values.index(maxVal)
    print('Greatest Increase in Revenue: ' + dates[indMax] + ' ' + str(maxVal), file=open('FinancialBudget.txt', 'a+'))
    print('Greatest Increase in Revenue: ' + dates[indMax] + ' ' + str(maxVal))
    minVal = min(values)
    indMin = values.index(minVal)
    print('Greatest Decrease in Revenue: ' + dates[indMin] + ' ' + str(minVal), file=open('FinancialBudget.txt', 'a+'))
    print('Greatest Decrease in Revenue: ' + dates[indMin] + ' ' + str(minVal))
    print('\n', file=open('FinancialBudget.txt', 'a+'))
    print('\n')
