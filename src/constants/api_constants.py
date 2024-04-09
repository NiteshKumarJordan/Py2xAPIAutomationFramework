
#API CONSTANTS = class which contains all the end points
# keep the url
# static method:- which can be called without the object directly by using class name


class APIConstants(object):

    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/token"

    @staticmethod
    def url_create_user(self):
        return "https://restful-booker.herokuapp.com/user"

    @staticmethod
    def url_put_patch_delete(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)






