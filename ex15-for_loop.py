def print_for_loop():

    distros = ['Debian', 'Kali Linux', 'Ubuntu', 'Linux Mint', 'Gentoo', 'Fedora', 'Arch']

    ### Basic syntax
    for distro in distros:
        print(f'- {distro}')

    ### iterate with enumarate
    for idx, distro in enumerate(distros, 1):
        print(f'{idx}- {distro}')

    ### iterate over a range
    for i in range(0, 10, 2):
        print(f"something {i}")

    ### iterate over a range without catching the iterator
    for _ in range(0, 4):
        print("just a line")

    ### Iterate over a zipped list
    first_name = ['Ana', 'Miguel', 'David', 'Jose']
    last_name = ['Lopez', 'Castillo', 'Hernandez', 'Perez']

    for first, last in zip(first_name, last_name):
        print(f'Hello, {first} {last}')

    ### iterate over dictionary
    countries = {
        'Uruguay': 'Montevideo',
        'Argentina': 'Buenos Aires',
        'Brasil': 'Brasilia',
        'Chile': 'Santiago de Chile'
    }

    for country in countries:
        print(country)

    for country in countries.keys():
        print(country)

    for country in countries.values():
        print(country)

    for country in countries.items():
        print(country)

    ### What if I want to print the country and the capital separate
    for country in countries:
        print(f'The capital of {country} is {countries[country]}')

    ### A better way
    for country, capital in countries.items():
         print(f'The capital of {country} is {capital}')


    ### Resolves rain drops exercism
    def convert(number):
        message = str()
        factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

        for factor in factors:
            if number % factor == 0:
                message += factors.get(factor, '')

        return message if message else str(number)

if __name__ == '__main__':
    print_for_loop()