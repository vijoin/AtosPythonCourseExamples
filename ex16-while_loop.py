def print_while():

    #Basic Syntax
    number = 10
    while number > 1:
        print(f'number is: {number}')
        number -= 1


    #Let the user decide when to finish
    prompt = "\nPlease enter the name of a dish you have tasted:"
    prompt += "\n(Enter 'quit' to leave.) "

    while True:
        dish = input(prompt)
        if dish == 'quit':
            break
        else:
            print(f"I'd love to taste the {dish.title()}!")

    ### Lets print numbers
    number = 15
    while number > 0:
        number -= 1
        if not number % 3 == 0:
            continue
        print(number)

    ### Remove from list
    mascotas = ['pez', 'gato', 'perro', 'dragon', 'tigre', 't-rex', 'perro', 'gato', 'ballena']

    while 'gato' in mascotas:
        mascotas.remove('gato')
    print(mascotas)



if __name__ == '__main__':
    print_while()