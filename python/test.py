import os

# Define the filename
filename = 'passwords.txt'

# Initialize an empty dictionary to store the data
data_dict = {}

# Open the file and read its contents
with open(filename, 'r') as file:
    for line in file:
        # Split each line into key and value
        key, value = line.split()
        # Store them in the dictionary
        data_dict[key] = value

# Prompt the user for input
user_input = input("Enter the key: ")

# Search for the user input in the dictionary
if user_input in data_dict:
    print(data_dict[user_input])
else:
    print("Nothing found")