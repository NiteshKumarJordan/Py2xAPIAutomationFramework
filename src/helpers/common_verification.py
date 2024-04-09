def verify_https_status_code(self, response_data, expect_data):
    assert response_data.status_code == expect_data, "expected https status code"


def verify_json_key_for_not_null(key):
    assert key != 0, "key is not null" + key
    assert key != 0, "key is not empty and key is greater than 0"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "key is not null" + key


def verify_response_key_should_not_be_null(key):
    assert key is not None, "key is not null" + key
