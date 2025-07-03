import random
import string


def password_generator():
    while True:
        pass_len = int(input("Enter the length of password u want: "))
        if pass_len > 6:
            character = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
            password = "".join(random.choice(character) for _ in range(pass_len))
            print(f"Your new and strong password is: ", password)
            break


def password_strength_checker():
    password = input("Enter Your Password: ")
    score = 0
    feedback = []
    # len check:
    if len(password) >= 8:
        score += 2
    elif len(password) > 6:
        score += 1
    else:
        feedback.append("Password should be at least 6 characters long ")
    # lowercase check:
    if  any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add Lowercase Letters")
    #uppercase check
    if  any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add Uppercase Letters")
    # digit check
    if  any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add Digits")
    # punctuation check
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Check for common patterns
    if password.lower() in ['password', '123456', 'qwerty', 'abc123']:
        score -= 2
        feedback.append("Avoid common passwords")

# Strength Value
    if score >= 5:
     strength = "strong"
    elif score >= 3:
     strength = "medium"
    else:
        strength = "weak"

    print(f"Password Strength: {strength} ")
    print(f"Score: {score}/6")

    if feedback:
        print("Suggesions: ")
        for suggestions in feedback:
            print(f"- {suggestions}")

try:
    choice = int(input("What do you want to do? \n"
                       "1.check Password \n"
                       "2.Generate Password: "))
    if choice == 1:
        password_strength_checker()
    else:
        password_generator()

except ValueError:
    print("Invalid Option")
