# Password-Locker

## Table of Content

- [Description](#description)
- [Installation Requirement](#Installation)
- [Technology Used](#technology-used)
- [Reference](#reference)
- [Licence](#licence)
- [Authors Info](#author-Info)


## Behavior Driven Enviroment

- #### Create account
   - Given that a user has provided both a username and password
   - When a user requests to create an account
   - Then the system should create and save the account
- #### Login
  - Given that the user has a valid username and password
  - When the user requests to login 
  - Then the system should provide access

- #### Create credential
  - Given that a user has provided a valid site name, username and password
  - When a user requests to create a credential
  - Then the system should create and save the credentials


- ####Display Credential
   - Given that a user has credentials saved
   - When a user requests to see the details of saved credentials
   - Then the system should return all saved credentials
- ####  Delete Credential
   - Given that a user has credentials saved
   - When a user requests for a credential to be deleted
   - Then the system should delete the account


## Description

This is an application that helps users manage their password by saving them in here

## Installation

- Open Terminal - Ctrl+Alt+T

- git clone ```https://github.com/charity-bit/password_locker```

- cd password_locker

- open vs code with <code>code .</code>

### Running the Application

To run the application, in your terminal:

- <code>$ #!/usr/bin/env python3.9 or your python version</code>

- <code>$ chmod +x run.py</code>

- <code>$ ./run.py</code>

## Technology Use

- Python3.9

- Pyperclip

- pip3

## Reference

1. official python documentation <a href="https://docs.python.org/3/">docs</a>

2. Programiz.com <a href="https://www.programiz.com/python-programming">here</a>

3. Moringa School official content

## Licence

   copyright © Charity 2022 - <a href="https://github.com/charity-bit/password_locker/blob/main/LICENSE">MIT</a>

## Authors Info

-LinkedIn - [Charity Nyanchera](https://www.linkedin.com/in/charity-nyanchera-2679281a2/)

-twitter - [Twitter](https://twitter.com/CcNyanchera)

-[Go Back to the top](#password_locker)
