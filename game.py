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