
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
        
        
    def test_add_multiple_users(self):
        
        """
        check if we can save multiple user data
        """   
        
        self.new_user.add_new_user()
        
        test_user = User("Test101","5656")
        
        test_user.add_new_user()
        
        self.assertEqual(len(User.user_list),2) 
        
        
        
    def test_delete_contact(self):
        
        """
        testing id we can delete user
        
        """ 
        
        self.new_user.add_new_user()
        
        test_user = User("Test101","5656")
        
        test_user.add_new_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
        
        
    def test_view_user_details(self):
        
        '''
        method that returns a list of all contacts saved
        '''
        
        self.assertEqual(User.view_user_details(),User.user_list)    
        
         
        
        
             
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()           
    
    

