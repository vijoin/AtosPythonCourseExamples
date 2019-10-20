def area_cuadrado(b, h):
    return b * h

def suma(n1, n2, n3=0):
    return n1 + n2 + n3

def suma_args(*args):
    return sum(args)

def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        return f"Key: {k} - Value: {v}"

def funcion(b=0, h=None, *args, **kwargs):
    area = b * h
    suma = sum(args)

    if 'name' in kwargs:
        print(f"{kwargs['name']}")

    return f"area: {area} suma: {suma}"


def print_name(b, h, name='', lastname=''):
    dictionary = {
        'name': name,
        'lastname': lastname
    }
    print("nombre: {name} apellido: {lastname}".format(**dictionary))


def compute_age(date):


#Given a birthday date, calculate the age
def person_age(name, lastname='', birthday):
    age =


if __name__ == '__main__':
    print(area_cuadrado(2, 5))
    print(suma(1, 4, 6))
    print(suma(1, 4))
    print(suma(n2=3, n3=5, n1=5))
    print(suma_args(5, 6, 7, 8))
    print(print_kwargs(name='Victor', last_name='Inojosa', age=34))
    print_name(1, 2, lastname='ino2', name='vic')


