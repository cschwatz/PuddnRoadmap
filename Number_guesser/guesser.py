import random

numToGuess = random.randrange(1,10)
numGuesses = 5

while numGuesses >= 0:
    guess = int(input("Please, type in you guess from 1 to 10: "))
    
    if guess == numToGuess:
        print("Congratulations, you have guessed right!")
        break
    elif guess > 10 or guess < 0:
        print("The input number should be between 1 and 10")
        continue
    else:
        print(f"That is not the correct number, you have {numGuesses} left.")
    numGuesses -= 1