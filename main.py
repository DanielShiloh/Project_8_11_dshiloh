"""
Daniel's Dog Clinic
---------------------purpose------------------
Daniel Shiloh
July 3, 2026
"""

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
        """checks for existing human and returns id,
        else add human to humans and return generated id"""

        if not name or not phone:
            raise ValueError("name and phone number cannot be blank")
        
        clean_name = name.strip().lower()
        clean_phone = ""
        for char in phone:
            if char in string.digits:
                clean_phone += char

        for existing_id, existing_human in self.humans.items():
            if existing_human.name == clean_name and existing_human.phone == clean_phone:
                return existing_id

        next_num = len(self.humans) + 1
        new_id = f"H-{next_num}"
        self.humans[new_id] = Human(new_id, clean_name, clean_phone)
        self.save_data()
        return new_id

    def register_patient(self, dog_id):
        """register new dog/owner pair, validates input"""
        return


def print_header():
    print("-" * 40)
    print("    Daniel's Dog Clinic: Registration    ")
    print("-" * 40)

def print_menu():
    print("\nMenu:")
    print("1. Register new patient")
    print("2. Search registered patients")
    print("3. Exit")

def main():

    clinic = Registration()

    print_header()

    while True:
        print_menu()
        choice = input("Select an option (1-3): ")

        if choice == '1':
            print("\n--New Registration--")
            #get inputs
            #check age is number

    

if __name__ == "__main__":
    main()    