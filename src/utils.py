from datetime import datetime, timedelta
from faker import Faker


faker = Faker()


def get_fly_book():
    return {
        'client': faker.name().replace('\'', '\\\''),
        'number': faker.sha1(),
        'fly_from': faker.country_code(),
        'fly_to': faker.country_code(),
        'book_date': str(faker.date_time_this_month())
    }


def get_hotel_book():
    return {
        'client': faker.name().replace('\'', '\\\''),
        'hotel': faker.address().replace('\'', '\\\'').replace('\n', '; '),
        'arrival': str(faker.date_time_this_month()),
        'departure': str(datetime.now() + timedelta(days=faker.random_digit()))
    }

