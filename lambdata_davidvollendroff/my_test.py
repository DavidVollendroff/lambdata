import unittest

class MyTest(unittest.TestCase):
  def oneplusone(self):
    self.assertEqual(1+1, 2)
    
if __name__ == '__main__':
  unittest.main()
