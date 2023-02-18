'''Write a Python program to print all distinct values in a dictionary.'''


l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",l)
u_value = set( val for dic in l for val in dic.values())
print("Unique Values: ",u_value)