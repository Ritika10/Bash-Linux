print("Hello world")


## Brian Miller's during Python Class
REFRAIN='''%d bottles of beer on the wall, 
            %d bottles of beer,
            take one down, pass it around,
            %d bottles of beer on the wall!
            '''

bottles =3
while bottles > 1:
    print(REFRAIN % (bottles, bottles, bottles - 1))
    bottles -=1


tabby_cat = "\t I'm tabbed in"
persian_cat = "I'm split \non a tail"
print(tabby_cat)
print(persian_cat)

a='positive'
if a=='positive':
    print(1)
elif a=='negative':
    print(-1)
else:
    print(0)