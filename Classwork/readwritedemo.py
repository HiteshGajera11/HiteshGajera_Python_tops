s = "ReadWrite demo"
print(s)
print("*"*50)

file = open("tops2.txt","w+")
file.write("Now this is ReadWrite demo...")
print("Current file cursor positon",file.tell())
file.seek(10)
print(file.read())
file.close()