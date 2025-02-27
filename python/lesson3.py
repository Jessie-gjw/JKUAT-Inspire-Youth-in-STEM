def greeting(user_name):
    return (f"Hello {user_name}")

print(greeting("John"))

#Calculate the area of a circle
#using the math module
import math

def circle_area(radius):
    return (math.pi * radius ** 2) #formula is pi*r^2
print(circle_area(5))

#Not using the math module
def circle_area(radius):
    return 3.142 * radius ** 2
print(circle_area(5))

def grade_score(score):
    if score >= 90:
        return "Qualifies for Grp A"
    elif score >= 80:
        return "Qualifies for Grp B"
    elif score >= 70:
        return "Qualifies for Grp C"
    elif score >= 60:
        return "Qualifies for Grp D"
    elif score >= 50:
        return "Qualifies for Grp E"
    else:
        return "You are religated"

score = int(input("Enter your game score: "))
print(grade_score(score))