# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Lists and tuples are both iterables meaning they can both be iterated over. However, lists are mutable and tuples are not. One of the most important consequences of this is that lists may have multiple variables that are tied to the same list object. This can cause unintended consequences when naively attempting to copy a list. Being immutable, tuples will work as keys in dictionaries; in general, any non-mutable type will work as a key.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Lists and sets are both mutable interables. However, sets do not contain duplicates. Also, sets are not allowed to contain mutable objects, like lists or other sets. This allows them to be hashable - like dictionaries. Hash functions match values to an index. This allows for quick finding of any particular element since sets can call the hash function when looking for an element while lists need to potentially iterate through the whole list to find an element.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> `lambda` is a key word for defining a function. It is used when one wants to define an unamed, single-use function - typically one that is embedded in another expression. Here's an example that filters out all numbers with digits that do not sum to an even number for the first 100 positive integers:
> 
>  ```python
   filter(lambda x: sum(int(i) for i in str(x))%2==0, range(100))
   ```
>  
> And here's an example with a lambda function in the key argument to sorted. I'll sort the first 100 positive integers by the sum of their digits: 
> 
>  ```python
   sorted(range(100), key = lambda x: sum(int(i) for i in str(x)))
   ```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehensions let you define a list by iterating through an iterable. They enable you to do any operation you want with each item of an iterable to create your list. For example, let's say you want to create a list that is the result of feeding every positive integer from 0 to 99 inclusive to a function named `foo`. You can do that with the `map` function:
> 
> ```python
   map(foo,range(100))
   ```
> 
> And equivelently you can do that with a list comprehension like this:
> 
> ```python
   [foo(i) for i in range(100)]
   ```
> 
> 
> List comprehensions also allow you to create a condition to enable only certain items to be included in your list. Let's say we want to know how many of the non-negative integers between 0 and 99 inclusive are not divisable by 2 or 3. We could use `filter` like this:
> 
> ```python
   len(filter(lambda x: x%2 and x%3, range(100)))
   ```
> 
> Or we could use a list comprehension like this:
> 
> ```python
   sum([1 for i in range(100) if i%2 and i%3])
   ```
> 
> 
> Set comprehensions are cool. Let's try making a list of all the prime numbers less than 100 using a set comprehension and the sieve of Eratosthenes :
> 
> ```python
   filter(lambda x: 0 not in set(x%i for i in range(2,int(round(x**.5))+1)), range(2,100))
   ```
> 
> Here's an example of a dictionary comprehension. It takes a list and makes a 'histogram' which maps each unique item in the list to the number of times it appears:
> 
> First let's create a random list of integers and then print out the histogram of frequencies:
> 
> ```python
> import random
> foo = [random.choice(range(7)) for _ in range(70000)]
> {item: foo.count(item) for item in set(foo)}
>  ## {0: 10057, 1: 9963, 2: 10041, 3: 10047, 4: 9974, 5: 9923, 6: 9995}
> ```
   

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





