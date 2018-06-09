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
    
    totVot = int(len(ids))

    def countX(lst, y):
        count = 0
        for ele in lst:
            if (ele == y):
                count = count + 1
        return count
    
   
    print('File Name: ' + str(input_file), file=open('ElectionResults.txt', 'a+'))
    print('Election Results', file=open('ElectionResults.txt', 'a+'))
    print('Election Results')
    print(30 * '-', file=open('ElectionResults.txt', 'a+'))
    print(30 * '-')
    
    print('Total Votes: ' + str(totVot), file=open('ElectionResults.txt', 'a+'))
    print('Total Votes: ' + str(totVot))
    print(30 * '-', file=open('ElectionResults.txt', 'a+'))
    print(30 * '-')
    
    
    unique_list = []
    tmp_name = ''
    tmp_tally = 0
     
    for x in candidates:
            if x not in unique_list:
                unique_list.append(x)
                
    for x in unique_list:
            
            tally = int(countX(candidates,x))
            
            if tally > tmp_tally:
                  tmp_tally = tally
                  tmp_name = x
                  
            per = float(tally)/float(totVot) * 100
        
            print(x + ': ' + str(tally) + " votes or " + str(per) + "%", file=open('ElectionResults.txt', 'a+'))
            print(x + ': ' + str(tally) + " votes or " + str(per) + "%")
            
            
  
    print(30 * '-', file=open('ElectionResults.txt', 'a+'))
    print(30 * '-')
    print('Winner: '+ tmp_name, file=open('ElectionResults.txt', 'a+'))
    print('Winner: ' + tmp_name)
    print(30 * '-', file=open('ElectionResults.txt', 'a+'))
    print(30 * '-')
    print('\n', file=open('ElectionResults.txt', 'a+'))
    print('\n')