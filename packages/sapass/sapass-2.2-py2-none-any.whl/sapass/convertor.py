import hashlib
import re
import uuid

class convertor():
    def __init__(self):
        pass

    @classmethod
    def hash_password(cls, password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    @classmethod
    def hash_password_validate(cls, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    @classmethod
    def password_strong_check(cls, password):
        """
        Verify the strength of 'password'
        Returns a dict indicating the wrong criteria
        A password is considered strong if:
            8 characters length or more
            1 digit or more
            1 symbol or more
            1 uppercase letter or more
            1 lowercase letter or more
        """

        # calculating the length
        length_error = len(password) < 8

        # searching for digits
        digit_error = re.search(r"\d", password) is None

        # searching for uppercase
        uppercase_error = re.search(r"[A-Z]", password) is None

        # searching for lowercase
        lowercase_error = re.search(r"[a-z]", password) is None

        # searching for symbols
        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

        # overall result
        password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

        return {
            'password_ok': password_ok,
            'length_error': length_error,
            'digit_error': digit_error,
            'uppercase_error': uppercase_error,
            'lowercase_error': lowercase_error,
            'symbol_error': symbol_error,
        }


# new_pwd = "testPWd"
# hashed_password = convertor.hash_password(new_pwd)
# print(hashed_password)
# old_pass = new_pwd
# if convertor.hash_password_validate(hashed_password, old_pass):
#     print('You entered the right password')
# else:
#     print('I am sorry but the password does not match')
#
print(convertor.password_strong_check("hello"))
print(convertor.password_strong_check("hello_W0rld"))
