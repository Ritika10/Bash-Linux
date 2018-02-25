#! /usr/bin/python

for num in range(10,20):
    for i in range(2,num):
        if (num%i)==0:
            j=num/i
            print "%d * %d = %d" % (j,i,num)
            break;
    else:
        print "%d is a prime number" % num
