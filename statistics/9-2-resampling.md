[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

``python
import thinkstats2
import numpy as np
import hypothesis
import first
```

```python
live, firsts, others = first.MakeFrames()
```

```python
class DiffMeansPermute(thinkstats2.HypothesisTest):
    """Tests a difference in means by permutation."""

    def TestStatistic(self, data):
        """Computes the test statistic.

        data: data in whatever form is relevant        
        """
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat

    def MakeModel(self):
        """Build a model of the null hypothesis.
        """
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        """Run the model of the null hypothesis.

        returns: simulated data
        """
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data
```

```python
class DiffMeansResample(DiffMeansPermute):
    def RunModel(self):
        ns = np.random.choice(self.pool,self.n,replace=True)
        ms = np.random.choice(self.pool,self.m,replace=True)
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
    p-value = 0.1666
    actual = 0.0780373
    ts max = 0.240183


With resampling instead of pooling, the p-value for the null hypothesis that there is no difference in the prglength between first and other babies is very similiar to what it was for pooling (it was 0.17, now it's 0.1666).


```python
data = firsts.birthwgt_lb.values, others.birthwgt_lb.values
ht = DiffMeansResample(data)
p_value = ht.PValue(iters=10000)
print 'means permute preglength'
print 'p-value = %g' % (p_value,)
print 'actual = %g' % (ht.actual,)
print 'ts max = %g' % (ht.MaxTestStat(),)
```

    means permute preglength
    p-value = 0
    actual = nan
    ts max = nan


Similiarly, the p-value for the null hypothesis that there is not difference in the birthweight of first babies versus others is 0 just as it was with the pooling procedure. This means that it is extreemly unlikely that the difference in means observed in the groups would ever present itself as a result of random fluctuations (aka sampling bias).