#! /usr/bin/python

str1 = "Hello World"

print "str1 is " + str1

commands = [
    "str1.capitalize()",
    "str1.upper()"
    ]

for i in commands:
    print i + " : " + eval(i)


# print r'c:\\nowhere'
# print "Updating the last characters", str[:6] + 'Python'
