from random import randint

# Generates a random number between 1 and 100
random_number = randint(1, 100)

# Debug
#print(random_number)

# Keeps running until the user guesses correctly
while True:

    user_input = int(input("Enter a number: "))

    # Checks if the guess is too high
    if random_number < user_input:
        print("Your guess is too high. Try again!")
        continue

    # Checks if the guess is too low
    elif random_number > user_input:
        print("Your guess is too low. Try again!")
        continue

    # Runs when the user guesses correctly
    else:
        print("Your guess is right!")
        break

# Displays the final result
print(f"Random number: {random_number}")
print(f"User guess: {user_input}")