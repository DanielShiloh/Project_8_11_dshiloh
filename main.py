"""
Daniel's Dog Clinic
---------------------purpose------------------
Daniel Shiloh
July 3, 2026
"""

class Human:
    """represents dog owner"""

    def __init__(self, name: str, phone: str):
        """create owner with given info"""
        self.name = name
        self.phone = phone

class Dog:
    """single patient at clinic"""

    def __init__(self, name: str, human: Human):
        """create dog with given info and Human object"""
        self.name = name
        self.human = human