# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples can be thought of immutable lists where the indices have an implied meaning (which is inextricably tied up with their immutability). Thus tuples can be used as keys in dictionaries, because of the fixed "meaning" of their index values. Another distinction that follows from tuples' immutability is that you deal with tuples as a coherent unit, while with lists you generally deal with the items individually. Also tuple instantiation is usually faster than for lists, but item access for lists can sometimes be faster or similar. If you want to change anything tuples are slower since you need to re-instantiate. Tuples take less space in memory since fixed (no need to overallocate). 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>  Sets are iterable sequences like lists and tuples but the elements in a set must be unique, and the order is arbitrary. Thus sets can use the union, intersect, difference and symmetric difference methods. Also the items in a set must be immutable, thus 

Usage-wise, if you care about order, you need to use a list. If you don't want duplicates, use a set. If you need to associate values with unique keys so you can look them up later, use a dictionary.

Performance-wise, when you want to store values to iterate over, lists are faster, but if you're storing unique values to check for their existence, sets are usually much faster.

Examples:
list1 = [["Janice","Dalton"],["Bill","Murray"],["Chloe","Montaigne"]]
for x in list1:
	print(x[0] + " " + x[1])

set1 = ["Janice Dalton","Bill Murray","Chloe Montaigne"]
if "Janice Dalton" in set1 print("Hello Janice")

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda is an anonymous function definition operator.

Lambda Examples:
sometups = [(0, -54, -78),(1, 3, -2),(-1, 0, 4),(0, -1, 3),(-2, 6, -5),(0, 23, 17)]
sorted(sometups, key = lambda item: item[1]) # sorts by the 2nd item in each tuple

(lambda x: x+2)(3) # 5

list3 = [23,5,6,7,8,2,3,4,5,6,7,8,9]
sorted(list3, key = lambda x: x-(x*2)) # [23, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 3, 2]

[lambda x: x*x for x in range(10)]
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Python's list comprehensions are a cute syntax for transforming any one list into another list, or for constructing a list from a function. They essentially support using the functionality of map and filter in a different (simpler?) syntax.

List comprehension examples:
list3 = [23,5,6,7,8,2,3,4,5,6,7,8,9]

[print(x) for x in list3]

[v * 5 for v in list3 if not v % 2] 
# Out: [30, 40, 10, 20, 30, 40]

list(map(lambda v : v *5, filter(lambda u : not u % 2, list3))) 
# Out: [30, 40, 10, 20, 30, 40]
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

# code:
from dateutil.parser import parse
(parse(date_stop) - parse(date_start)).days

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

# code:
from dateutil.parser import parse

date_start = 
	str(date_start[0:2]) + "-" + str(date_start[2:4]) + "-" + str(date_start[4:8])

date_stop = 
	str(date_stop[0:2]) + "-" + str(date_stop[2:4]) + "-" + str(date_stop[4:8])

(parse(date_stop2) - parse(date_start2)).days

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```
# code:
from dateutil.parser import parse

(parse(date_stop) - parse(date_start)).days

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





