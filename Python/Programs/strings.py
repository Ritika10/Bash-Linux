#!/usr/intel/bin/python2.6.5 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  if len(s)>2:
      return s[:2]+s[-2:]
  else:
      return ""

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    first=s[0]
    return first+s.replace(first,'*')[1:]

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  pass

# Given a string, capitalize every word in the string
def capitalize_words(s):
  pass

# Given a string, convert it into pig latin
# In order to convert a word into pig latin, remove the first character
# of the word, then place that character + 'ay' after the word
# For example, 'pig' becomes 'ig pay' and 'latin' becomes 'atin yay'
def pig_latin(s):
  pass

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = '  OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

  print("\n")
  print ('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

  print("\n")
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')

  print("\n")
  print ('capitalize_words')
  test(capitalize_words('the quick and the dead'), 'The Quick And The Dead')
  test(capitalize_words('star wars'), 'Star Wars')
  test(capitalize_words('william h. macy'), 'William H. Macy')
  test(capitalize_words("the handmaid's tale"), "The Handmaid's Tale")

  print ("\n")
  print ('pig_latin')
  test(pig_latin('pig latin'), 'ig pay atin lay')
  test(pig_latin('you are smart'), 'ou yay re aay mart say')
  test(pig_latin('french toast'), 'rench fay oast tay')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
