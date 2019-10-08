def print_convert_datatypes():
    #Convert number to String
    number = 55
    print(55)

    number_to_string = str(55)
    print(number_to_string)

    print(type(number))
    print(type(number_to_string))

    #Convert String to Number
    string = '1_000_000'
    string_to_number = int(string)

    print(string)
    print(string_to_number)

    #Convert Int to Float
    integer = 100
    int_to_float = float(integer)

    print(integer)
    print(int_to_float)

    #Convert String to List
    name = 'Victor'
    name_to_list = list(name)

    print(name)
    print(name_to_list)
    print(type(name))
    print(type(name_to_list))

    # Convert List to String
    name_list = ['V', 'i', 'c', 't', 'o', 'r']
    name_string = str(name_list) # It doesn't do what we expected

    print(name_list)
    print(name_string)

    name_string = "".join(name_list)
    print(name_string)

    name_string_v2 = str().join(name_list)
    print(name_string_v2)

if __name__ == '__main__':
    print_convert_datatypes()