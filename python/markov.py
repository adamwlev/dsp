#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

from __future__ import print_function
import random
import sys

def make_prefixes (words, order):
	prefixes = dict()
	for u in xrange(len(words)-order):
		if tuple(words[u:u+order]) in prefixes:
			prefixes[tuple(words[u:u+order])][words[u+order]] = prefixes[tuple(words[u:u+order])].get(words[u+order],0) + 1
		else:
			prefixes[tuple(words[u:u+order])] = dict()
			prefixes[tuple(words[u:u+order])][words[u+order]] = 1
	return prefixes

def rand_choice_from_dict (d):
	r = random.choice(xrange(1,len(d)+1))
	cum_sum = 0
	for key in d:
		cum_sum += d[key]
		if r <= cum_sum:
			return key

def print_random_words (d, n):
	startind = random.choice(xrange(len(d)))
	for u,prefix in enumerate(d):
		if u==startind:
			start = prefix
			break
	print(" ".join(start),end=" ")
	for i in range(n):
		new_word = rand_choice_from_dict(d[start])
		print(new_word,end="")
		start = start[1:] + (new_word,)
		if i < n-1:
			print(" ",end="")
		else:
			print("")

def main(*args):
	order = 3 ##size of each prefix
	filename = args[1]
	no_of_words = args[2]
	try:
		no_of_words = int(no_of_words)
	except:
		print('Usage: markov.py filename1 # of words')
	else:
		words = []
		f = open(filename)
		words.extend(f.read().split())
		f.close()
		p = make_prefixes(words,order)
		print_random_words(p,no_of_words-order)

if __name__ == '__main__':
 	main(*sys.argv)
