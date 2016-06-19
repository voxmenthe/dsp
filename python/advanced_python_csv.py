###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file
import pandas as pd
import csv
fac = pd.read_csv('faculty.csv')
fac.columns = ['name','degree','title','email']
emailadds = fac['email']
#emailadds.to_csv('emails.csv',sep='\n')
with open('emails.csv', 'w') as export:
    for row in emailadds:
     	export.write('{}\n'.format(row))