# ====== User Input ======
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Executes the selected mathetical operation
match operation:

    case "+":
        print(f"{n1} + {n2} = {n1 + n2}")

    case "-":
        print(f"{n1} - {n2} = {n1 - n2}")

    case "*":
        print(f"{n1} * {n2} = {n1 * n2}")

    case "/":
        #Use .2f to display two decimal places
        print(f"{n1} / {n2} = {n1 / n2:.2f}")

    case _:
        print("Invalid operation. Please enter one of the following: (+, -, *, /)")