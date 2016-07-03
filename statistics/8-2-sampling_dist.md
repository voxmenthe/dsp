"""
[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)
Exercise 2  
Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.
Repeat the experiment with a few different values of n and make a plot of standard error versus n.
>> Code below
"""
def Estimate3a(n=10, m=1000):
    lam = 2

    means = []
    medians = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        Lm = math.log(2) / thinkstats2.Median(xs)
        means.append(L)
        medians.append(Lm)
    
    cdf = thinkstats2.Cdf(means)    
    ci = cdf.Percentile(5), cdf.Percentile(95)

    return RMSE(means, lam), ci

def expRMSE(start, stop, step):
    results = []
    for i in range(start,stop,step):
        results.append(list([i,Estimate3a(n=i)]))
    return results

# It can be seen in the following table output (n, stderr, ci) that as
# n goes down, the standard error goes down and the confidence interval tightens:

[[10, (0.7786432940740008, (1.2528717987156206, 3.6065374396546583))],
 [20, (0.48792185791547893, (1.4336104099282865, 2.9019721878353995))],
 [30, (0.40109003683918937, (1.51165751957409, 2.75941974521356))],
 [40, (0.33648497900168145, (1.5604336363648328, 2.6329136252470704))],
 [50, (0.29641561186979104, (1.6199293683146658, 2.5666478144073013))],
 [60, (0.26291553140980095, (1.6296076253503002, 2.4824281427719126))],
 [70, (0.24972717488296248, (1.6628646144987558, 2.4892769481282451))],
 [80, (0.22604650403763407, (1.6749558650641114, 2.4093659909352381))],
 [90, (0.21255006005314384, (1.6995242868802589, 2.4003124695926759))]]    