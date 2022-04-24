
import unittest

from User import User  # Importing the User and Credentials class



class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("user001","2580")   # create new object
    
    
    def test_init(self):
        self.assertEqual(self.new_user.username,"user001")
        self.assertEqual(self.new_user.password,"2580") 
        
        
if __name__ == '__main__':
    unittest.main()           
    
    

