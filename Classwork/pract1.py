l = []

for i in range(3333,4001):
    s = str(i)
    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
        l.append(i)

print(l)
