import pytest
import requests
from jsonschema import validate
import os

from src.helpers.api_request_wrapper import *
from jsonschema.exceptions import ValidationError
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util
from src.constants.api_constants import APIConstants


class TestCreateBookingJSONSchema(object):

    def load_schema(self, file_name):
        with open(file_name, 'r') as file:
            return json.load(file)

    def test_get_booking_schema(self):
        response = post_request(url=APIConstants.url_create_booking(self),
                                auth=None,
                                headers=Util.common_headers_json(self),
                                payload=payload_create_booking(),
                                in_json=False)
        booking_id = response.json()["bookingid"]

        # actual_status_code = response.status_code
        verify_https_status_code(self,response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        # verify response with json stored
        #print(os.getcwd())
        file_path = os.getcwd() + "/schema.json"
        schema = self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(), schema=schema, )

        except ValidationError as e:
            print(e.message)
