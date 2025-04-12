print("Welcome to Password Strength Checker!")

# Input from user
password = input("Enter your password: ")

# Initial score
score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check for number
if (
    "0" in password or
    "1" in password or
    "2" in password or
    "3" in password or
    "4" in password or
    "5" in password or
    "6" in password or
    "7" in password or
    "8" in password or
    "9" in password
):
    score += 1

# Check for uppercase letter
if (
    "A" in password or
    "B" in password or
    "C" in password or
    "D" in password or
    "E" in password or
    "F" in password or
    "G" in password or
    "H" in password or
    "I" in password or
    "J" in password or
    "K" in password or
    "L" in password or
    "M" in password or
    "N" in password or
    "O" in password or
    "P" in password or
    "Q" in password or
    "R" in password or
    "S" in password or
    "T" in password or
    "U" in password or
    "V" in password or
    "W" in password or
    "X" in password or
    "Y" in password or
    "Z" in password
):
    score += 1

# Check for special character
if (
    "!" in password or
    "@" in password or
    "#" in password or
    "$" in password or
    "%" in password or
    "^" in password or
    "&" in password or
    "*" in password or
    "(" in password or
    ")" in password
):
    score += 1

# Match-case to print strength
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









