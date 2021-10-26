import random 

"""A number-guessing game."""



# Put your code here
# greet player
# get player name
# choose random number between 1 and 100
# repeat forever:
#     get guess
#     if guess is incorrect:
#         give hint
#         increase number of guesses
#     else:
#         congratulate player


print("Welcome to the guessing number game.")
player = input("What is your name?  ").upper()
print(f"Great {player}, let's get started!")

answer = random.randint(1, 100)
num_guesses = 1

while True:
    guess = input("Guess a number between 1 and 100: ")

    try:
        guess = int(guess)
    except:
        print("please guess numbers only.")
        continue



    if  guess < 1 or guess > 100:
        print("please guess between 1 and 100.")
        continue

    elif guess == answer: 
        print("That's correct.")
        break

    elif guess > answer: 
        print("Too high, guess again!")

    elif guess < answer:
        print("Too low, guess again!")

    num_guesses += 1

print(f"{player}, you got the answer in {num_guesses} guess(es)!")

    