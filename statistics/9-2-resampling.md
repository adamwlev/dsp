[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

```python
import thinkstats2
import numpy as np
import hypothesis
import first
```

```python
live, firsts, others = first.MakeFrames()
```

```python
class DiffMeansResample(hypothesis.DiffMeansPermute):
    def RunModel(self):
        ns = np.random.choice(self.pool[:self.n],self.n,replace=True)
        ms = np.random.choice(self.pool[:self.m],self.m,replace=True)
        return (ns,ms)
```

```python
data = firsts.prglngth.values, others.prglngth.values
ht = DiffMeansResample(data)
p_value = ht.PValue(iters=10000)
print 'means permute preglength'
print 'p-value = %g' % (p_value,)
print 'actual = %g' % (ht.actual,)
print 'ts max = %g' % (ht.MaxTestStat(),)
```

    means permute preglength
    p-value = 0.187
    actual = 0.0780373
    ts max = 0.222025


With resampling instead of pooling, the p-value for the null hypothesis that there is no difference in the prglength between first and other babies is very similiar to what it was for pooling (it was 0.17, now it's 0.18).


```python
data = firsts.prglngth.values, others.prglngth.values
ht = DiffMeansResample(data)
p_value = ht.PValue(iters=10000)
print 'means permute preglength'
print 'p-value = %g' % (p_value,)
print 'actual = %g' % (ht.actual,)
print 'ts max = %g' % (ht.MaxTestStat(),)
```

    means permute preglength
    p-value = 0.1815
    actual = 0.0780373
    ts max = 0.285163


Similiarly, the p-value for the null hypothesis that there is not difference in the birthweight of first babies versus others is 0 just as it was with the pooling procedure. This means that it is extreemly unlikely that the difference in means observed in the groups would ever present itself as a result of random fluctuations (aka sampling bias).
