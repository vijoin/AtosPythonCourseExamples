def print_hello():
    first = "Hello"
    second = "World!"
    if True:
        print("The message is: '{} {}'".format(first, second))
        print("""This a multiline Text.
         And this 
            is the prove""")
        username = input("Please, enter your username: ")
        print("Your username is: '{}'".format(username))

def print_variables():
    a = 3
    b = a
    c = b + 4
    d, e, f = a, b, c


    print(a)
    print(b)
    print(c)

    print(d)
    print(e)
    print(f)


if __name__ == "__main__":
    print_hello()

    print_variables()

