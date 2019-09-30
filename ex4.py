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


    CONSTANT = "ALL IN CAPITAL LETTERS"
    print(CONSTANT)

    #This is a comment

    """
    Mutiline Comments 
    """
if __name__ == "__main__":
    print_hello()
