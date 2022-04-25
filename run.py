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
        print("Welcome to PassWord-Locker.")
        print('\n')
        print("Use these short codes to navigate through: Create New User use 'nw' and 'ex' To exit Password-Locker")
        shortcode = input().lower()
        print('\n')
        
        if shortcode == 'nw':
        
            print("Create your Username:")
            entered_username = input()
            
            print("Create your Password")
            entered_userpassword = input()
            
            print("Confirm your Password")
            confirm_password = input()
            
            while confirm_password != entered_userpassword:
                print("Sorry your passwords did not match!")
                print("Enter a password")
                entered_userpassword  = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {entered_username}! You have created your new account.")
                print('\n')
                print("Proceed to Log In to your Account")
                print("Username")
                entered_username = input()
                print("Your Password")
                entered_password = input()
            while entered_username != entered_username or entered_password != entered_userpassword:
                print("Invalid username or password")
                print("Username")
                entered_username = input()
                print("Your Password")
                entered_password = input()
            else:
                print(f"Welcome: {entered_username},login scuccesfull")
                
                print('\n')
            add_new(create_user(entered_username,entered_userpassword))
        
            while True:
                print("Choose a shortcode: nc -create New Credentials,sc - save existing, vc -view credentials,dl -To delete and ex -exit ")
                picked_code = input("Enter code:").lower()
                
                if picked_code == 'nc':
                    
                    print("Enter New Credentials")
                    print("-"*20)
                    A_name = input("Enter Account Name:")
                    print("\n")
                    A_user = input("Enter Username:")
                    print("\n")
                    
                    while True:
                        print("tp - To type your own Password")
                        print("gp - To generate random Password")
                        sel_code = input("Enter code choice:").lower()
                        
                        if sel_code == 'tp':
                            print("Enter password:")
                            A_pass = input("Password:")
                        elif sel_code == 'gp':
                            A_pass = Credentials.generate_password(6)
                            print(f"Generated password is:{A_pass}")
                            
                            print("\n")
                            
                            break
                        else:
                            print("Invalid code,Enter provided codes")
                            
                    more_credentials(new_credentials(A_name,A_user,A_pass))        
                
                elif sel_code == 'sc':
                    print("Enter Existing credentials ")
                    print("-"*20)
                    print("Enter Account Name:")
                    a_name = input("Account name:")
                    print("\n")
                    print("Enter Username:") 
                    a_user = input("Username:")   
                    print("\n")
                    print("Enter Password:")
                    a_pass = input("Password:")
                    print("\n")
                    
                    more_credentials(new_credentials(a_name,a_user,a_pass))
                    break
                
                elif sel_code == 'vc':
                    if view_credentials():
                        print("Credentials List") 
                        print("*"*20)
                        for Credentials in view_credentials():
                            print("Account Name  Account Username  Account Password")
                            print("_"*30)
                            print(f"{Credentials.account_name}  {Credentials.user_name}  {Credentials.Pass_word}")
                    
                    else:
                        print("🥵You dont have saved credentials")
                
                elif sel_code == 'dl':
                    print("To delete type y/n")
                    delete = input().lower()
                    
                    if delete == 'y':
                        
                        remove_credentials(Credentials.credentials_list)
                        break
                    else:
                        print("Oops you dont have and credentials saved")
                        break
                elif sel_code == 'ex':
                    print("🔚Goodbye, you;ve exited Credentials Account")
                    break
                
                else:
                    print("😟 Please select a valid shortcode") 
                    
                    
                
        elif shortcode == 'ex':
            print("🔚Goodbye, you have exited Password-Locker")
            break
        
        else:
            print("😟 Please select a valid shortcode")
             



    
if __name__ == '__main__':

    main()    
    
    
    
    
    
#     while True:
      
#         print("Welcome to Password-Locker")
        
#         print("\n")
#         print("Create new user 'NU':To login 'LG':To delete details 'DL':To exit 'EX'")
#         shortcode = input("Enter your choice:").upper()
        
#         if shortcode == 'NU':
            
#             print("Create your Username:")
#             entered_username = input()
            
#             print("Create your Password")
#             entered_password = input()
            
#             print("Confirm your Password")
#             confirm_password = input()
            
            
            
#             while confirm_password != entered_password:
#                 print("Your password did not match")
#                 print("Enter your password again")
#                 entered_password = input()
#                 print("Confirm Your password")
#                 confirm_password = input()
                
