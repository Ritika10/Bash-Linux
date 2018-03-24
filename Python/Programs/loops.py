# given a non-empty string, return a string of
# all substrings of that string that start with the first letter,
# in order of length of substring.
# Example: 'Code' -> 'CCoCodCode'
def string_splosion(s):
    str=""
    str1=""
    for letter in s:
        str=str+letter
        str1=str1+str
    return str1


# given an list of integers, return the number of 9s found in the list
def count9(nums):
    count=0
    for num in nums:
        if num==9:
            count +=1
    return count


# given an integer, return it if it is odd
# otherwise divide it by 2 until the result is odd
# and then return that result
# RA => Should not be 3.0
def first_odd(num):
    while num%2==0:
        num = num / 2
    return num


# given a positive integer, return True if it is a prime number
# (divisible only by 1 and itself)
# and False otherwise
def is_prime(num):
    for i in range(2,num):
        if num%i == 0 :
            return False
    return True


def test(got, expected):
    if got == expected:
        prefix = '  OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('string_splosion')
    test(string_splosion('Bad'), 'BBaBad')
    test(string_splosion('Code'), 'CCoCodCode')
    test(string_splosion('abcde'), 'aababcabcdabcde')
    test(string_splosion('Kitten'), 'KKiKitKittKitteKitten')

    print("\n")
    print( 'count9')
    test(count9([1, 2, 9]), 1)
    test(count9([1, 9, 9]), 2)
    test(count9([1, 9, 9, 3, 9]), 3)
    test(count9([1, 2, 3]), 0)
    test(count9([]), 0)
    test(count9([4, 2, 4, 3, 1]), 0)
    test(count9([9, 2, 4, 3, 1]), 1)

    print("\n")
    print('first_odd')
    test(first_odd(2), 1)
    test(first_odd(17), 17)
    test(first_odd(24), 3)
    test(first_odd(30), 15)
    test(first_odd(42), 21)
    test(first_odd(64), 1)

    print("\n")
    print('is_prime')
    test(is_prime(7), True)
    test(is_prime(10), False)
    test(is_prime(13), True)
    test(is_prime(21), False)


if __name__ == '__main__':
    main()
