"""
l = []

for i in range(3333,3999):
    #print(type(i))
    s = str(i)
    if int(s[0])%2!=0 and int(s[1])%2!=0 and int(s[2])%2!=0 and int(s[3])%2!=0:
        l.append(i)

print(l)

data = open("data.txt","w")
data.write(str(l))
data.close()
"""
l = []
for i in range(2000,3001):
    if i%2==0:
        l.append(i)
        print(l)
    else:
        l.append(i)
        print(l)
  
    

