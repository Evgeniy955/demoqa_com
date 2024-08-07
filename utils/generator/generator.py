import random

from allure import step
from faker import Faker

from testlib.data.data import Person, PersonInTextBox, get_project_path

faker_en = Faker('En')


@step('generated person')
def generated_person():
    return Person(
        last_name=faker_en.last_name(),
        first_name=faker_en.first_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject="English"
    )


@step('generated person for text box')
def generated_person_for_text_box():
    return PersonInTextBox(
        full_name=faker_en.name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address()
    )


@step('generated file')
def generated_file():
    path = get_project_path() + '\\Translation{random.randint(10, 100)}.txt'
    file = open(path, 'w')
    file.write(f'Helloworld{random.randint(23, 100)}')
    file.close()
    return path
