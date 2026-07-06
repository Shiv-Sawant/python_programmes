import string
import random

def generate_password(min_length,numbers=True,special_chars=True):
    letters = string.ascii_letters
    if numbers:
        letters += string.digits
    if special_chars:
        letters += string.punctuation

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(letters)
        pwd += new_char
        
        if new_char in string.digits:
            has_number = True
        elif new_char in string.punctuation:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special
            
    return pwd


min_length = int(input("Enter the minimum length of the password: "))
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

print(generate_password(min_length, include_numbers, include_special))
