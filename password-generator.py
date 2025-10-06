import random, string, pyperclip

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))

# to copy password to clipboard
pyperclip.copy(password)
print("Password copied to clipboard!")

print("Generated password:", password)