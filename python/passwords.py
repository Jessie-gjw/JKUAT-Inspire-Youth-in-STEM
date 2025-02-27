import hashlib
import os

FILENAME = "passwords.txt"

#function to hash/encrypt a password
def hash_password(password):
    """Hash / Encrypt a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

#function to save the password
def save_password(site, password):
    hashed_password = hash_password(password)
    with open(FILENAME, "a") as file:
        file.write(f"{site} {hashed_password}\n")
    print(f"Password for the site {site} saved successfully")

#function to get the password
def get_password(site):
    if not os.path.exists(FILENAME):
        print("No passwords saved yet")
        return
    with open(FILENAME, "r") as f:
        for line in f: #f meaning file
            stored_site, stored_password = line.strip().split(" ")
            if site == stored_site:
                return stored_password
    print(f"No password saved for {site}")        
    return None

#function to check if a site exists
def site_exists(site):
    if not os.path.exists(FILENAME):
        return False
    with open(FILENAME, "r") as f:
        for line in f:
            stored_site, stored_password = line.strip().split(" ")
            if site == stored_site:
                return True
    return False

def main():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            pass #create the file if it does not exist

    action = input("Enter 'save' to save a password or 'get' to retrieve a password: ")

    if action == "save":
        site = input("Enter the site: ")
        if site_exists(site):
            print("Site already exists")
            overwrite = input("Do you want to update the password? (yes/no): ")
            if overwrite != "yes":
                print ("Password not updated")
                return
        import string
        import random

#Generate random password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(characters, k=10))
        print(f"Generated password: {password}")
        save_password(site, password)
    elif action == "get":
        site = input("Enter the site name: ")
        password = get_password(site)
        if password:
            print(f"Password for {site} is {password}")

    else:
        print("Invalid action")
    
if __name__ == "__main__":
    main()