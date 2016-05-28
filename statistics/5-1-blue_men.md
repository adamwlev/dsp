[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
def in_to_cm (i):
    return 2.54*i
dist.cdf(in_to_cm(73))-dist.cdf(in_to_cm(70))

## 0.34274683763147457
```

34.3% of males are between 6'1" and 5'10". 
