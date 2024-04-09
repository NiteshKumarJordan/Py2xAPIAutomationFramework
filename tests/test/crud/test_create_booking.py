import pytest
import requests
import allure
import allure_pytest

from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util
from src.constants.api_constants import APIConstants


class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("verify that booking status is correct and booking id should not be null")
    @allure.description(
        "Creating a booking from payload and verify that booking is should not be null and status code should be 200")
    def test_create_booking_positive(self):
        # url, # headers # payload

        response = post_request(url=APIConstants.url_create_booking(self),
                                auth=None,
                                headers=Util.common_headers_json(self),
                                payload=payload_create_booking(),
                                in_json=False)
        booking_id = response.json()["bookingid"]
        # actual_status_code = response.status_code
        verify_https_status_code(self, response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

    def test_create_booking_tc2_negative(self, response_data):
        response = post_request(url=APIConstants.url_create_booking(self), auth=None,
                                headers=Util.common_headers_json(),
                                payload=payload_create_booking(), in_json=False)
        verify_https_status_code(response, 500)
