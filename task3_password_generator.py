# Task 2: Password Generator
# CODSOFT Internship
# Author: Siva Saravanan A

import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
