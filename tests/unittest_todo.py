import unittest
class TestProject(unittest.TestCase):
    #Fixture /Metodo que se ejecuta antes del test
    def setUp(self):
        print("set up")
    def test_one(self):
        print("Test one")
    def test_two(self):
        print("Test two")
    def test_three(self):
        print("Test three")
    # Fixture /Metodo que se ejecuta despues del test
    def tearDown(self):
        print("tearDown")
