def print_if():

    #Basic Structure
    if True:
        print("Execute this 1")

    if not False:
        print("Execute this 2")

    if True and True:
        print("Execute this 3")

    if False or True:
        print("Execute this 4")

    if (True and True) or (True and False):
        print("Execute this 5")

    if False:
        print("Execute this 6")
    elif True:
        print("Execute this 7")
    else:
        print("Execute this 8")


    #Let's check if a Framework exists in a list
    frameworks = ['Angular', 'Laravel', 'Sprint', 'Flask', 'Rails', 'Bootstrap']

    if 'Flask' in frameworks:
        language = 'Python'
    elif 'Laravel' in frameworks:
        language = 'PHP'
    else:
        language = 'Unknown'

    print(language)

    #iterate over a list and compares its iterator
    for framework in frameworks:
        if framework == 'Laravel' or framework == 'Angular':
            stack = 'Web'
        elif framework in ('Flask', 'Sprint'):
            stack = 'Backend'
        else:
            stack = 'Unknown'

        print(f'Framework: {framework} \t Stack: {stack}')

    #Comprehensive if
    result = "It's a Framework" if 'Flask' in frameworks else "Not a Frameork"
    print(result)

if __name__ == '__main__':
    print_if()