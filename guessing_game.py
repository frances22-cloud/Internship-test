import random

secret_number = random.randint(1, 10)
tries = 3

print("I'm thinking of a number between 1 and 10.")
print(f"You have {tries} tries.\n")

while tries > 0:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    if guess < 1 or guess > 10:
        print("Please guess a number between 1 and 10.")
        continue
    
    tries -= 1
    
    if guess == secret_number:
        print("Congratulations! You won!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    if tries > 0:
        print(f"You have {tries} {'try' if tries == 1 else 'tries'} left.\n")
    else:
        print(f"Game over! The number was {secret_number}.")
