count = 0

while count<9:
    print(count)
    count += 1

#Using user input

password = input("Enter your password: ")

user_input = ""
while user_input != password:
    user_input = input("Enter your password again: ")

print("Access granted")