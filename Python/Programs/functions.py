# return the Nth number in the Fibonacci sequence
# the zeroth number in the sequence is 0
# the first number in the sequence is 1
# subsequent numbers in the sequence are defined by the formula:
#   F_n = F_(n-1) + F(n-2)
# for example, F_2 === F_1 + F_0 === 1 + 0 === 1
def fibonacci(n):
    l = [0,1]
    i=2
    while(i<n-1):
        l[i]=l[i-1]+l[i-2]
        i +=1
    return l[n-1]
    pass


# given a non-negative integer N, write a recursive function
# that sums the digits of N and returns the result
# for example, the sum_digits(1234) == 10
def sum_digits(n):
    pass


# given a sequence, return the list of all elements
# after the first in the sequence that is larger than the first
def bigger_than_first(xs):
    pass


# given a list of sequences, return a list of the sizes of those
# input sequence in order from smallest to largest
def ordered_lengths(xs):
    pass


def test(got, expected):
    if got == expected:
        prefix = '  OK '
    else:
        prefix = '   X '
    print
    '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    print ('fibonacci')
    test(fibonacci(0), 0)
    test(fibonacci(1), 1)
    test(fibonacci(2), 1)
    test(fibonacci(3), 2)
    test(fibonacci(4), 3)
    test(fibonacci(5), 5)
    test(fibonacci(20), 6765)

    print("\n")
    print('sum_digits')
    test(sum_digits(1234), 10)
    test(sum_digits(0), 0)
    test(sum_digits(77), 14)
    test(sum_digits(1010101), 4)

    print("\n")
    print('bigger_than_first')
    test(bigger_than_first([1, 2, 3, 4]), [2, 3, 4])
    test(bigger_than_first([7, 3, 9, 5]), [9])
    test(bigger_than_first([42, 64, 31, 7, 101]), [64, 101])
    test(bigger_than_first([1000, 100, 10, 1]), [])

    print("\n")
    print('ordered_lengths')
    test(ordered_lengths(['the', 'lazy', 'dog']), [3, 3, 4])
    test(ordered_lengths(['a', 'terrible', 'fate']), [1, 4, 8])
    test(ordered_lengths('elephant trunks and giraffe necks'.split()), [3, 5, 6, 7, 8])


if __name__ == '__main__':
    main()
