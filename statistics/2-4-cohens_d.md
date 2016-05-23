[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

 ``` python
 import nsfg
 import thinkstats2
 preg = nsfg.ReadFemPreg()
 firsts = preg[preg.birthord==1]
 others = preg[preg.birthord!=0]
 print thinkstats2.CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb)
 
 ## -0.0457262384721
 ```

This represents a small effect size however it is almost twice as large as the effect size for the difference in pregnancy length between these same groups.

I didn't write my own function since the function is pretty basic. Plus I've heard being lazy is a positive attribute sometimes!
