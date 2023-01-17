def maxoftwo(a,b):
    if a>b :
        print("A is Max ")
    else:
        print("B is Max ")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print("A is Max")
        else:
            print("C is Max")
    else:
        if b>c:
            print("B is Max")
        else:
            print("C is Max")
        
def oddeven(a):
    if a%2==0:
        print("A is Even")
    else:
        print("A is Odd")

def primeno(a):
    if a>1:
        for i in range(2,int(a/2)+1):
            if (a%i)==0:
                print("A is not Prime number")
                break
            else:
                print("A is Prime Number")
                break
    else:
        print("A is not a Prime Number")

def feb_ser(a):
    x=0 
    y=1
    z=1
    if a==0 or a==1:
        print("A is Fibonacci Number")
    else:
        while x<a:
            x=y+z
            z=y
            y=x
        if x==a:
            print("A is Fibonacci No.")
        else:
            print("A is not Fibonacci No.")

        