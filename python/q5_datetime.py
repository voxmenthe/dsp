# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

# code:
from dateutil.parser import parse
(parse(date_stop) - parse(date_start)).days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

# code:
from dateutil.parser import parse

date_start = 
	str(date_start[0:2]) + "-" + str(date_start[2:4]) + "-" + str(date_start[4:8])

date_stop = 
	str(date_stop[0:2]) + "-" + str(date_stop[2:4]) + "-" + str(date_stop[4:8])

(parse(date_stop2) - parse(date_start2)).days


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

# code:
from dateutil.parser import parse

(parse(date_stop) - parse(date_start)).days

