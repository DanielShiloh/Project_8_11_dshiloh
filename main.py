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

class Dog:
    """represents single patient"""

    def __init__(self, dog_id: str, name: str, breed: str, sex: str, dob: str, human_id: str):
        """create dog with given info and human-object id"""
        self.id = dog_id
        self.name = name
        self.breed = breed
        self.dob = dob
        self.human_id = human_id

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
    
    def save_data(self):
        """write current data to registry file"""
        new_dict = ""
        self.db_path.write_text(json.dumps(new_dict))

    def register_human(self, name: str, phone: str) -> bool:
        """register human, generates id"""
        human_id = len(self.humans) + 1
        self.humans[human_id] = Human(human_id, name, phone)
        self.save_data()
        return True

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