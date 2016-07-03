"""
[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Exercise 1   In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” (70" = 177.8cm) and 6’1” (73" = 185.42cm) (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

>> CODE BELOW
"""
def EvalNormalCdf(x, mu=0, sigma=1):
    return scipy.stats.norm.cdf(x, loc=mu, scale=sigma)

EvalNormalCdf(177.8, mu=178, sigma=7.7) # 0.48963902786483265
EvalNormalCdf(185.42, mu=178, sigma=7.7) # 0.83238586549630633
0.83238586549630633 - 0.48963902786483265 # 0.3427468376314737

# Thus the percentage of the male population that falls in the range is 34%