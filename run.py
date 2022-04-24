#!/usr/bin/env python3.8


import random

from User import User

from Credentials import Credentials


# Class user functions

def create_user(username,password):
    new_user = User(username,password)
    
    return new_user


def add_new(User):
    
    
    """
    function to add user
    """
    
    User.add_new_user()
    
    
    
def delete_users(User):
    
    """
    function to delete user
    
    """
    
    User.delete_user() 
    
    
    
def display_user_details():
    
    return User.view_user_details() 



     
    
#   class credentials functions


def new_credentials(account_name,user_name,Pass_word):
    
    new_credentials = Credentials(account_name,user_name,Pass_word)
    
    return new_credentials



def more_credentials(Credentials):
    
    """
    function to save credentials
    """
    
    Credentials.add_credentials()
    
    
    
def remove_credentials(Credentials):
    
    """
    function to delete credentials
    
    """  
    
    Credentials.delete_credentials() 
    
    
    
    
def view_credentials():
    
    return Credentials.view_credentials()


# def mygenerated_password(Credentials):
    
#     Credentials.generate_password()    
    
     
    
    
    
      
    
  

    

def main():
    
    while True:
        print("Welcome to Password-Locker")
        print('\n')
        print("Please select a short code to cruise through:To create new user use 'NU': For logging in to your account use 'LG':To view Your details use 'VW':And finally to exit use 'EX'")
        print("To store existing tutorials use 'CS'")
        shortcode = input().upper()
        print('\n')
        
        
       
        
        
        if shortcode == 'NU':
            
            print("Create your Username:")
            entered_username = input()
            
            print("Create your Password")
            entered_password = input()
            
            print("Confirm your Password")
            confirm_password = input()
            
            
            
            while confirm_password != entered_password:
                print("Your password did not match")
                print("Enter your password again")
                entered_password = input()
                print("Confirm Your password")
                confirm_password = input()
                
            else:
                print(f"Hurray {entered_username} your account was created successfully")
                print('\n')
                print("Continue to Login")
                print("Enter your Username")
                entered_user_name = input()
                print("Enter Password")
                entered_user_password = input()
                
                
            while entered_user_name != entered_username or entered_user_password != entered_password:
                print("Your Username or Password is invalid")
                print("Re-enter your Username")
                entered_user_name = input()
                print("Enter your Password")
                entered_user_password = input()
                
            else:
                print(f"Welcome {entered_user_name} you've logged in succesfully")
                print("\n") 
                
                
                
            add_new(create_user(entered_user_name,entered_password))
                  
                
                
        elif shortcode == 'CS':
            print("New Credentials")
            
            print("\n")
            
            print("Enter Account Name:")
            a_name = input()
            
            print("Enter Username:")
            u_name = input()
            
            print("To type Account password type 'TP':To let the system generate for you type 'GP':")
            code = input().upper()
            
            if code == 'TP':
                print("Enter Account Password:")
                
                a_password = input()
            elif code == 'GP':
                
                a_password = Credentials.generate_password(6) 
                
                print(f"Generated password is: {a_password} ")
                   
            
            # a_password = input()
            
            more_credentials(new_credentials(a_name,u_name,a_password))
            print("\n")
            print(f"New Credentials {a_name} {u_name} {a_password}")

            print("\n")
            
            
            
                
        elif shortcode == 'LG':
            print("Welcome, Login to your Account")
            print("Enter your Username")
            default_username = input()

            
            print("Enter Passwprd")
            default_password = input()
            print("\n")
            
            while default_username != "user001" or default_password != "2580":
                 print("Invalid username or password. Username is 'user001' and Password is '2580'")
                 print("Enter your Username")
                 default_username = input()
                 print("Enter Password")
                 default_password = input()
                 
            else:
                print("Logged in Succesfully")
                
                print("\n") 
                
        elif shortcode == 'VW':
            
            
           
           
            
            if display_user_details():
                
                print("Here is a List of your User Data")
                
                print("\n") 
                
                for User in display_user_details():
                    print(f"{User.username}  {User.password}")
                    
                    print("\n")          
                
            else:
                print("\n")
                print("Your dont have stored User Data yet. Please save and check again")
                print("\n")
        
        elif shortcode == 'EX':
            break
        
        else:
            
            print("Pick valid shortcode to continue")  
            
            
if __name__ == '__main__':

    main()                                 
                  
            
            

                     
                
                    
                    
            
            
        