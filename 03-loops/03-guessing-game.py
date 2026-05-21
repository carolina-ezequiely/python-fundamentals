from random import randint

random_number = randint(1, 100)

# Debug
#print(random_number)

# Keeps running until the user guesses correctly
while True:

    user_input = int(input("Enter a number: "))

    if random_number < user_input:
        print("Your guess is too high. Try again!")
        continue

    elif random_number > user_input:
        print("Your guess is too low. Try again!")
        continue

    else:
        print("Your guess is right!")
        break

print(f"Random number: {random_number}")
print(f"User guess: {user_input}")
