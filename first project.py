import random

secret = random.randint(1, 10)
attempts = 5

while attempts > 0:
    guess = int (input(f"GUESS THE NUMBER (1-10) | Attempts left {attempts}:"))

    if guess == secret:
        print ("You guessed it right!🎉")
        print("Your score:", attempts * 10)

        break
    elif guess < secret:
        print ("Too low!")
    else:
        print ("Too high!")

    attempts -= 1

if attempts == 0:
    print("Game Over 💀 The number was:", secret)


print("SECRET NUMBER IS:", secret)