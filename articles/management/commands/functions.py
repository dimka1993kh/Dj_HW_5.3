from random import randrange
from datetime import timedelta, datetime

def random_date():
    date_1 = datetime(1970, 1, 1).date()
    date_2 = datetime.now().date()

    delta = date_2 - date_1

    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)

    return date_1 + timedelta(seconds=random_second)