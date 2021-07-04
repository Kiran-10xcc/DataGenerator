import csv
import random
from time import time
from decimal import Decimal
from faker import Faker
fake = Faker(locale='en_GB')
RECORD_COUNT = 100



def create_csv_file():
    with open('customer.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'product_id', 'qty',
                      'amount', 'description', 'address', 'city', 'county',
                      'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'first_name': fake.name(),
                    'last_name': fake.name(),
                    'email': fake.email(),
                    'product_id': fake.random_int(min=100, max=199),
                    'qty': fake.random_int(min=1, max=9),
                    'amount': float(Decimal(random.randrange(500, 10000))/100),
                    'description': fake.sentence(),
                    'address': fake.street_address(),
                    'city': fake.city(),
                    'county': fake.county(),
                    'country': fake.country()
                }
            )
if __name__ == '__main__':
    create_csv_file()