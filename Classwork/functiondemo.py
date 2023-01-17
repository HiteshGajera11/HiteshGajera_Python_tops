"""
def printline() :
    print("*"*50)

printline()
print("Welcome to python programming")
printline()

def printstar() :
    print("*"*80)

def add():
    a = int(input("Enter A = "))
    b = int(input("Enter B = "))
    print("Befor Swapping A = ",a,"B = ",b)
    a,b = b,a
    print("After Swapping A = ",a,"B = ",b)
    print("Addition is = ",(a+b))
printstar()
add()
printstar()


def printstar():
    print("*"*80)

def add(a,b):
    print("A = ",a,"B = ",b)
    print("Addition is ",(a+b))

n1 = int(input("Enter N1 = "))
n2 = int(input("Enter N2 = "))
printstar()
add(n1,n2)
printstar()
"""

def printstar():
    print("*"*80)

def add(a,b):
    print("A is = ",a)
    print("B is = ",b)
    printstar()
    return a+b
def evenodd(n):
    print("Value is n = ",n)
    if n%2==0:
        print("Addition is Even no")
    else:
        print("Addition is Odd no")

n1 = int(input("Enter A  = "))
n2 = int(input("Enter B  = "))

num = add(n1,n2)
print("Addition is = ",num)
evenodd(num)
















