# create token
# create booking id
# update(put) the booking
# delete the booking

# verify that created booking id when we update we are able to to update it and delete the booking
# create token
# create booking
# test_update
# Fixtures--pass the data in Pytest

import pytest
import requests
import allure
import allure_pytest

from src.helpers.api_request_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util
from src.constants.api_constants import APIConstants


class Test_Crud_Booking(object):

    @pytest.fixture()
    def test_create_token(self):
        response = post_request(url=APIConstants.url_create_token(self),
                                headers=Util().common_headers_json(),
                                auth=None,
                                payload=payload_create_booking(),
                                in_json=False)
        verify_https_status_code(self,response_data=response, expect_data=200)
        verify_json_key_for_not_null_token(response.json()["token"])
        return response.json()["token"]

    @pytest.fixture()
    def test_get_booking_id(self):
        response = post_request(url=APIConstants.url_create_booking(self),
                                auth=None,
                                headers=Util.common_headers_json(self),
                                payload=payload_create_booking(),
                                in_json=False)
        booking_id = response.json()["bookingid"]
        # actual_status_code = response.status_code
        verify_https_status_code(self, response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    @pytest.mark.positive
    @allure.title("test crud operation Update(PUT)")
    @allure.description("Verify test crud operation Update(PUT) with booking id and token")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_put_patch_delete(booking_id=booking_id)
        response = put_request(
            url=put_url,
            headers=Util().common_header_put_patch_delete_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False,
            token=token
        )
        print(response.json)
        verify_https_status_code(response_data=response, expect_data=200)

    @pytest.mark.positive
    @allure.title("test crud operation DELETE")
    @allure.description("Verify booking gets deleted with the booking id and token")
    def test_delete_booking_id(self):
        pass
