"""
Daniel's Dog Clinic
---------------------purpose------------------
Daniel Shiloh
July 3, 2026
"""

#TO DO list:
# main: validate inputs, add try/except, refactor
# test: all test cases

import string
from registration import Registration
from datetime import datetime

def print_header():
    """prints at top of output"""
    print("-" * 40)
    print("    Daniel's Dog Clinic: Registration    ")
    print("-" * 40)

def print_menu():
    """prints options for initial user input"""
    print("\nMenu:")
    print("1. Register new human")
    print("2. Register new dog (requires Human ID)")
    print("3. Search registered humans")
    print("4. Search registered dogs")
    print("5. Exit")

def get_clean_name(name: str):
    """format user input consistently; use before storing value"""
    return name.strip().upper()
    
def get_clean_phone(phone: str):
    """format user input consistently; use before storing value"""
    clean_phone = ""
    for char in phone:
        if char in string.digits:
            clean_phone += char
    return clean_phone

def get_non_empty_input(prompt):
    """repeat prompt until user's response isn't blank"""
    while True:
        user_input = input(prompt)
        if user_input != "":
            return user_input
        print("\nThis field cannot be left blank.  Please try again.")

def validate_sex(sex_str):
    """check if user-inputted sex matches reasonable options"""
    if sex_str.upper() in ['M', 'F', 'MALE', 'FEMALE', 'BOY', 'GIRL']:
        return True
    return False

def validate_dob(date_str):
    """check if user-inputted date of birth is a valid yyyy-mm-dd date"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    """manage user interaction, adding to and searching in registry"""

    clinic = Registration()

    print_header()

    while True:
        
        print_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            print("\n--New Human Registration--")
            name = get_clean_name(input("Human's name: "))
            phone = get_clean_phone(input("Phone number: "))
            potential_id = clinic.register_human(name, phone)
            if potential_id:
                print(f"\nYour new ID is {potential_id}.")
            else:
                print("\nThat name/number is already in our system.")
    
        elif choice == '2':
            print("\n--New Dog Registration--")

            human_id = get_clean_name(input("Enter human id (eg H-1): "))
            if human_id in clinic.humans:
                print("Human ID not found.  Please register the human.")


            #TO DO: validate these inputs
            name = get_clean_name(input("Dog's name: "))
            breed = input("Breed: ")
            sex = input("Sex (m/f): ")
            dob = input("Estimated date of birth (YYYY-MM-DD): ")
            potential_id = clinic.register_dog(name, breed, sex, dob, human_id)
            print(f"\n{name.title()}'s ID is {potential_id}.")

        elif choice == '3':
            print("\n--Human Search--")
            human_id = get_clean_name(input("Enter human ID (eg H-1): "))
            if human_id in clinic.humans:
                human = clinic.humans[human_id]
                print(f"\nHuman Found: {human.id}")
                print(f"  Name: {human.name}")
                print(f"  Phone: {human.phone}")
            else:
                print("\nNo human found with that ID.")
        
        elif choice == '4':
            print("\n--Dog Search--")
            dog_id = get_clean_name(input("Enter dog ID (eg D-1): "))
            if dog_id in clinic.dogs:
                dog = clinic.dogs[dog_id]
                human = clinic.humans[dog.human_id]
                print(f"\nDog Found: {dog.id}")
                print(f"  Name: {dog.name}")
                print(f"  Breed: {dog.breed}")
                print(f"  Sex: {dog.sex}")
                print(f"  Date of birth (est): {dog.dob}")
                print(f"  Human: {human.name} (ID: {human.id}), {human.phone})")
            else:
                print("\nNo dog found with that ID.")

        elif choice == '5':
            print("\nExisting application.")
            break

        else:
            print("\nInvalid choice.  Please pick options 1 through 5.")

if __name__ == "__main__":
    main()    