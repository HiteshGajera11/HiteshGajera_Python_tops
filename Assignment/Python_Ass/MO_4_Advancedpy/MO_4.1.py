"""
==> What is File function in python?What is keywords to create and write
file

    Python file object provides methods and attributes to access and manipulate files.
Using file objects, we can read or write any files. Whenever we open a file to perform any operations on it, Python returns a file object.
To create a file object in Python use the built-in functions, such as open() and os. popen() """

f = open("demofile.txt", "a")
f.write("Hello World")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())