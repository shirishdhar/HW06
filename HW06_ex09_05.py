#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
import os
def uses_all(word, string):
	count=0
	for letter in string:
		if letter in word:
			count+=1
	if count==len(string):
		return True
	else:
		return False

def vowels():
	f=open('words.txt', 'r')
	string='aeiou'
	main_count=0
	for line in f:
		count=0
		for letter in string:
			if letter in line:
				count+=1
		if count==5:
			main_count+=1
	print main_count
	f.close()

def vowels_plus_y():
	f=open('words.txt', 'r')
	string='aeiouy'
	main_count=0
	for line in f:
		count=0
		for letter in string:
			if letter in line:
				count+=1
		if count==5:
			main_count+=1
	print main_count


# Imports

# Body


##############################################################################
def main():
	#print uses_all('hibernation','bink')
	vowels()
	vowels_plus_y()
    

if __name__ == '__main__':
    main()
