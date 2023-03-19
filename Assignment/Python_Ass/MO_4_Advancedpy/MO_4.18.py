""" ==)How to Define a Class in Python? What Is Self? Give An Example Of 
A Python Class.

==> A class in Python can be defined using the class keyword. 
As per the syntax above, a class is defined using the class keyword 
followed by the class name and : operator after the class name, 
which allows you to continue in the next indented line to define class members
==> SELF represents the instance of class. This handy keyword allows 
you to access variables, attributes, and methods of a defined class in Python.
The self parameter doesn't have to be named “self,” as you can call it by any 
other name."""

class Person:
  def _init_(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()