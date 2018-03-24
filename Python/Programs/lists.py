#!/usr/intel/bin/python2.6.5 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count=0
    for word in words:
        if len(word)>=2 and word[0]==word[-1]:
            count +=1
    return count


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    list1, list2=[],[]
    for word in words:
        if word[0]=='x':
            list1.append(word)
        else:
            list2.append(word)
    return sorted(list1)+ sorted(list2)


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element from each tuple.
def sort_last(tuples):
    pass


# given a string s, return the number of times
# the last two characters in the string are found somewhere else
# in the string in the same order
def last2(s):
    pass


# given two lists, return a list of elements
# that are present in both lists in ascending order
# report any element that is duplicated only once
def intersection(xs, ys):
    pass


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print("\n")
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print("\n")
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

    print("\n")
    print('last2')
    test(last2('hixxhi'), 1)
    test(last2('xaxxaxaxx'), 1)
    test(last2('axxxaaxx'), 2)
    test(last2('xxaxxaxxaxx'), 3)
    test(last2('xaxaxaxx'), 0)
    test(last2('xxxx'), 2)
    test(last2('13121312'), 1)
    test(last2('11212'), 1)
    test(last2('13121311'), 0)
    test(last2('1717171'), 2)
    test(last2('hi'), 0)
    test(last2('h'), 0)
    test(last2(''), 0)

    print("\n")
    print('intersection')
    test(intersection('Eine kleine Nachtmusik', 'Nocturne in E minor'),
         [' ', 'E', 'N', 'c', 'e', 'i', 'm', 'n', 't', 'u'])
    test(intersection(range(0, 10), range(5, 15)), range(5, 10))


if __name__ == '__main__':
    main()
