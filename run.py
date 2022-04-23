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
            
            
        