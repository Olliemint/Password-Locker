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
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()          