import unittest
from airthemetic import*

class Test_Arithmetic(unittest.TestCase):
    def setUp(self):
        self.a=Airthmetic()


    def test_add(self):
        self.assertEqual(5,self.a.add(2,3))


