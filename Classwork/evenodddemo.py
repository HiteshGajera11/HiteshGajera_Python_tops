import random

data = open("data.txt","w")
for i in range(10):
    num = random.randint(1, 999)
    data.write(str(num)+" ")
data.close()

data = open("data.txt","r")
even = open("even.txt","w")
odd = open("odd.txt","w")
s = data.read().split(" ")[:-1]
print(s)
#print(type(s))

for i in s :
    #print(type(int(i)))
    if int(i)%2==0 :
        even.write(i+" ")
    else :
        odd.write(i+" ")

data.close()
even.close()
odd.close()

print("*"*100)

data = open("data.txt","r")
print("this is data file content")
print(data.read())
data.close()
print("*"*100)

even = open("even.txt","r")
print("this is even file content")
print(even.read())
even.close()
print("*"*100)

odd = open("odd.txt","r")
print("this is odd file content")
print(odd.read())
odd.close()

