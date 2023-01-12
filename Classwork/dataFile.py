"""
s="Write demo"
print(s)
print("*"*50)

file = open("tops.txt","w")
file.write("This is write demo...")
print("File writing successfull")
file.close()

s="read demo"
print(s)
print("*"*50)

file = open("tops.txt","r")
print(file.read())
file.close()
"""
s = "Append demo"
print(s)
print("*"*50)

file = open("tops.txt","a")
file.write("This is append data...")
file = open("tops.txt","r")
print(file.read())
file.close()




