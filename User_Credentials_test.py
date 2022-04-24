
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


    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list= []
    
    
    
    
    
    def test_init(self):
        
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_user.username,"user001")
        self.assertEqual(self.new_user.password,"2580") 
        
        
    def test_add_new_user(self):
        
        '''
        test_add_new_user test case to test if the contact object is saved into
         the user list
        '''
        
        self.new_user.add_new_user()  #saving new user
        
        self.assertEqual(len(User.user_list),1)
        
        
             
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()           
    
    

