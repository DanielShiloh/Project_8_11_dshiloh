"""
Daniel's Dog Clinic
---------------------purpose------------------
Daniel Shiloh
July 3, 2026
"""

##generally to do: add try/except, actually read/write to file w json

from pathlib import Path
import string
import json

class Human:
    """represents dog owner"""

    def __init__(self, human_id: str, name: str, phone: str):
        """create owner with given info"""
        self.id = human_id
        self.name = name
        self.phone = phone
        
    #def to_dict
        """convert human data to dict, for json"""

    #def from_dict
        """create Human instance from dict"""

class Dog:
    """represents single patient"""

    def __init__(self, dog_id: str, name: str, breed: str, sex: str, dob: str, human_id: str):
        """create dog with given info and human-object id"""
        self.id = dog_id
        self.name = name
        self.breed = breed
        self.sex = sex
        self.dob = dob
        self.human_id = human_id

    #def to_dict
        """convert dog data to dict, for json"""

    #def from_dict
        """create Dog instance from dict"""

class Registration:
    """saves, loads, and validates registration for dogs and humans"""

    def __init__(self, db_file="registry_data.json"):
        """pull existing registrations"""
        self.db_path = Path(db_file)
        self.humans = {}
        self.dogs = {}
        self.load_data()
    
    def load_data(self):
        """read from registry file with exeption handling"""
        if not self.db_path.exists():
            return
        #if content
        #load humans
        #load dogs
    
    def save_data(self):
        """write current data to registry file"""
        final_dict = {}
        #for human in humans, dog in dogs, add to dict)
        self.db_path.write_text(json.dumps(final_dict))

    def register_human(self, name: str, phone: str):
        """check for existing human (return empty string),
        else add human to humans and return generated id"""

        if not name or not phone:
            raise ValueError("name and phone number cannot be blank")

        for existing_id, existing_human in self.humans.items():
            if existing_human.name == name and existing_human.phone == phone:
                return ""

        next_num = len(self.humans) + 1
        new_id = f"H-{next_num}"
        self.humans[new_id] = Human(new_id, name, phone)
        self.save_data()
        return new_id

    def register_dog(self, name: str, breed: str, sex: str, dob: str, human_id: str):
        """register new dog if human exists,
        return generated id"""
        
        if human_id not in self.humans:
            raise ValueError(f"Human ID '{human_id}' is not registered in system")

        next_num = len(self.dogs) + 1
        new_id = f"D-{next_num}"
        self.dogs[new_id] = Dog(new_id, name, breed, sex, dob, human_id)
        self.save_data()
        return new_id

def get_clean_name(name: str):
    return name.strip().upper()
    
def get_clean_phone(phone: str):
    clean_phone = ""
    for char in phone:
        if char in string.digits:
            clean_phone += char
    return clean_phone

def print_header():
    print("-" * 40)
    print("    Daniel's Dog Clinic: Registration    ")
    print("-" * 40)

def print_menu():
    print("\nMenu:")
    print("1. Register new human")
    print("2. Register new dog (requires Human ID)")
    print("3. Search registered humans")
    print("4. Search registered dogs")
    print("5. Exit")

def main():

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
                print("That name/number is already in our system.")
    
        elif choice == '2':
            print("\n--New Dog Registration--")
            human_id = get_clean_name(input("Enter owner id (eg H-4): "))
            ######validate these inputs
            name = get_clean_name(input("Dog's name: "))
            breed = input("Breed: ")
            sex = input("Sex: ")
            dob = input("Estimated date of birth (YYYY-MM-DD): ")
            potential_id = clinic.register_dog(name, breed, sex, dob, human_id)
            print(f"\n{name.title()}'s ID is {potential_id}.")

if __name__ == "__main__":
    main()    