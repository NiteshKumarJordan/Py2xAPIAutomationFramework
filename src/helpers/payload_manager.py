# payloads
from faker import Faker
import json

faker = Faker()


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload



def payload_create_booking():
    payload = {
        "firstname": "James",
        "lastname": "Brown1",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }
    return payload


def _payload_create_booking_dynamic():
    payload = {
        "firstname": Faker().first_name(),
        #"lastname": faker().last_name,
        "lastname": Faker().last_name(),
        "totalprice": Faker().random_int(min=100, max=100000),
        "depositpaid": Faker().boolean(),
        "bookingdates": {
            "checkin": Faker().date_this_month(before_today=True),
            "checkout": Faker().date_this_month(before_today=True)
        },
        "additionalneeds": Faker().random_element(elements=("Breakfast", "Coffee", "Parking", "Wifi"))

    }
    return payload
