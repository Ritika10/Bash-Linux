# Return True if the input n is positive (i.e. greater than 0)
# and False otherwise
def is_positive(n):
    return n>0

# Return True if a is larger than b and smaller than c
def between(a, b, c):
    return a>b and a<c


# Return True if a is within nearby of b
def close_enough(a, b, nearby):
    return abs(a-b)<=nearby


# The squirrels are playing if the temperature is between 60 and 90, inclusive
# Unless it is summer, in which case the upper limit is 100
# Return True if the squirrels are playing
def squirrels_playing(temperature, is_summer):
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
    print('is_positive')
    test(is_positive(0), False)
    test(is_positive(42), True)
    test(is_positive(-7), False)
    test(is_positive(1), True)

    print
    print('between')
    test(between(1, 2, 3), False)
    test(between(2, 1, 3), True)
    test(between(2, 2, 3), False)
    test(between(0, -1, 1), True)

    print
    print('close_enough')
    test(close_enough(1, 2, 3), True)
    test(close_enough(-5, 5, 10), True)
    test(close_enough(1, 10, 5), False)
    test(close_enough(42, 4, 21), False)

    print
    print('squirrels_playing')
    test(squirrels_playing(70, False), True)
    test(squirrels_playing(45, True), False)
    test(squirrels_playing(95, False), False)
    test(squirrels_playing(95, True), True)


if __name__ == '__main__':
    main()
