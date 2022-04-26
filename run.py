#!/usr/bin/python3.9
from ast import If
from user import User,Credentials
import pyperclip as pyc


def create_user(username,password):
    '''
    Method to create a new user
    '''
    new_user = User(username,password)
    return new_user

def s_user(user):
    '''
    method to save a newly created user
    '''
    user.save_user()
    
def r_user(user):
    '''
    method to create a user
    '''
    user.remove_user()
    
def create_creds(site_name,username,password):
    '''
    method to create a credential
    '''
    new_creds = Credentials(site_name,username,password)
    return new_creds

    
def u_cred(creds):
    '''
    method to update a credential
    '''
    return creds.update_cred()


def remove_cred(cred):
    '''
    method to delete a credential
    '''
    return cred.remove_cred()


def s_creds(creds):
    '''
    method to save a credential
    '''
    creds.save_creds()
    
def search_creds(name):
    '''
    method to search for a credential by name
    '''
    return Credentials.search_cred(name)


def auth(name,password):
    '''
    method to check if a uer already exists in the users list
    '''
    return Credentials.aunthenticate(name,password)


def disp_creds():
    '''
    method to display a list of credentials
    '''
    return Credentials.display_creds()



def main():
    
    print("Welcome to Password-Locker")
    print("*"*30)
    
    
    while True:
        '''
         login section 
         CA - create account
         LI - Login
         EX - exit
         
        '''
      
        print("Use These short codes to Navigate:ca - to login: li - to login: ex - to exit")
        print("\n")
      
        shortcode = input("Enter the shortcode: ").lower().strip()
        print("\n")
        
        if shortcode == 'ca':
            print("Enter Your Details")
            print("*"*20)
            username = input("Enter your Username: ").strip()
            print("\n")
            
            while True:
                print("Enter tp - to type in your password")
                print("Enter gp - to be generated password")
                
                print("\n")
                pass_choice = input("Choice:").lower().strip()
                
                if pass_choice == 'tp':
                    password = input("Enter password: ")
                    break
                elif pass_choice == 'gp':
                    print("Enter the length of the password")
                    print("Password must be between 8 and 12")
                    len=int(input("Length:"))
                    
                    if len > 12 or len < 8:
                        print("length must not be less than 8 or greater than 12")
                        
                    else:
                        password = Credentials.generate_password(len)
                        print(f"Your password is {password}")
                        break
                        
                else:
                    print("Invalid Choice.Please use short codes")
                    
            password=password.strip()
            if password == "" or username == "":
                print("/n")
                print("ACCOUNT CREATION FAILED:Username and Password cannot be empty.Please try again")
            else:
                
                s_user(create_user(username,password))
                print("\n")
                print("Account created successfully")
                print(f"tUse username:{username} and password:{password} to login ")
                print("\n")
                
        elif shortcode == 'li':
            
            print("Enter your credentials to login")
            username = input("Username:")
            password = input("Password:")
            print('\n')
                
            user = auth(username,password)
            print("*"*20)
             
            
            
            if user == username:
                print(f"Hello, {username}.Proceed to select a short code to navigate")
                
                while True:
                   
                    print("cc  - create an a new credential")
                    print("dc - display credentials")
                    print("fc - find credential")
                    print("rm - remove credential")
                    print("up - update credential")
                    print("cp - copy credential")
                    print("ex - exit app")
                    print('\n')
                    print("*"*20)
                    
                    
                    shortcode = input("Shortcode:").lower().strip()
                    print("\n")
                    
                    if shortcode == 'cc':
                        # create a new credential
                        print("Enter details of the new credentials")
                        site_name = input("Account Name:").strip()
                        user_name = input("User Name:").strip()
                        while True:
                            print("Enter tp - to type in your password")
                            print("Enter gp - to be generated password\n")
                
                          
                            pass_choice = input("Choice:").lower().strip()
                
                            if pass_choice == 'tp':
                                password = input("Enter password:")
                                break
                            elif pass_choice == 'gp':
                                print("Enter the length of the password")
                                print("Password must be between 8 and 12")
                                len=int(input("Length:"))
                    
                                if len > 12 or len < 8:
                                    print("length must not be greater than 12 or less than 8")
                        
                                else:
                                    password = Credentials.generate_password(len)
                                    print(f"Your password is {password}")
                                    break
                            else:
                                print("Invalid Choice.Please use short codes")
                        password=password.strip() 
                        if site_name == "" or user_name == "" or password == "":
                            print("FAILED TO CREATE AND SAVE CREDENTIALS:Please fill in all details")
                           
                        else:
                            s_creds(create_creds(site_name,user_name,password))
                        
                        
                            
                    elif shortcode == 'fc':
                        print("Enter the name of the account you want to find")
                        print("\n")
                        account_name = input("Account Name:").strip()
                        print("\n")
                        
                        if search_creds(account_name):
                            account = search_creds(account_name)
                            print("tAccount\t\tUsername\t\tPassword")
                            print("_"*30)
                            print(f"{account.site_name}\t\t{account.username}\t\t{account.password}")
                            
                            
                        else:
                            print("Account not found")
                                
                    
                    elif shortcode == 'dc':
                        if disp_creds():
                            for cred in disp_creds():
                                
                                print("_"*20)
                                print(" Account Name\t\t  Username\t\t Password")
                                print(f"{cred.site_name}\t\t{cred.username}\t\t{cred.password}")
                                print("\n")
                                
                        else:
                            print("\n")
                            print("There are no saved credentials available")
                            print("\n")
                            
                    elif shortcode == 'rm':
                        print("\n")
                        print("Enter the name of the account you wan't to delete")
                        account_name = input("Account Name:").strip()
                        print("\n")
                        
                        if search_creds(account_name):
                            account = search_creds(account_name)
                            remove_cred(account)
                            if disp_creds():
                                for cred in disp_creds():
                                    print("Remaing Accounts......")
                                    print("_"*50)
                                    print(f"{cred.site_name}\t\t{cred.username}\t\t{cred.password}")
                                
                            else:
                                print("No accounts remaining")
                               
                        else:
                            print("Account not found")
                            
                            
                    elif shortcode == 'cp':
                        print("Enter the account you want to update")
                        account_name = input("Account Name:").strip()
                        if search_creds(account_name):
                            account = search_creds(account_name)
                            pyc.copy(account.password)
                            print("Password copied to clipboard")
                        else:
                            print("account not found")
                            
                    elif shortcode == "up":
                        print("Enter the account you want to update")
                        account_name = input("Account Name:").strip()
                        if search_creds(account_name):
                            account = search_creds(account_name)
                            print("Enter the username to change username.")
                            print("\n")
                            print("If you not wish to change the username, type existing username")
                            username = input("Username:").strip()
                            print("\n")
                            while True:
                                print("Enter tp - to type in new password")
                                print("Enter gp - to be generated new password\n")
                
                                
                                pass_choice = input("Choice:").lower().strip()
                
                                if pass_choice == 'tp':
                                    password = input("Enter password:")
                                    break
                                elif pass_choice == 'gp':
                                    print("Enter the length of the password")
                                    print("Password must be between 8 and 12")
                                    len=int(input("Length:"))
                    
                                    if len > 12 or len < 8:
                                        print("length must not be greater than 12 or less than 8")
                        
                                    else:
                                        password = Credentials.generate_password(len)
                                        print(f"Your password is {password}")
                                        break
                                else:
                                     print("\t\t\t\t\tInvalid Choice.Please use short codes")
                                     
                            if password == "" or username == "":
                                print("UPDATE FAILED.Please try filling in the values in order to update credential")
                            
                            else:
                                password=password.strip()        
                                account.username = username
                                account.password = password
                                print("Account Updated")
                                print("Remaing Accounts......")
                                print("_"*20)
                                print(f"{account.site_name}\t\t{account.username}\t\t{account.password}")
                            
                            
                        else:
                            print("Account not found")
                            
                    elif shortcode == 'ex':
                        print("\n")
                        print("*"*30)     
                       
                        print(f"Goodbye,{username} See you again later")
                        
                        
                        break
                        
                    else:
                       
                        print("I did not get that, Please use the provided short codes")
                        
            
                        
                        
            else:
                print("Wrong credentials.Please try again")                
                        
                    
                    
        
        
        elif shortcode == 'ex':
            print("\n")
            print("*"*20)     
            
            print("Goodbye, See you again later")
           
            
            break
        else:
            print("*"*20)
            print("I did not get that, Please use the provided short codes")
           
            
            
        
        
    
    
    

if __name__ == '__main__':
    main()
    
