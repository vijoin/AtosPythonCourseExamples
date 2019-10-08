from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def print_dates():
    #Get current time
    current_date = datetime.now()
    print(f'Today is: {current_date}')

    #Get Tomorrow
    one_day = timedelta(days=1)
    tomorrow = current_date + one_day
    print(f'Tomorrow will be {tomorrow}')

    #Get Yesterday
    yesterday = current_date - one_day
    print(f'Yesterday was {yesterday}')

    #Split the date
    day = current_date.day
    month = current_date.month
    year = current_date.year
    print(f'Day is: {day}')
    print(f'Month is: {month}')
    print(f'Year is: {year}')

    #Parse string to time
    birthday = input('When is your birthday (dd/mm/yyyy)?: ')
    birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
    print(f'Datatype {type(birthday_date)}')
    print(f'Year {birthday_date.year}')

    #How old are you?
    years_old = relativedelta(current_date, birthday_date).years
    print(f'You are {years_old} years old')


if __name__ == "__main__":
    print_dates()