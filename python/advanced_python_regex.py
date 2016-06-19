"""
For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

###Part I - Regular Expressions  
"""

####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

import pandas as pd
from collections import Counter
fac = pd.read_csv('faculty.csv')
fac.columns = ['name','degree','title','email']
degreefrequencies = Counter(fac["degree"])

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

titlefrequencies = Counter(fac["title"])

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

print(list(emailadds = fac["email"]))

####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

def getUniqueDomains(listofemails):
	result = []
  	for x in listofemails:
    		result.append(x.split('@')[1])
  	print(list(set(result)))

getUniqueDomains(emailadds)
