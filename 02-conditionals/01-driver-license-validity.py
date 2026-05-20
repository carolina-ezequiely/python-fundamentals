# ====== User Input ======
age = int(input("What's your age? "))

# License validity changes according to the driver's age
# Conditions are checked from highest age to lowest age

if age >= 116:
    print("You broke a record! The oldest person currently is 116 years old! ")
elif age >= 70:
    print("Your driver's license validity is 3 years")
elif age >= 50:
    print("Your driver's license validity is 5 years")
elif age >= 18:
    print("Your driver's license validity is 10 years")
else:
    print("You are not old enough to drive!")