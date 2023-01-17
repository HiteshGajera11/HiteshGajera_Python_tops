import practice_1701

def printstar():
    print("*"*80)

while True:
    printstar()
    print("Enter 1. For Find The Maximum of Two numbers.")
    print("Enter 2. For Find The Maximum of Three numbers.")
    print("Enter 3. For Find The Given Number is Even or Odd.")
    print("Enter 4. For Find The Given Number is Prime no or not.")
    print("Enter 5. For Find The Given Number is Fibonacci no or not.")
    print("Enter 6 For Exit.")
    printstar()
    print("Please Enter your Choice")

    choice = int(input("Enter Your Choice."))

    if choice==1:
        a = int(input("Enter A : "))
        b = int(input("Enter B : "))
        practice_1701.maxoftwo(a, b)
    elif choice==2:
        a = int(input("Enter A : "))
        b = int(input("Enter B : "))
        c = int(input("Enter C : "))
        practice_1701.maxofthree(a, b, c)
    elif choice==3:
        a = int(input("Enter A :"))
        practice_1701.oddeven(a)
    elif choice==4:
        a = int(input("Enter A :"))
        practice_1701.primeno(a)
    elif choice==5:
        a = int(input("Enter A : "))
        practice_1701.feb_ser(a)
    else:
        break






