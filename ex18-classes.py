# class Person():
#     name = 'Victor'
#     last_name = 'Inojosa'
#     age = 34
#
#
#     def get_personal_info(self):
#         return "Name: {}\nLast name: {}\nAge: {}".format(self.name, self.last_name, self.age)
#
#
# if __name__ == '__main__':
#     person = Person()
#     print(person.get_personal_info())
#     person.city = 'Montevideo'
#     print(person.city)

class Person():

    def __init__(self, name, last_name, age, city):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.city = city

    def get_personal_info(self):
         return "Name: {}\nLast name: {}\nAge: {}\nCity: {}".format(
             self.name, self.last_name, self.age, self.city)

    def get_personal_info_v2(self, *args):
        info = ''
        for arg in args:
            if hasattr(self, arg):
                value = self.__getattribute__(arg)
                info += "{}: {}\n".format(arg.title(), value)
            else:
                info += "{}: {}\n".format(arg, 'Not Found')
        return info


if __name__ == '__main__':
    #person1 = Person('Victor', 'Inojosa', 34, 'Montevideo')
    #print(person1.get_personal_info())

    person2 = Person(name='Laura', age=38, city='Montevideo', last_name='Albarracin')
    #print(person2.get_personal_info())

    print(person2.get_personal_info_v2('name', 'age', 'city', 'address', 'asdasdas'))