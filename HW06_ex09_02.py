#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports
def has_no_e():
	total_lines=0
	non_e_lines=0
	f=open('words.txt','r')
	for line in f:
		total_lines+=1
		if 'e' not in line:
			non_e_lines+=1
			print line                                        #Printing lines without an 'e'
	print 'There are %d words without e' %non_e_lines
	percentage= (non_e_lines/float(total_lines)) * 100
	print "%f%%  of the words do not have e " %percentage
	f.close()



# Body


##############################################################################
def main():
	has_no_e()
    

if __name__ == '__main__':
    main()
