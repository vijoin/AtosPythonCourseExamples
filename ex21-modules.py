import datetime
from dateutil import relativedelta

birthday = datetime.datetime.strptime('06/05/1985', '%d/%m/%Y')
current_date = datetime.datetime.now()
age = relativedelta.relativedelta(current_date, birthday).years

####
from datetime import datetime
from dateutil.relativedelta import relativedelta

birthday = datetime.strptime('06/05/1985', '%d/%m/%Y')
current_date = datetime.now()
age = relativedelta(current_date, birthday).years


####
from datetime import datetime as dt, time
from dateutil.relativedelta import relativedelta as rd

birthday = dt.strptime('06/05/1985', '%d/%m/%Y')
current_date = dt.now()
age = rd(current_date, birthday).years

####
from datetime import *
from dateutil.relativedelta import *

birthday = dt.strptime('06/05/1985', '%d/%m/%Y')
current_date = dt.now()
age = rd(current_date, birthday).years

if __name__ == '__main__':
    print(age)
    print(dir(datetime))