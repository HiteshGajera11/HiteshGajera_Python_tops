"""
a =20
if a>0 :
    print(a," is Positive")
    


n = int(input("Enter N = "))
if n%2==0 :
    print(n," is Even")
else :
    print(n,"is odd")
    
n1 = int(input("Enter N1"))
n2 = int(input("Enter N2"))

if n1 > n2:
    print("N1 is Greater")
else:
    print("N2 is Greater")

n1=int(input("Enter N1 = "))
n2=int(input("Enter N2 = "))
n3=int(input("Enter N3 = "))

if n1>n2 :
    if n1>n3 :
        print("N1 is Greater")
    else:
        print("N3 is greater")
else :
    if n2>n3:
        print("N2 is Greater")
    else : 
        print("N3 Greater")
             
"""
roll=int(input("Enter Your Roll number = "))
name=input("Enter Your Name = ")
p=int(input("Enter Physics markes = "))
c=int(input("Enter chemistry markes = "))
m=int(input("Enter maths markes = "))
tot=p+c+m
per=tot/3
print("*"*50)

print("Roll num is = ",roll)
print("Name is = ",name)
print("Total markes is = ",tot)
print("Percentage is = ",per)
print("Grade is = ",end="")

if per>90 :
    print("Distinction")
elif per>75 :
    print("Grade A")
elif per>60 :
    print("Grade B")
elif per>40 :
    print("Fail")














