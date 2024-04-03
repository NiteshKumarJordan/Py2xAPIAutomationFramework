# class or functions

class Util(object):

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass

    def common_headers_json(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        return headers

    def common_headers_xml(self):
        headers = {
            'Accept': 'application/xml',
            'Content-Type': 'application/xml'
        }
        return headers

    def common_headers_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": " Basic" + str(basic_auth_value),
        }
        return headers

    def common_header_put_patch_delete_cookie(self, token):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            "Cookie": "token=" + str(token)
        }
        return headers
