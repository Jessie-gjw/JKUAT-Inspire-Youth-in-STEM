# Variables in Python
student_name = "John" #String
student_second_name = 'Doe' #String
student_age = 20 #Integer
student_height = 5.5 #Float
student_admitted = True #Boolean

#Operators in Python
#1. Arithmetic Operators
num1 = 10
num2 = 20
addition = num1 + num2
#print(addition)
subtraction = num1 - num2
#print(subtraction)

#2. Comparison Operators
#Equal to
#print(num1 == num2)#False
#Greater than
#print(num1 > num2)#False
#Not equal to
#print(num1 != num2)#True
#Less than
#print(num1 < num2)#True

#3. Logical Operators
#and, or, not
#print(num1 < num2 and num1 > num2)#False
#print(num1 > num2 or num1 < num2)#True
#print(not num1 < num2)#True

#4. Assignment Operators
# =, +=, -=, *=, /=, %=, //=, **=
#num1 += 5
#print(num1) #15
#num1 -= 5
#print(num1) #20
#num1 *= 5
#print(num1) #100

#5. Identity Operators
#is, is not
#print(num1 is not num2)#False
#print(num1 is num2)#False

#6. Conditional Statements
#If, elif, else

if student_age >= 18:
    print("You are an adult")

enter_name = input("Enter your name: ")
enter_age = int(input("Enter your age: ")) 
if enter_age >= 18:
    print(enter_name, "are an adult") 
else:
    print(enter_name, "are a minor")
    
