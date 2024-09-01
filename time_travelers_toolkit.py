import datetime as dt
from decimal import Decimal
from random import randint, choice

import custom_module

years = [randint(1900, 3000) for i in range(10)]
#target_year = randint(1900, 3000)

target_year = choice(years)

current = dt.datetime.now()
print(f"Date : {current.date()}")
print(f"Time : {current.time()}")

base_cost = Decimal('12.0394')
year_cost = target_year - current.year
time_travel_cost = round( base_cost * year_cost, 2)

print(time_travel_cost)

print(custom_module.generate_time_travel_message(target_year, "Mars", time_travel_cost))
