#Password generator
#This code generates a random password of length 16 using letters, digits, and punctuation.

import random
import string

total = string.ascii_letters + string.digits + string.punctuation   

length = 16 #length of the password

password = "".join(random.sample(total, length))    # Generate a random password by sampling characters from the total set

print(password) # Print the generated password