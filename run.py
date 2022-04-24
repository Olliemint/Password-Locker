#!/usr/bin/env python3.8


import random

from User import User

import Credentials

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
    
    
    
def display_user_details(User):
    
    return User.view_user_details()      
    
    
    
  
    
    

def main():
    
    while True:
        print("Welcome to Password-Locker")
        print('\n')
        print("Please select a short code to cruise through:To create new user use 'NU': For logging in to your account use 'LG':And finally to exit use 'EX'")
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
                
        
        elif shortcode == 'EX':
            break
        
        else:
            
            print("Pick valid shortcode to continue")  
            
            
if __name__ == '__main__':

    main()                                 
                  
            
            

                     
                
                    
                    
            
            
        