'''Write python program that swap two number with temp variable and
without temp variable. '''

#without using temt
a = 30
b = 20
print("\nBefore swap A = ",a,",B = ",b)
a, b = b, a
print("\nAfter swaping A = ",a,", B = ",b)

#Using Temt

x = 34
y = 56
print("Before swap of x =", x,",Y = ",y)
temp = x
x = y
y = temp
print("\nAfter swaping value of x =", x,",Y = ",y)
