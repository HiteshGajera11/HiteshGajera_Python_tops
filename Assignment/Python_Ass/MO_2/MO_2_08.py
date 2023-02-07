'''Write a Python program to test whether a passed letter is a vowel or
not. '''

def vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
    
print(vowel('c'))
print(vowel('e'))