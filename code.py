import random
import string

print("hello, welcome to Nolly.co password generator!")
length = int(input("Enter the length of password you desire:"))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all, length)

password = "".join(temp)
print(password)