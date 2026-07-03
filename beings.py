"""
Daniel's Dog Clinic: Beings
Define human and dog models, linking dog to human
Daniel Shiloh
July 3, 2026
"""

class Human:
    """represents dog owner"""

    def __init__(self, human_id: str, name: str, phone: str):
        """create owner with given info"""
        self.id = human_id
        self.name = name
        self.phone = phone
        
    def to_dict(self):
        """convert human data to dict, for json"""
        return {"id": self.id, "name": self.name, "phone": self.phone}

    @classmethod
    def from_dict(cls, data: dict):
        """create Human instance from dict"""
        return cls(data["id"], data["name"], data["phone"])

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

    def to_dict(self):
        """convert dog data to dict, for json"""
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "sex": self.sex,
            "dob": self.dog,
            "human_id": self.human_id
        }

    @classmethod
    def from_dict(cls, data: dict):
        """create Dog instance from dict"""
        return cls(data["id"], data["name"], data["breed"], data["sex"], data["dob"], data["human_id"])