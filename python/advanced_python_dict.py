### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
"""
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }

Print the first 3 key and value pairs of the dictionary:

>> 
"""


# temp:
"""
import pandas as pd
from collections import Counter

# create dataframe
faculty = pd.read_csv('faculty.csv')
faculty.columns = ['name','degree','title','email']

# create array of names
names = []
for item in faculty["name"]:
    names.append(item.split(" "))

# create array of last names
lastnames = []
for item in names:
    lastnames.append(item[-1])

faculty["lastname"] = lastnames

# create array of role titles:
roles = []
for item in faculty["title"]:
    A = 'Assistant Professor'
    B = 'Associate Professor'
    C = 'Professor'
    if A in item:
        roles.append(A)
    elif B in item:
        roles.append(B)
    else:
        roles.append(C)

faculty["role"] = roles

# delete columns - don't run twice
# to avoid issues with this can create
# copy of the "faculty" dataframe
# but wasn't necessary in this instance
del faculty["name"]
del faculty["title"]

# prepare lists to insert into dictionary
faclists= []
for row in faculty.iterrows():
    index, data = row
    faclists.append(data.tolist())

# create dictionary
faculty_dict = {}
for x in faclists:
    faculty_dict[x[2]] = []
for idx, y in enumerate(faclists):
    for z in faculty_dict:
        if y[2] == z:
            faculty_dict[z].append([
                    faclists[:][idx][0],
                    faclists[:][idx][3],
                    faclists[:][idx][1]])

# modify dictionary to allow printing of first n items
import collections
import itertools
faculty_dict = collections.OrderedDict(faculty_dict)

# print first 3 items
x = itertools.islice(faculty_dict.items(), 0, 3)

for key, value in x:
    print(key, value)

#temp:
"""

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

"""
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }

Print the first 3 key and value pairs of the dictionary:
"""

import pandas as pd
from collections import Counter
faculty = pd.read_csv('faculty.csv')
faculty.columns = ['name','degree','title','email']

# create array of names
names = []
for item in faculty["name"]:
    names.append(item.split(" "))

# create arrays of first and last names
firstnames = []
lastnames = []
for item in names:
    firstnames.append(item[0])
    lastnames.append(item[-1])

faculty["firstname"] = firstnames
faculty["lastname"] = lastnames

# create array of role titles:
roles = []
for item in faculty["title"]:
    A = 'Assistant Professor'
    B = 'Associate Professor'
    C = 'Professor'
    if A in item:
        roles.append(A)
    elif B in item:
        roles.append(B)
    else:
        roles.append(C)

faculty["role"] = roles

# delete columns - don't run twice
# to avoid issues with this can create
# copy of the "faculty" dataframe
# but wasn't necessary in this instance
del faculty["name"]
del faculty["title"]

# prepare lists to insert into dictionary
faclists= []
for row in faculty.iterrows():
    index, data = row
    faclists.append(data.tolist())

# create the dictionary
professor_dict = {}
for x in faclists:
    professor_dict[(x[2],x[3])] = []
for idx, y in enumerate(faclists):
    for z in professor_dict:
        if (y[2],y[3]) == z:
            professor_dict[z].append(faclists[:][idx][0])
            professor_dict[z].append(faclists[:][idx][4])
            professor_dict[z].append(faclists[:][idx][1])

# prepare dictionary for printing
import collections
import itertools
professor_dict = collections.OrderedDict(professor_dict)
professor_dict = sorted(professor_dict.items(), key=lambda key: key[0])
professor_dict = collections.OrderedDict(professor_dict)

# print the first 3 items
x = itertools.islice(professor_dict.items(), 0, 3)

# note using python-2-style printing here
for key, value in x:
    print key, value


####Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  

#code is same as above but with the following changes:

# prepare dictionary for printing with sorting
import collections
import itertools
from operator import itemgetter
professor_dict = collections.OrderedDict(professor_dict)
professor_dict = sorted(professor_dict.items(), key= lambda key: key[0][1])
professor_dict = collections.OrderedDict(professor_dict)

x = itertools.islice(professor_dict.items(), 0, 3)

for key, value in x:
    print(key, value)
