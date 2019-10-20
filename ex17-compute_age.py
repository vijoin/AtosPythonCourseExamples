from datetime import datetime
from dateutil.relativedelta import relativedelta

def compute_age(date):
    current_date = datetime.now()
    birthday_date = datetime.strptime(date, '%d/%m/%Y')
    age = relativedelta(current_date, birthday_date).years
    return age

#Given a birthday date, calculate the age
def person_age(name, lastname, birthday):
    age = compute_age(birthday)

    return " Nombre: {}\n Apellido: {}\n " \
           "Edad: {}".format(name, lastname, age)

def run():
    name = input("Ingrese su nombre: ")
    lastname = input("Ingrese su apellido: ")
    birthday = input("Ingrese su fecha de nacimiento (dd/mm/yyyy): ")

    print(person_age(name, lastname, birthday))


if __name__ == '__main__':
    run()
