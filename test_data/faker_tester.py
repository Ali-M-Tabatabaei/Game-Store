from faker import Faker

fake = Faker()

print(fake.date_between('-60d'))