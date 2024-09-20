#***************************************
# Lab Assignment No.1: ENCRYPTION      *
# Programmed by: Mariella H. Calderon  *
# Course, Year and Section: BSCPE 1-3  *
# Instructor: Engr. Julius S. Cansino  *
# Date Submitted: March 9, 2024        *
#***************************************

import string

chars = string.ascii_lowercase + string.punctuation + string.digits + string.ascii_uppercase
chars = list(chars)

# Create a translation table for the specific character substitutions
translation_table = str.maketrans({
   'a': '*', 'e': '&', 'i': '#', 'o': '+', 'u': '!'
})

# Encrypt function using string manipulation and translation table
def encrypt(plain_text):
   return plain_text.translate(translation_table)

# Get user input
plain_text = input("Enter a message to encrypt: ")

# Encrypt the message
cipher_text = encrypt(plain_text)
print(f"Encrypted message: {cipher_text}")