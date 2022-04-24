import pyperclip


class User:
    """
    class to generate objects/new instance of User
    """
    user_list = []
    """
    Empty user list for saving user objects
    """
    
    def __init__(self,username,password):
        
        """
        method that defines user attributes and we can pass the Args
        """
        
        self.username = username
        self.password =  password
    
    
    def add_new_user(self):
        
        """
        saves user objects to user_list
        """   
        
        User.user_list.append(self) 
        
        
        
    def delete_user(self):
        
        User.user_list.remove(self)
        
    @classmethod 
    def view_user_details(cls):
        
        
        '''
        method that returns the user list
        '''
        
        return cls.user_list
    
    
    @classmethod 
    def copy_user_details(cls,string):
        
        
        '''
        Method that takes in a string and returns a username that matches that string.

        Args:
            string: username to search for
        Returns :
            username of person that matches the string.
            
        '''
        for user in cls.user_list:
            if user.username == string:
                return user
   
        
       
                
        
        