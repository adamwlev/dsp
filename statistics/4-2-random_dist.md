[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)


```python
import random
import thinkstats2
import thinkplot
```

```python
random_nums = [random.random() for _ in range(1000)]
random_pmf = thinkstats2.Pmf(random_nums,label='random')
% matplotlib inline
thinkplot.Pmf(random_pmf)
thinkplot.Show()
```

![Pmf](https://github.com/adamwlev/dsp/blob/master/img/4-2_files/4-2_1_0.png)


```python
thinkplot.Cdf(thinkstats2.Cdf(random_nums,label='random'))
thinkplot.Show()
```

![Cdf](https://github.com/adamwlev/dsp/blob/master/img/4-2_files/4-2_2_0.png)
