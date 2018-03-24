import hashlib


# given a filename, read all lines of the file,
# extract the last non-whitespace character of each line
# and concatenate them together into a string
def last_character(filename):
    str=[]
    with open(filename) as f:
        for line in f:
            str.append(line[-2])
    return ''.join(str)
    pass


# given a list of filenames, open each one in order
# and return its contents in a list
def cat(*filenames):
    pass


# given an input file, infile, and an output file, outfile,
# write the contents of infile to outfile
def cp(infile, outfile):
    pass


# give two input files, a and b,
# read each line in order
# if they are different, print
# < aline
# > bline
def diff(a, b):
    pass


def md5sum(fn):
    with open(fn) as f:
        return hashlib.md5(f.read()).hexdigest()


def test(got, expected):
    if got == expected:
        prefix = '  OK '
    else:
        prefix = '   X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('last_character')
    test(last_character('lastchar1.txt'), 'eknxdreyg')
    test(last_character('lastchar2.txt'), ',,.,...')

    print("\n")
    print('cat')
    test(cat('cat1.txt', 'cat2.txt', 'cat3.txt'), [['the quick brown\n'], ['fox jumped over\n'], ['the lazy dog\n']])

    print("\n")
    print('cp')
    cp('lastchar2.txt', 'lastchar2_copy.txt')
    try:
        test(md5sum('lastchar2_copy.txt'), md5sum('lastchar2.txt'))
    except IOError as e:
        print
        "IO error: " + str(e)

    print("\n")
    print("your diff('diffa.txt', 'diffb.txt')")
    diff('diffa.txt', 'diffb.txt')

    print("\n")
    print("expected diff('diffa.txt', 'diffb.txt')")
    print('< Ut enim ad minim veniam,')
    print('> Ut enim ad maxim veniam,')
    print('< Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')
    print('> Duis aute calore dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')


if __name__ == '__main__':
    main()
