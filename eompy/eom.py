import unittest

class agetest(unittest.TestCase):
    def testentry(self):
        x=int(input("enter age"))
        message="false"
        self.assertIn(x, range(1, 110), message)
