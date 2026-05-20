# ====== Input ======
n1 = int(input("What's the first number? "))
n2 = int(input("What's the second number? "))

# ====== Processing ======
sum_result = n1 + n2
minus_result = n1 - n2
multiply_result = n1 * n2
divide_result = n1 / n2

# ====== Output ======
print(f"{n1} + {n2} = {sum_result}")
print(f"{n1} - {n2} = {minus_result}")
print(f"{n1} * {n2} = {multiply_result}")

#Using .2f to always show two decimal places
print(f"{n1} / {n2} = {divide_result:.2f}")