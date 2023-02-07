'''
try:
    a = int(input("Enter A :"))
    b = int(input("Enter B :"))

    div = a/b
    print("Div is : ",div)
except Exception:
    print("Exeception Caught")'''

while True:
    try:
        n = input("Enter Integer no only :")
        n = int(n)
        break
    except Exception:
        print("Invalid Input")
    finally:
        print("Finally Called")

print("Bye")
    