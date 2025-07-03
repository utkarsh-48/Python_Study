import random

secret = random.randint(1,3)
print("Welcome to number guessing game-> ")
print("You have three attempts to win")
for guesses in range(1,4):
    guess = int(input("Attempt {}, Enter Your Guess: ".format(guesses)))
    if guess == secret:
        print(f"Yay! You Won in {guesses} tries")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")
else:
    print("Lol, Loser. Get Good")
