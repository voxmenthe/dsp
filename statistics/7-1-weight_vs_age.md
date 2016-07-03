"""
[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

Exercise 1   Using data from the NSFG, make a scatter plot of birth weight versus mother’s age. Plot percentiles of birth weight versus mother’s age. Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?

>> Code below:
"""
import math
import numpy as np
import pandas as pd
import thinkstats2
import thinkplot


# read the data and select records for live births
import nsfg
import nsfg2
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]


def Corr(xs, ys):
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    # MeanVar computes mean and variance slightly more efficiently 
    # than separate calls to np.mean and np.var.
    meanx, varx = thinkstats2.MeanVar(xs)
    meany, vary = thinkstats2.MeanVar(ys)

    corr = Cov(xs, ys, meanx, meany) / math.sqrt(varx * vary)
    return corr

def SpearmanCorr(xs, ys):
    import pandas as pd
    xs = pd.Series(xs)
    ys = pd.Series(ys)
    return xs.corr(ys, method='spearman')

# make a scatter plot of the data
birthweight = live2['totalwgt_lb']
mothersage = live2['agepreg']
thinkplot.Scatter(birthweight,mothersage)
thinkplot.Show(xlabel='Total Weight (lb)',
              ylabel='Mother Age')

# alternate scatter plot view
thinkplot.Scatter(mothersage, birthweight, alpha=0.3)
thinkplot.Config(xlabel='age (years)',ylabel='weight (lbs)',xlim=[10, 45],ylim=[0, 15],legend=False)

# plot by quartiles:
bins = np.arange(10, 48, 3)
indices = np.digitize(live2.agepreg, bins)
groups = live2.groupby(indices)

ages = [group.agepreg.mean() for i, group in groups][1:-1]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

thinkplot.PrePlot(3)
for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weights, label=label)


# Compute Pearson's correlation:
Corr(birthweight,mothersage) # 0.068833970354109084

# Compute Spearman correlation:
SpearmanCorr(birthweight,mothersage) # 0.094610041096582262

"""
Answer:
The scatterplot shows a weak correlation, but interestingly,
the variance in birthweight seems to decrease slightly as the
mother's age increases. 

Looking at a plot by quartiles, in all groups, there is an increase
in birthweight as the mother's age rises until it reaches around 38,
with a sharp dropoff thereafter.

The correlation numbers also point to a not-so-strong relationship,
with both near 0 (0.07 and 0.09)