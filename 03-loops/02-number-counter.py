for i in range(1, 101, 1):

    # Multiple of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    # Multiplies of 3
    elif i % 3 == 0:
        print("Fizz")

    # Multiplies of 5
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
