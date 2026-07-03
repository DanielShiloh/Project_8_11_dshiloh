"""
Daniel's Dog Clinic: Registration Tests
Verify rules for user-entered data
Daniel Shiloh
July 3, 2026
"""

from pathlib import Path
import json
import pytest
from registration import Registration

#setup

@pytest.fixture
def temp_db(tmp_path):
    """create temporary db file path for testing"""
    return Path(tmp_path, "test_registry.json")

#human registration tests

def test_register_first_human(temp_db):
    """does the first human get id H-1?"""
    clinic = Registration(db_file=temp_db)
    generated_id = clinic.register_human(name="First Human", phone="123")
    assert generated_id == "H-1"
    assert "H-1" in clinic.humans

def test_register_duplicate_human(temp_db):
    """does registering an existing human block the second attempt?"""
    clinic = Registration(db_file=temp_db)
    first_reg_id = clinic.register_human(name="Repeat Me", phone="1234")
    second_reg_id = clinic.register_human(name="Repeat Me", phone="1234")
    assert second_reg_id == ""

def test_register_human_with_blank_fields_fails(temp_db):
    """does leaving fields blank give an error?"""
    clinic = Registration(db_file=temp_db)
    try:
        clinic.register_human(name="", phone="")
        pytest.fail("ValueError not raised")
    except ValueError:
        pass


#dog registration tests

def test_register_dog_with_valid_human(temp_db):
    """can a dog be registered to an existing human?"""
    clinic = Registration(db_file=temp_db)
    human_id = clinic.register_human(name="Im Human", phone="4321")
    dog_id = clinic.register_dog(
        name="human's dog", 
        breed="mix", 
        sex="m", 
        dob="2026-01-01", 
        human_id=human_id
    )
    assert dog_id == "D-1"
    assert "D-1" in clinic.dogs

def test_register_dog_with_invalid_human_fails(temp_db):
    """does an invalid human id stop a dog from registering?"""
    clinic = Registration(db_file=temp_db)
    try:
        clinic.register_dog(
            name="humanless", 
            breed="foop", 
            sex="f", 
            dob="2020-01-01", 
            human_id="H-999"
        )
        pytest.fail("Dog registered without valid human.")
    except ValueError:
        pass


#file read/write tests