'''Write a Python program to get the Fibonacci series of given range.'''


n = int(input("Enter Value : "))

x,y=0,1

while y<n:
    print(y)
    x,y = y,x+y


