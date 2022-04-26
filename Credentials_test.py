import unittest

from user import Credentials



class TestCredential(unittest.TestCase):
    '''
     Unitest for the credential class
    '''
    
    def setUp(self):
        '''
        set up Method to create a new cred before every test
        '''
        
        self.new_cred = Credentials("twitter","Ccnyanchera","qwertyip")
    def tearDown(self):
        '''
        clear the creds lists after every test
        '''
        Credentials.creds_list = []
        
    def test_init(self):
        '''
        unittest to test if the object is being initialized properly
        '''
        self.assertEqual(self.new_cred.site_name,"twitter")
        self.assertEqual(self.new_cred.username,"Ccnyanchera")
        self.assertEqual(self.new_cred.password,"qwertyip")
    
    def test_save_creds(self):
        '''
        test if a credential has been saved successfully
        '''
        self.new_cred.save_creds()
        self.assertEqual(len(Credentials.creds_list),1)
        
    def test_remove_cred(self):
        '''
        unittest to test if a credential has been removed
        
        '''
        self.new_cred.save_creds()
        test_cred = Credentials("facebook","CcNyanchera","qwertyip")
        test_cred.save_creds()
        test_cred.remove_cred()
        self.assertEqual(len(Credentials.creds_list),1)
        
    def test_update_cred(self):
        '''
        unittest to test if a credential has been updated successfully
        '''
        self.new_cred.save_creds()
        self.new_cred.password = "QWERTYIP"
        self.new_cred.username = "charity"
        self.new_cred.save_creds()
        self.assertEqual(self.new_cred.password,"QWERTYIP")
        self.assertEqual(self.new_cred.username,"charity")
        self.assertEqual(self.new_cred.site_name,"twitter")
        
    def test_save_multiple_creds(self):
        '''
        unittest to test if a user can save multiple credentials
        '''
        self.new_cred.save_creds()
        test_cred1= Credentials("facebook","CcNyanchera","qwertyip")
        test_cred2 = Credentials("Instagram","CcNyanchera","qwertyip")
        test_cred1.save_creds()
        test_cred2.save_creds()
        self.assertEquals(len(Credentials.creds_list),3)
        
    def test_search_cred(self):
        '''
        test to check if we can find a contact by name
        '''
        self.new_cred.save_creds()
        test_cred= Credentials("facebook","CcNyanchera","qwertyip")
        test_cred.save_creds()
        found_cred = Credentials.search_cred("facebook")
        self.assertEquals(found_cred.password,test_cred.password)
        
        


if __name__ == '__main__':
    unittest.main()