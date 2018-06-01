import os
import csv

with open(input("What is the name of the file: "), 'rU') as input_file:
    readCSV = csv.reader(input_file, delimiter=',')
    ids = []
    counties = []
    candidates = []

    header = next(readCSV)
    for row in readCSV:
        id = row[0]
        county = row[1]
        candidate = row[2]

        ids.append(id)
        counties.append(county)
        candidates.append(candidate)
    
    totVot = float(len(ids))

    def unique(list1):

        unique_list = []
     
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        for x in unique_list:
       
            temp = 0

            tally = int(countX(candidates,x))

            name = str(x)

            per = float(tally)/float(totVot) * 100

            if (tally > temp):
                temp = tally

        

            print(x + ': ' + str(countX(candidates,x)) + " votes or " + str(per) + "%")

        
            

    def countX(lst, y):
        count = 0
        for ele in lst:
            if (ele == y):
                count = count + 1
        return count

    

    print('File Name: ' + str(input_file), file=open('ElectionResults.txt', 'a+'))
    print('Election Results', file=open('ElectionResults.txt', 'a+'))
    print('Election Results')
    print('-------------------------------', file=open('ElectionResults.txt', 'a+'))
    print('-------------------------------')
    
    print('Total Votes: ' + str(totVot), file=open('ElectionResults.txt', 'a+'))
    print('Total Votes: ' + str(totVot))
    print('-------------------------------', file=open('ElectionResults.txt', 'a+'))
    print('-------------------------------')
    print(unique(candidates), file=open('ElectionResults.txt', 'a+'))
    print('-------------------------------', file=open('ElectionResults.txt', 'a+'))
    print('-------------------------------')
    print('Winner: ', file=open('ElectionResults.txt', 'a+'))
    # print('Winner: ' + str(name))
    print('-------------------------------', file=open('ElectionResults.txt', 'a+'))
    print('-------------------------------')
    print('\n', file=open('ElectionResults.txt', 'a+'))
    print('\n')
