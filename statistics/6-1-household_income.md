[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

```python
import hinc
```


```python
df = hinc.ReadData()
```


```python
import hinc2
import numpy as np
import thinkstats2
```

Upper Bound default of 10^6


```python
sample = [10**i for i in hinc2.InterpolateSample(df)]
```


```python
cdf = thinkstats2.Cdf(sample)
pmf = thinkstats2.Pmf(sample)
print 'Median of sample is ',cdf.Value(.5)
print 'Mean of sample is ',np.mean(sample)
print 'The sample skewness of the sample is ',thinkstats2.Skewness(sample)
print "The Pearson's skewness of the sample is ",thinkstats2.PearsonMedianSkewness(sample)
print 'The fraction of observations above the mean is ',1-cdf.Prob(np.mean(sample))
```

    Median of sample is  51226.4544789
    Mean of sample is  74278.7075312
    The sample skewness of the sample is  4.94992024443
    The Pearson's skewness of the sample is  0.736125801914
    The fraction of observations above the mean is  0.339994120433


Let's say the Upper Bound is 10^8 now


```python
sample = [10**i for i in hinc2.InterpolateSample(df,log_upper=8.0)]
```


```python
cdf = thinkstats2.Cdf(sample)
pmf = thinkstats2.Pmf(sample)
print 'Median of sample is ',cdf.Value(.5)
print 'Mean of sample is ',np.mean(sample)
print 'The sample skewness of the sample is ',thinkstats2.Skewness(sample)
print "The Pearson's skewness of the sample is ",thinkstats2.PearsonMedianSkewness(sample)
print 'The fraction of observations above the mean is ',1-cdf.Prob(np.mean(sample))
```

    Median of sample is  51226.4544789
    Mean of sample is  457453.487247
    The sample skewness of the sample is  14.8924598044
    The Pearson's skewness of the sample is  0.274790973381
    The fraction of observations above the mean is  0.0213705923664


The sample skewness for a larger upper bound is predictibly much larger. Interestingly, the Pearson's Median Skewness actually went down for this larger bound (probably because the difference between the mean and median is drowned out by the large increase in the standard deviation of the sample).
