class Employee:

    IPC = 0.08

    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.email = f"{name}.{lastname}@company.com".lower()
        self.salary = salary

    def __repr__(self):
        return "Employee: {} {}".format(self.name, self.lastname)

    def raise_salary(self):
        self.salary += self.salary * self.IPC


class Developer(Employee):

    def __init__(self, name, lastname, salary, prog_lang):
        super().__init__(name, lastname, salary)
        self.prog_lang = prog_lang

    def __repr__(self):
        return "Developer: {} {}".format(self.name, self.lastname)


class Manager(Employee):

    def __init__(self, name, lastname, salary, department):
        super().__init__(name, lastname, salary)
        self.department = department

    def __repr__(self):
        return "Manager: {} {}".format(self.name, self.lastname)

    def raise_salary(self, bonus=0):
        super().raise_salary()
        self.salary += bonus

if __name__ == '__main__':
    employee = Employee('Victor', 'Inojosa', 40_000)
    print(employee.email)

    developer = Developer('DevVictor', 'DevInojosa', 45_000, 'Python')
    print(developer.email)
    print(developer.prog_lang)

    manager = Manager('ManVictor', 'ManInojosa', 50_000, 'HR')
    print(manager.email)
    print(manager.department)

    #Modify a class attribute (not a instance attribute)
    Employee.IPC = 0.09
    print(developer.IPC)

    employee.raise_salary()
    print(employee.salary)

    manager.raise_salary(2000)
    print(manager.salary)

