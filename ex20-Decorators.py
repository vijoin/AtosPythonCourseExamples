def suma(a, b):
    print("{}".format(a + b))

suma(1,2)
suma1 = suma
suma2 = suma
suma1(2,2)


def log(f):
    def wrapper(f, *args):
        print(f"Function: {f.__name__}")
        return f(args)
    return wrapper

suma = log(suma)
print(suma(4,5))
