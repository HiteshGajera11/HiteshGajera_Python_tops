""" Write a Python program to append text to a file and display the text"""

file1 = open("myfile.txt", "w")

L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

file1 = open("myfile.txt", "a")  # append mode

file1.write("Today \n")
file1.close()
 

file1 = open("myfile.txt", "r")

print("Output of Readlines after appending")

print(file1.read())

print()
file1.close()


file1 = open("myfile.txt", "w")  # write mode

file1.write("Tomorrow \n")
file1.close()
 

file1 = open("myfile.txt", "r")

print("Output of Readlines after writing")

print(file1.read())

print()
file1.close()