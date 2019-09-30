def print_strings():

    one_line_string = "Hello World"
    multi_line_string = """ Lorem ipsu
                        Example 7
                        of Strings"""

    print(one_line_string)
    print(multi_line_string)
    print(one_line_string[4]) #Why the 'o' and not the 'l'
    print(one_line_string[0]) #Because the first position is zero

#    print("Hello "World"") #Error
#    print('Hello 'World'') #Error
    print("Hello 'World'") #Correct
    print('Hello "World"') #Correct


    slice_string = one_line_string[2:8] #gets until 7, but do not include it

    print(slice_string)
    print(one_line_string[4:]) #From 5th position to the end
    print(one_line_string[:4]) #From beggining to the 5th position (not included)
    print(one_line_string[-1]) #Last string
    print(one_line_string[-3]) #Third Last string
    print(one_line_string[3:-3]) #From 4th to 3rd last (not included)

    #add and multiply ith string
    sum_string = one_line_string + ", Again!"

    print(sum_string)
    #print(one_line_string + 125)
    print(sum_string * 2)
    print(sum_string.lower())
    print(sum_string.upper())
    print(sum_string.lower().title())

    string_lower = one_line_string.lower()
    print(string_lower.isupper())
    print(string_lower.islower())

    num_string = '105'
    print(num_string.isnumeric())

    #replacing
    a = "string"
    print(a.replace("ring", "anillo"))
    print(a)
    a = a.replace("ring", "anillo")
    print(a)

    #Using Variables in String
    #Python 3.5+
    name = 'Victor'
    lastname = 'Inojosa'

    print(f'Hello {name} {lastname}')

    #before 3.5
    print('Hello Again {} {}'.format(name, lastname))
    print('Hello Again-Again {n} {ln}'.format(ln=lastname, n=name))
    print('Hello %s. Your lastname is %s' % (name, lastname))


if __name__ == '__main__':
    print_strings()