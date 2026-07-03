"""
Daniel's Dog Clinic
---------------------purpose------------------
Daniel Shiloh
July 3, 2026
"""

#TO DO list:
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

def choice_register_human(clinic):
    """handles process of registering a new human (option 1)"""

    print("\n--New Human Registration--")

    name_as_is = get_non_empty_input("Human's full name: ")
    name = get_clean_name(name_as_is)

    phone_as_is = get_non_empty_input("Phone number: ")
    phone = get_clean_phone(phone_as_is)

    potential_id = clinic.register_human(name, phone)
    if potential_id:
        print(f"\nYour new ID is {potential_id}.")
    else:
        print("\nThat name/number is already in our system.")

def choice_register_dog(clinic):
    """handles process of regstering a new dog (option 2)"""
    
    print("\n--New Dog Registration--")

    human_id = get_clean_name(input("Enter human id (eg H-1): "))
    if human_id not in clinic.humans:
        print("\nHuman ID not found.  Please register the human.")
        return

    name_as_is = get_non_empty_input("Dog's name: ")
    name = get_clean_name(name_as_is)

    breed_as_is = get_non_empty_input("Breed: ")
    breed = get_clean_name(breed_as_is)
    
    while True:
        sex_as_is = get_non_empty_input("Sex (m/f): ")
        if validate_sex(sex_as_is):
            sex = get_clean_name(sex_as_is)
            break
        print("\nPlease enter M or F.")
    
    while True:
        dob_as_is = get_non_empty_input("Estimated date of birth (YYYY-MM-DD): ")
        if validate_dob(dob_as_is):
            dob = get_clean_name(dob_as_is)
            break
        print("\nInvalid date.  Please use YYYY-MM-DD (eg 2026-01-30).")

    potential_id = clinic.register_dog(name, breed, sex, dob, human_id)
    print(f"\n{name.title()}'s ID is {potential_id}.")

def choice_search_human(clinic):
    """handles process of searching and displaying human records (option 3)
    search by human_id or display all registered humans"""
    
    print("\n--Human Search--")
    
    search_input = get_clean_name(input("Enter human ID (eg H-1) or ALL: "))
    
    if search_input == "ALL":
        if not clinic.humans:
            print("\nNo humans registered yet.")
            return
        print("\n--All Registered Humans--")
        for human in clinic.humans.values():
            print(f"ID: {human.id}, name: {human.name}, phone: {human.phone}")

    elif search_input in clinic.humans:
        human = clinic.humans[search_input]
        print(f"\nHuman Found: {human.id}")
        print(f"  Name: {human.name}")
        print(f"  Phone: {human.phone}")

    else:
        print("\nNo human found with that ID.")

def choice_search_dog(clinic):
    """handles process of searching and displaying dog records (option 4)
    search by dog_id or display all registered dogs"""
    
    print("\n--Dog Search--")
    
    search_input = get_clean_name(input("Enter dog ID (eg D-1) or ALL: "))
    
    if search_input == "ALL":
        if not clinic.dogs:
            print("\nNo dogs registered yet.")
            return
        print("\n--All Registered Dogs--")
        for dog in clinic.dogs.values():
            human = clinic.humans.get(dog.human_id)
            print(f"ID: {dog.id}, name: {dog.name}, breed: {dog.breed}, human: {human.name}")

    elif search_input in clinic.dogs:
        dog = clinic.dogs[search_input]
        human = clinic.humans[dog.human_id]
        print(f"\nDog Found: {dog.id}")
        print(f"  Name: {dog.name}")
        print(f"  Breed: {dog.breed}")
        print(f"  Sex: {dog.sex}")
        print(f"  Date of birth (est): {dog.dob}")
        print(f"  Human: {human.name} (ID: {human.id}), {human.phone}")
    
    else:
        print("\nNo dog found with that ID.")


def main():
    """manage user interaction, adding to and searching in registry"""

    clinic = Registration()

    print_header()

    while True:

        print_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            choice_register_human(clinic)
        elif choice == '2':
            choice_register_dog(clinic)
        elif choice == '3':
            choice_search_human(clinic)        
        elif choice == '4':
            choice_search_dog(clinic)
        elif choice == '5':
            print("\nExiting application.")
            break
        else:
            print("\nInvalid choice.  Please pick options 1 through 5.")

if __name__ == "__main__":
    main()