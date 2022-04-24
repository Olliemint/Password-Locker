


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
       
                
        
        