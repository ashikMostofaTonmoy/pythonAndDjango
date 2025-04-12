# Password Strength Checker
print("Welcome to Password Strength Checker!")

# Input from user (variable & data type: str)
password = input("Enter your password: ")

# Initial score
score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check for numbers
if any(char.isdigit() for char in password):
    score += 1

# Check for uppercase letters
if any(char.isupper() for char in password):
    score += 1

# Check for special characters
special_characters = "!@#$%^&*()-_+=<>?/"

if any(char in special_characters for char in password):
    score += 1

# Control Structure: match (Python 3.10+)
match score:
    case 4:
        print("Strength: Very Strong 🔥")
    case 3:
        print("Strength: Strong ✅")
    case 2:
        print("Strength: Medium ⚠️")
    case 1:
        print("Strength: Weak ❌")
    case _:
        print("Strength: Very Weak 🚫")

print("Thanks for using Password Strength Checker!")
