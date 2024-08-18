import unittest
from vodafone_app.authenticator import Authenticator

class TestVodafoneApp(unittest.TestCase):
    def test_authenticator(self):
        authenticator = Authenticator("1234567890", "password")
        # ToDo

if __name__ == '__main__':
    unittest.main()
