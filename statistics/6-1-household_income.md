"""
[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)
Exercise 1  
The distribution of income is famously skewed to the right. In this exercise, we’ll measure how strong that skew is.
The Current Population Survey (CPS) is a joint effort of the Bureau of Labor Statistics and the Census Bureau to study income and related variables. Data collected in 2013 is available from http://www.census.gov/hhes/www/cpstables/032013/hhinc/toc.htm. I downloaded hinc06.xls, which is an Excel spreadsheet with information about household income, and converted it to hinc06.csv, a CSV file you will find in the repository for this book. You will also find hinc2.py, which reads this file and transforms the data.

The dataset is in the form of a series of income ranges and the number of respondents who fell in each range. The lowest range includes respondents who reported annual household income “Under $5000.” The highest range includes respondents who made “$250,000 or more.”

To estimate mean and other statistics from these data, we have to make some assumptions about the lower and upper bounds, and how the values are distributed in each range. hinc2.py provides InterpolateSample, which shows one way to model this data. It takes a DataFrame with a column, income, that contains the upper bound of each range, and freq, which contains the number of respondents in each frame.

It also takes log_upper, which is an assumed upper bound on the highest range, expressed in log10 dollars. The default value, log_upper=6.0 represents the assumption that the largest income among the respondents is 106, or one million dollars.

InterpolateSample generates a pseudo-sample; that is, a sample of household incomes that yields the same number of respondents in each range as the actual data. It assumes that incomes in each range are equally spaced on a log10 scale.

Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?

>> REPLACE THIS TEXT WITH YOUR RESPONSE
"""
import hinc
import hinc2
import math
import numpy as np
import pandas as pd
import thinkstats2
import thinkplot

hincdata = hinc.ReadData()
sampleatlog = hinc2.InterpolateSample(hincdata, log_upper=6.0)
cdfatlog = thinkstats2.Cdf(sampleatlog, label = 'CDF in log')

median = cdfatlog.Value(.5) # 4.70949429822
mean = sampleatlog.mean() # 4.65758573589
var = sampleatlog.var() # 0.212369464462
std = sampleatlog.std() # 0.460835615445

# The mean is a bit less than the median so that's consistent with left skew.

def raw_moment(xs, k):
    return sum(x**k for x in xs)/len(xs)
def central_moment(xs, k):
    mean = raw_moment(xs, 1)
    return sum((x-mean)**k for x in xs)/len(xs)
def standardized_moment(xs, k):
    var = central_moment(xs,2)
    std = math.sqrt(var)
    return central_moment(xs,k)/std**k
def skewness(xs):
    return standardized_moment(xs,3)

skewness(sampleatlog)  # -0.64135436656621081

def pearson_skew(xs):
    median = np.median(xs)
    mean = raw_moment(xs,1)
    var = central_moment(xs,2)
    std = math.sqrt(var)
    gp = 3*(mean-median)/std
    return gp

pearson_skew(sampleatlog) # -0.33794666458482181

# So the skewness coefficients are both negative, indicating left skew

# What fraction of households reports a taxable income below the mean? 

cdfatlog.Prob(mean) # 0.45060347221088048

# Answer: around 45%

# How do the results depend on the assumed upper bound?

# function to create a range of upper bounds:

def makeUpperBounds(minval,maxval,step):
    result = []
    for val in range(minval,maxval,step):
        result.append(np.log10(val))
    return result

# function to create an array of upper bound, skewness and pearson skew:
def makeSkewRanges(upboundarray)
    skewranges = []
    for i in upboundarray:
        tempsampleatlog = hinc2.InterpolateSample(hincdata, log_upper=i)
        skewranges.append([i,skewness(tempsampleatlog),pearson_skew(tempsampleatlog)])
    returnskewranges

upbounds = makeUpperBounds(50000,1000000,500000)
skewtable = makeSkewRanges(upbounds)

# and so we can see in the table below that as the upper bound increases,
# the skewness decreases:
[[5.6989700043360187, -0.78027100204483202, -0.36776042752922677],
 [6.0, -0.64135436656621081, -0.33794666458482181],
 [6.1760912590556813, -0.54173205701914551, -0.32055446739929111],
 [6.3010299956639813, -0.46318704829921076, -0.30827820563809427],
 [6.3979400086720375, -0.39796843688090006, -0.29880702715093044],
 [6.4771212547196626, -0.3420117715536396, -0.29110828497062097],
 [6.5440680443502757, -0.29290059850294453, -0.28463056028039357],
 [6.6020599913279625, -0.24907292778098708, -0.27904470919120578],
 [6.653212513775344, -0.20945676195379692, -0.27413855164932549],
 [6.6989700043360187, -0.17328242875555391, -0.26976734617163572],
 [6.7403626894942441, -0.13997748231480556, -0.26582797072694175],
 [6.7781512503836439, -0.10910391966373148, -0.26224437901986791],
 [6.8129133566428557, -0.08031870201309417, -0.25895889724977311],
 [6.8450980400142569, -0.053347871261526437, -0.25592675610706561],
 [6.8750612633917001, -0.02796898034755485, -0.25311251489389247],
 [6.9030899869919438, -0.0039988118887109509, -0.25048764310404664],
 [6.9294189257142929, 0.018715425142890912, -0.24802883735251305],
 [6.9542425094393252, 0.040302544644392022, -0.24571682082772581],
 [6.9777236052888476, 0.060872198967002619, -0.24353546834304812]]