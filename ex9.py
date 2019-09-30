def print_dictionaries():
    Countries = {'Uruguay':
                  {'official_name': 'República Oriental del Uruguay',
                   'capital': 'Montevideo',
                   'population': 3_457_000,
                   }
              }

    print(Countries)

    Countries['Venezuela'] = {'official_name': 'República Bolivariana de Venezuela',
                           'capital': 'Caracas',
                           'population': 31_980_000,
                           }
    print(Countries)
    print(Countries['Venezuela'])
    print(Countries['Uruguay'])
    print(Countries['Uruguay']['population'])
    print(Countries['Venezuela']['capital'])

    country = 'Venezuela'
    print("The Capital of {} is {}".format(country, Countries[country]['capital']))

    #What if I ask for a non existing key
    country = 'Uruguay'
    #language = Countries[country]['language']
    language = Countries[country].get('language', 'Not Specified')
    print(f'The Population of {country} is {language}')

    population = Countries[country].get('population', 'NULL')
    print(f'The Population of {country} is {population}')

    countries_keys = Countries.keys()
    countries_values = Countries.values()
    countries_items = Countries['Uruguay'].items()

    print(countries_keys)
    print(countries_values)
    print(countries_items)

    del Countries['Venezuela']['population']
    print(Countries['Venezuela'])



if __name__ == '__main__':
    print_dictionaries()
