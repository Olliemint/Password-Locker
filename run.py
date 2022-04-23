import random

import User

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
                    
            
            
        