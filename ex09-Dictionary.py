def print_dictionaries():
    #Add a country
    countries = {'Uruguay':
                     {'official_name': 'República Oriental del Uruguay',
                      'capital': 'Montevideo',
                      'population': 3_457_000,
                      }
                 }

    print(countries)

    #Add a second key
    countries['Venezuela'] = {'official_name': 'República Bolivariana de Venezuela',
                              'capital': 'Caracas',
                              'population': 31_980_000,
                              }
    print(countries)


    #access to a specific key
    print(countries['Venezuela'])
    print(countries['Uruguay'])

    #Access multilevel key
    print(countries['Uruguay']['population'])
    print(countries['Venezuela']['capital'])

    country = 'Venezuela'
    print("The Capital of {} is {}".format(country, countries[country]['capital']))

    #What if I ask for a non existing key
    country = 'Uruguay'
    #language = Countries[country]['language']

    ## I can catch the error with the get() method
    language = countries[country].get('language', 'Not Specified')
    print(f'The Population of {country} is {language}')

    population = countries[country].get('population', 'NULL')
    print(f'The Population of {country} is {population}')

    #Access to the keys
    countries_keys = countries.keys()
    print(countries_keys)

    #Access to the values
    countries_values = countries.values()
    print(countries_values)

    #Access both keys and items
    countries_items = countries['Uruguay'].items()

    print(countries_items)

    del countries['Venezuela']['population']
    print(countries['Venezuela'])

    print("Los datos de Venezuela son {official_name}, {capital}, {population}".format(**countries['Venezuela']))


if __name__ == '__main__':
    print_dictionaries()
