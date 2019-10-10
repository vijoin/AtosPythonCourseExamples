def print_operators():

    x = 7
    y = 3


    # Arithmetic operators
    print(x + y) #Addition
    print(x - y) #Subtraction
    print(x * y) #Multiplication
    print(x / y) #Division
    print(x % y) #Modulus
    print(x ** y) #Exponentiation
    print(x // y) #Floor division


    # Assignment operators
    x += 7 #Same as x = x + 7
    x -= 7 #Same as x = x - 7
    x *= 7 #Same as x = x * 7
    x /= 7 #Same as x = x / 7
    x %= 7 #Same as x = x % 7
    x //= 7 #Same as x = x // 7
    x **= 7 #Same as x = x ** 7

    # Comparison operators
    print(x == y)  # Equal
    print(x != y)  # Not equal
    print(x > y)   # Greater than
    print(x < y)   # Less than
    print(x >= y)  # Greater than or equal to
    print(x <= y)  # Less than or equal to

    # Logical operators
    print(x < 5 and x < 10)
    print(x < 5 or x < 4)
    print(not (x < 5 and x < 10))


    # Identity operators
    print(x is y)
    print(x is not y)

    # Membership operators
    x = [1, 5, 10, 7, 6]
    print(7 in x)
    print(12 not in x)


if __name__ == '__main__':
    print_operators()

