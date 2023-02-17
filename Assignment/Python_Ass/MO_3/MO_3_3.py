'''Write a Python function to get the largest number, smallest num and sum
of all from a list. '''

def max_num_in_list( list ):
    max = list[ 0 ]

    for a in list:
        if a > max:
            max = a
    return max

print(max_num_in_list([11, 5, 45, -2]))