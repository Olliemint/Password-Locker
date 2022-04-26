import unittest
from user import User

class TestUser(unittest.TestCase):
    
    
    def setUp(self):
        '''
        set up method to run before each test
        create a new user before any test
        '''
        self.new_user = User("ollie",'22333')
        
        
    
    def test_init(self):
        '''
        test_init to test if the object is initialized properly
    
        '''
        self.assertEqual(self.new_user.username,"Olli")
        self.assertEqual(self.new_user.password,"jj101")
      
      
    
    def test_save_user(self):
        '''
        unit test to test if a user has been saved successfully
        ''' 
        self.new_user.save_user()
        self.assertEqual(len(User.users),1)
        
    def tearDown(self):
        '''
         clean users array after every test
        '''
        User.users = []
        
    def test_remove_user(self):
        self.new_user.save_user()
        test_user = User("Olli","22333")
        test_user.save_user()
        self.new_user.remove_user()
        self.assertEqual(len(User.users),1)
    


if __name__ == '__main__':
    unittest.main()