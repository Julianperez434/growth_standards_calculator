import pytest
from growth_standards_calculator import main, Person, generate_height_boys_csv, generate_height_girls_csv, generate_bmi_boys_csv, generate_bmi_girls_csv, generate_csv_files

def test_gender_valid():
    person = Person()
    person.gender = "Male"
    assert person.gender == "Male"


def test_gender_invalid():
    person = Person()
    with pytest.raises(ValueError):
        person.gender = "House"


def test_age_valid():
    person = Person()
    person.age = 10
    assert person.age == 10


def test_age_invalid():
    person = Person()
    with pytest.raises(ValueError):
        person.age = 20


def test_height_valid():
    person = Person()
    person.height = 150.0
    assert person.height == 150.0


def test_height_invalid():
    person = Person()
    with pytest.raises(ValueError):
        person.height = "cat"


def test_weight_valid():
    person = Person()
    person.weight = 50.0
    assert person.weight == 50.0


def test_weight_invalid():
    person = Person()
    with pytest.raises(ValueError):
        person.weight = "cat"


def test_calculate_bmi():
    person = Person()
    person.height = 160.0
    person.weight = 55.0
    bmi = 55.0 / (1.6 ** 2)
    assert person.calculate_bmi() == bmi


def test_csv_generation():
    assert generate_height_boys_csv() == 0
    assert generate_height_girls_csv() == 0
    assert generate_bmi_boys_csv() == 0
    assert generate_bmi_girls_csv() == 0
    assert generate_csv_files() == 0
