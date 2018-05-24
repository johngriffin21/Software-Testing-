import unittest
from pop.up import divideby

class AddTestCase(unittest.TestCase):

     def test_one(self):
         self.assertEqual(divideby(2,2),1)
     def test_two(self):
         self.assertNotEqual(divideby(2,2),3)
         
if __name__ == '__main__':
     unittest.main()
