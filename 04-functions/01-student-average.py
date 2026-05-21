def calculate_average(sum_grades):
    average = sum_grades / (i+1)
    return average

def above_below_average(average_result):
    if average_result == 0:
        print("Oh no! The student got a zero on average!")
    elif average_result > 7:
        print("The student passed the year!")
    else:
        print("The student will need to do the retake test!")
    

grades = []

i = int(input("Enter the amount of activies: "))


for i in range(i):
    grade = float(input("Enter the grade: "))
    if grade >= 0:
        grades.append(grade)
    else:
        print("Invalid grade. Try again.")
        i = 0
        break
    #print(i)

# Debug
#print(grades)
# print(sum(grades))

if i != 0:
    sum_grades = sum(grades)
    average_result = calculate_average(sum_grades)
    
    print(f"Student average: {average_result:.2f}")
    above_below_average(average_result)