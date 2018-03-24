# given a dictionary of the form {string1: float1, string2: float2 ... }
# print contents of the dictionary one per line, with the string
# right aligned in 20 characters, followed by a colon and a space, followed by
# the floating point number printed with two decimal precision

def precise_printing(dictionary):
 for key in dictionary:
  print('%20s:%0.2f' % (key, dictionary[key]))
  pass


# given a list of tuples of two integers each, print
#   num1 multiplied by num2 is num1*num2
# with the appropriate integers in place of a, b, and a*b
def multiply_printing(tuples):
  pass

# given a string, return a string with every number in the input
#   1) converted to float
#   2) divided by divisor
#   3) printed with four decimal precision
# for simplicity, you can assume there is no punctuation in the sentence
def divide_numbers(sentence, divisor):
  pass

# given two positive integers, x and y,
# generate a times table with x as the column, y as the row
# and x*y as the value
# compute the narrowest field width you can use to display the largest number
# and display all numbers in that field width, right aligned
# e.g. a times_table(5,4) looks like this:
#    1  2  3  4  5
# 1  1  2  3  4  5
# 2  2  4  6  8 10
# 3  3  6  9 12 15
# 4  4  8 12 16 20
def times_table(x,y):
  pass

def test(got, expected):
  if got == expected:
    prefix = '  OK '
  else:
    prefix = '   X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
  test_d = {'height': 6.54, 'weight': 124.6547, 'wingspan': 0.3645}
  print ('your precise_printing')
  precise_printing(test_d)

  print ("\n")
  print ('expected precise_printing')
  print ('            wingspan: 0.36')
  print ('              weight: 124.65')
  print ('              height: 6.54')

  print("\n")
  print ('your multiply printing')
  multiply_printing([(1,1), (2,4), (3,3), (4,6)])

  print("\n")
  print ('expected multiply printing')
  print ('1 multiplied by 1 is 1')
  print ('2 multiplied by 4 is 8')
  print ('3 multiplied by 3 is 9')
  print ('4 multiplied by 6 is 24')

  print("\n")
  print ('divide_numbers')
  test(divide_numbers('the 2000 year old statue was worth 4 million dollars', 3), 'the 666.6667 year old statue was worth 1.3333 million dollars')
  test(divide_numbers('58 engineers worked for 3 months on the project', 4), '14.5000 engineers worked for 0.7500 months on the project')

  print("\n")
  print ('your times_table')
  times_table(10,12)

  print("\n")
  print ('expected times_table')
  print ('      1   2   3   4   5   6   7   8   9  10')
  print ('  1   1   2   3   4   5   6   7   8   9  10')
  print ('  2   2   4   6   8  10  12  14  16  18  20')
  print ('  3   3   6   9  12  15  18  21  24  27  30')
  print ('  4   4   8  12  16  20  24  28  32  36  40')
  print ('  5   5  10  15  20  25  30  35  40  45  50')
  print ('  6   6  12  18  24  30  36  42  48  54  60')
  print ('  7   7  14  21  28  35  42  49  56  63  70')
  print ('  8   8  16  24  32  40  48  56  64  72  80')
  print ('  9   9  18  27  36  45  54  63  72  81  90')
  print (' 10  10  20  30  40  50  60  70  80  90 100')
  print (' 11  11  22  33  44  55  66  77  88  99 110')
  print (' 12  12  24  36  48  60  72  84  96 108 120')



if __name__ == '__main__':
  main()
