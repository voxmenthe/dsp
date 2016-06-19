#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def readfile_array(filename):
    result = []
    with open(filename, 'rb') as csvfile:
        filedata = csv.reader(csvfile, delimiter=',')
        for row in filedata:
            result.append(row)
    return result

def get_min_score_diff(data_array):
    import sys
    result = [sys.maxint,""]
    for idx, row in enumerate(data_array):
        if idx != 0:
            diff = abs(int(row[-3])-int(row[-2]))
            if diff < result[0]:
                result[0] = diff
                result[1] = row[0]
    print result[1]
    return result[1]

footballdata = readfile_array('football.csv')
get_min_score_diff(footballdata)
