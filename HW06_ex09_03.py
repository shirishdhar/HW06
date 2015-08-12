#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
def avoids():
        string=raw_input('Enter a string of forbidden letters: ')
        f=open('words.txt','r')
        main_count=0
        for word in f:
            count=0
            for letter in string:
                lU=letter.upper()
                if (letter not in word) and (lU not in word):                       #Accounts for both lowercase and uppercase
                    count+=1
            if count==len(string):                                                  #Checks if all the forbidden letters are absent from the word
                main_count+=1
        print main_count
        f.close()

def key(s):                                                                         #Defined a 'key' function which is used by the sorted() method later to sort the list.
    return int(s[2:])


def combination():
        alphabet='abcdefghijklmnopqrstuvwxyz'
        f=open('words.txt', 'r')
        final_list=[]
        for letter in alphabet:
            count=0
            f.seek(0)
            for word in f:
                if letter in word:                                                  
                    count+=1                                                        #Finds number of occurences of each letter in the alphabet
            final_list.append(letter+' '+str(count))
        sorted_list= sorted(final_list,key=key)                                     #List contains the letter followed by a space followed by the occurence number.
        print sorted_list[:5]                                                       #So, we use the key to return only the numeric part of each list element, which makes sorting by numbers possible.
        f.close()


##############################################################################
def main():
    #avoids()
    combination()

if __name__ == '__main__':
    main()
