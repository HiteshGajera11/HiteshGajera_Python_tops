'''What is the purpose continue statement in python?
ANS : 
    The continue keyword is used to end the current iteration in a for loop (or a while loop), 
and continues to the next iteration.'''

for i in range(10):
  if i == 3:
    continue
  print(i)