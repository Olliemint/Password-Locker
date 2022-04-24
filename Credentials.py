import random


class Credentials:
    
    """
    class to generate objects/new instance of Credetials
    """
    
    
    credentials_list = []
    
    
    def __init__(self,account_name,user_name,Pass_word):
        
        
        """
        method that defines user attributes and we can pass the Args
        """
        
        self.account_name = account_name
        self.user_name = user_name
        self.Pass_word = Pass_word
        
        
        
    def add_credentials(self):
        
        """
        saves user objects to user_list
        """ 
        Credentials.credentials_list.append(self)
        
        
    def delete_credentials(self):
        
        
        Credentials.credentials_list.remove(self)
        
        
        
    def generate_password(self):
        
        characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
        
        password_length = 6
        
        password = "".join(random.sample(characters, password_length))
        
        return password
        
              
        
        
        
    @classmethod 
    
    def view_credentials(cls):
        
        
        """"
        method to view user credentials
        
        """
        
        return cls.credentials_list
        
          
        
        
            
        
        
        