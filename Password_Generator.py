import random
import string
print("Welcome to the Password Generator: ")
n_letters = random.randint(0,9)
n_symbols = random.randint(0,9)
n_numbers = random.randint(0,9)
length = int(input("Enter the length of password : "))



# letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
#           'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G',
#           'H','I','J','K','L','M','N','O','P',
#           'Q','R','S','T','U','V','W','X','Y','Z']
letter = string.ascii_lowercase + string.ascii_lowercase
password=[]
symbol = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")



for i in range(0,n_letters):
        password.append(random.choice(letter))
for i in range(0,n_symbols):
    password.append(random.choice(symbol))
for i in range(0,n_numbers):
    password.append(random.randint(0,9))

random.shuffle(password)
print(password)
new_length = []

for i in password:
    if len(new_length)<length:
        new_length.append(i)
random.shuffle(new_length)

password = ""
for i in new_length:
    password += str(i)
    
print(password)