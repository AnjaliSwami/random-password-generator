
'''****** PYTHON PROGRAM TO GENERATE RANDOM PASSWORDS******'''


import random
import array
import string

# length of password as an input from user in variable length

length = int(input('Enter the Length of the Password\n'))

password = ''

# Password consist of UpperCase and LowerCase Alphabet ,Digits or Special Symbols
# Characters is a array

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = [
    '#',
    '$',
    '@',
    '%',
    '=',
    '*',
    '?',
    '.',
    '/',
    '|',
    '~',
    '>',
    ':',
    '(',
    ')',
    '<',
    ]

# the character arrays is combination of all arrays

Characters = lowercase + uppercase + digits + symbols

# random module randomly select at least one character from each character set
# choice() in random module-- return random element from a sequence

temp_lower = random.choice(lowercase)
temp_upper = random.choice(uppercase)
temp_digit = random.choice(digits)
temp_symbol = random.choice(symbols)

# According to the rule password should atleast contain Uppercase, Lowercase , Digit and a Special symbol

compulsory = temp_digit + temp_upper + temp_lower + temp_symbol

# compulsory contain the atleast one char from all sets rest of length will be filled using for loop
# randomly choose characters from Characters array using random module

for x in range(length - 4):
    compulsory = compulsory + random.choice(Characters)

password = password + compulsory
print (password)
