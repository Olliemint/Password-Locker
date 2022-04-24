class Credentials:
    
    """
    class to generate objects/new instance of Credetials
    """
    
    
    credentials_list = []
    
    
    def __init__(self,account_name,Pass_word):
        
        
        """
        method that defines user attributes and we can pass the Args
        """
        
        self.account_name = account_name
        self.Pass_word = Pass_word
        
        
        