import unittest
from activities.login_system import login

class TestLogin(unittest.TestCase):
    def test_login(self):
        self.assertEqual(login("admin", "1234"), "Login successful")
        self.assertEqual(login("admin", "wrong"), "Invalid credentials")
        self.assertEqual(login("user", "1234"), "Invalid credentials")
