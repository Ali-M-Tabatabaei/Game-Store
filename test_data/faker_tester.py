from faker import Faker
from reference_lists import cities
import random
from datetime import date, timedelta

fake = Faker()

seven_days = timedelta(days=7)
next_week = date.today() + seven_days
print(next_week)
the_fake = fake.date_between(date.today(), next_week)
print(type(str(the_fake)))