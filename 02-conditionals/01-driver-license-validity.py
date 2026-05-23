# ====== User Input ======
age = int(input("What's your age? "))

# License validity changes according to the driver's age
# Conditions are checked from highest age to lowest age

if age < 18:
    print("You are not old enough to drive!")
elif age < 50:
    print("Your driver's license validity is 10 years")
elif age < 70:
    print("Your driver's license validity is 5 years")
elif age < 116:
    print("Your driver's license validity is 3 years")
else:
    print("You broke a record! The oldest person currently is 116 years old! ")