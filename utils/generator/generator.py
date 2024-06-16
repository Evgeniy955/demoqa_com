import random


from faker import Faker

from testlib.data.data import Person

faker_en = Faker('En')

def generated_person():
    return Person(
        last_name = faker_en.last_name(),
        first_name = faker_en.first_name(),
        email = faker_en.email(),
        current_address = faker_en.address(),
        mobile = faker_en.msisdn(),
        subject = "English"
    )


def generated_file():
    path = rf'C:\Users\Yevhen\PycharmProjects\youtube_test\Translation{random.randint(10,100)}.txt'
    file = open(path, 'w')
    file.write(f'Helloworld{random.randint(23,100)}')
    file.close()
    return path