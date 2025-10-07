import random, string, pyperclip

# Ask if user wants advanced settings
choice = input("Do you want to customize password requirements? (yes/no): ").strip().lower()
length = int(input("Enter password length: "))
if choice == "yes":
    min_upper = int(input("Min uppercase letters: "))
    min_lower = int(input("Min lowercase letters: "))
    min_digits = int(input("Min digits: "))
    min_symbols = int(input("Min symbols: "))

    symbols = "!@#$%^&*"
    password_chars = []

    password_chars += random.choices(string.ascii_uppercase, k=min_upper)
    password_chars += random.choices(string.ascii_lowercase, k=min_lower)
    password_chars += random.choices(string.digits, k=min_digits)
    password_chars += random.choices(symbols, k=min_symbols)

    remaining = length - len(password_chars)
    all_chars = string.ascii_letters + string.digits + symbols
    password_chars += random.choices(all_chars, k=remaining)

    random.shuffle(password_chars)
    password = ''.join(password_chars)
    
else:
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

# to copy password to clipboard
pyperclip.copy(password)
print("Password copied to clipboard!")

print("Generated password:", password)