#             else:
#                 print(f"Hurray {entered_username} your account was created successfully")
#                 print('\n')
#                 # print("Continue to Login")
#                 # print("Enter your Username")
#                 # entered_username = input()
#                 # print("Enter Password")
#                 # entered_user_password = input()
#             add_new(create_user(entered_username,entered_password))    
                
#             # while entered_user_name != entered_username or entered_user_password != entered_password:
#             #     print("Your Username or Password is invalid")
#             #     print("Re-enter your Username")
#             #     entered_user_name = input()
#             #     print("Enter your Password")
#             #     entered_user_password = input()
                
#             # else:
#             #     print(f"Welcome {entered_user_name} you've logged in succesfully")
#             #     print("\n")
                
           
                
            
            
                
#         elif shortcode == 'LG':
#             print("Welcome, Login to your Account")
#             print("Enter your Username")
#             a_name = input("Username:")

            
#             print("Enter Passwprd")
#             a_password = input("Password:")
#             print("\n")
            
#             while a_name != entered_username or a_password !=entered_password:
#                  print("Invalid username or password.")
#                  print("Enter your Username")
#                  a_name = input("Username:")
#                  print("Enter Password")
#                  a_password = input("Password")
                 
#             else:
#                 print("Logged in Succesfully")
                
#                 print("\n")
            
#             while True:
                
#                 print("Use the short codes to navigate:'NC' Create new credentials: 'SA' Save existing credentials: 'VW' View Credntials:'EX' To exit")
                
#                 p_code = input("Enter short code:").upper()
                
                
#                 if p_code == 'NC':
                    
#                     print("Create Acount Credentials")
                    
#                     print("__"*20)
                    
#                     print("Enter Acount Name")
#                     C_name = input()
                    
#                     print("\n")
#                     print("Enter Username")
                    
#                     C_usern = input()
                    
                    
#                     print("TP - to type your own password")
#                     print("GP -random generated password")
                    
#                     p_word = input("Enter shortcode")
                    
#                     if p_word == 'TP':
                        
#                         print("Enter Password")
#                         print("\n")

#                         C_pass = input()
#                     elif p_word == 'GP':
                        
#                         C_pass = Credentials.generate_password(6) 
                        
#                         break
                        
#                     else:
#                         print("Invalid short code, choose either TP or GP")
                        
#                         break
                        
#                     more_credentials(new_credentials(C_name,C_usern,C_pass)) 
                        
                        
                
#                 # print("")       
                            
#                 elif shortcode == 'SA':
                    
#                     print("Save Acount Credentials")
                    
#                     print("__"*20)
                    
#                     print("Enter Acount Name:")
#                     S_name = input("Account name:")
                    
#                     print("\n")
#                     print("Enter Account Username: ")
#                     S_usern = input("Username:")
#                     print("\n")
                    
#                     print("Enter Account Password:")
#                     S_pass = input("Password:")
                    
#                     print("\n")
                    
#                     more_credentials(new_credentials(S_name,S_usern,S_pass))
                    
#                 elif shortcode == 'VW':
                    
#                     if view_credentials():
                        
#                         print("Here is Credentials List")
                        
#                         for Credentials in view_credentials():
                            
#                             print("Account Name     Username      Password")
#                             print("*"*20)
                            
#                             print(f" {Credentials.account_name}     {Credentials.user_name}     {Credentials.Pass_word}")
#                             print("\n")
                    
                    
#                     else:
#                         print("You dont have any Saved Credentials yet")        
                            
                            
                            
                    
                        
                    
#                 elif shortcode == 'EX':
                    
#                     print("You've exited Credentials section")
                    
#                     break
                
#                 else:
                    
#                     print("Please enter a valid code")    
                
                
                 
                
#         # elif shortcode == 'VW':
            
            
           
           
            
#         #     if display_user_details():
                
#         #         print("Here is a List of your User Data")
                
#         #         print("\n") 
                
#         #         for User in display_user_details():
#         #             print(f"{User.username}  {User.password}")
                    
#         #             print("\n")          
                
#         #     else:
#         #         print("\n")
#         #         print("Your dont have stored User Data yet. Please save and check again")
#         #         print("\n")
        
#         elif shortcode == 'EX':
#             break
        
#         else:
            
#             print("Pick valid shortcode to continue")  
            
            
# if __name__ == '__main__':

#     main()                                 
                  
            