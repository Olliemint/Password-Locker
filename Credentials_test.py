import unittest

from Credentials import Credentials


class TestCredentials(unittest.TestCase):
    
    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        
        '''
        Set up method to run before each test cases.
        '''
        
        self.new_credentials = Credentials("Pintrest","Pin580","5555")
        
        
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = [] 
            
            
            
            
              
    def test_init(self):
        
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credentials.account_name,"Pintrest")
        self.assertEqual(self.new_credentials.user_name,"Pin580")
        self.assertEqual(self.new_credentials.Pass_word,"5555")
        
        
        
    def test_add_credentials(self):
        
        """
        test case if we can add new user
        
        """ 
        
        self.new_credentials.add_credentials()
        
        self.assertEqual(len(Credentials.credentials_list),1)  
        
        
        
    def test_add_multiple_credentials(self):
        
        """
        test case if we can add multiple credentials
        
        """ 
        
        self.new_credentials.add_credentials()
        
        test_credentials = Credentials("Pixabay","Fury","2233")  
        
        test_credentials.add_credentials()
        
        self.assertEqual(len(Credentials.credentials_list),2) 
        
        
        
        
    def test_delete_credentials(self):
        
        """
        test case to check if we can delete user credentiials
        
        """ 
        
        self.new_credentials.add_credentials()
        
        test_credentials = Credentials("Pixabay","Fury","2233")  
        
        test_credentials.add_credentials()
        
        self.new_credentials.delete_credentials()
        
        self.assertEqual(len(Credentials.credentials_list),1)
        
        
        
    def test_view_credentials(self):
        
        """
        test case to check if we can view user credentials
        
        """  
        
        
        self.assertEqual(Credentials.view_credentials(),Credentials.credentials_list)  
        
        
           
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()          