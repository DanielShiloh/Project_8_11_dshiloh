"""
Daniel's Dog Clinic: Registration
Manage human and patient registration
Daniel Shiloh
July 3, 2026
"""

from pathlib import Path
import string
import json
from beings import Human, Dog

class Registration:
    """saves, loads, and validates registration for dogs and humans"""

    def __init__(self, db_file="registry_data.json"):
        """pull existing registrations"""
        self.db_path = Path(db_file)
        self.humans = {}
        self.dogs = {}
        self.load_data()
    
    def load_data(self):
        """read from registry file with exeption handling,
        create instances of Human and Dog from that file"""
        
        if not self.db_path.exists():
            return

        content = self.db_path.read_text()
        if not content:
            return
    
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            print("\nJSON parsing failed.  Starting fresh.")
            return
        
        for human_id, human_data in data.get("humans", {}).items():
            self.humans[human_id] = Human.from_dict(human_data)

        for dog_id, dog_data in data.get("dogs", {}).items():
            self.dogs[dog_id] = Dog.from_dict(dog_data)
    
    def save_data(self):
        """write current data to registry file"""
        final_dict = {}
        #TO DO: for human in humans, dog in dogs, add to dict
        self.db_path.write_text(json.dumps(final_dict))

    def register_human(self, name: str, phone: str):
        """check for existing human (return empty string),
        else add human to humans and return generated id"""

        if not name or not phone:
            raise ValueError("Name and phone number cannot be blank.")

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
            raise ValueError(f"Human ID '{human_id}' is not registered in system.")

        next_num = len(self.dogs) + 1
        new_id = f"D-{next_num}"
        self.dogs[new_id] = Dog(new_id, name, breed, sex, dob, human_id)
        self.save_data()
        return new_id