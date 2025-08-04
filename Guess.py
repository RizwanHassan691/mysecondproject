print("Guess the number between 1 and 100")

number = 42  # Fixed number
guess = int(input("Enter your guess: "))

if guess == number:
    print("You guessed right!")
elif guess < number:
    print("Too low!")
else:
    print("Too high!")
