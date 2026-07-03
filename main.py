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

    def __init__(self, name: str, phone: str):
        """create owner with given info"""
        self.name = name
        self.phone = phone

class Dog:
    """represents single patient"""

    def __init__(self, name: str, human: Human):
        """create dog with given info and Human object"""
        self.name = name
        self.human = human

class Registration:
    """saves, loads, and validates registration"""

    def __init__(self, db_file="registry_data.json"):
        """pull existing registrations"""
        self.db_path = Path(db_file)
        self.patients = {}
        self.load_data()
    
    def load_data(self):
        """read from registry file with exeption handling"""

        if not self.db_path.exists():
            return
    
    def save_data(self):
        """write current data to registry file"""
        new_dict = ""
        self.db_path.write_text(json.dumps(new_dict))

    def register_patient(self, dog_id):
        """register new dog/owner pair, validates input"""
        return
    
def main():
    clinic = Registration()
    print("-" * 40)
    print("    Daniel's Dog Clinic: Registration    ")
    print("-" * 40)

if __name__ == "__main__":
    main()    