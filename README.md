# Password-Locker

# By Oliver Maiyo

## Table of Content

- [Description](#Description)
- [Behavior Driven Enviroment](#Behavior Driven Enviroment)
- [Installation Requirement](#Installation)
- [Technology Used](#technology-used)
- [Reference](#reference)
- [Licence](#licence)
- [Authors Info](#author-Info)

## Description

Password-Locker allow users to create and account and let them stores user passwords for different sites and can also generates random passwords for them once they log in

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


- #### Display Credential
   - Given that a user has credentials saved
   - When a user requests to see the details of saved credentials
   - Then the system should return all saved credentials
- ####  Delete Credential
   - Given that a user has credentials saved
   - When a user requests for a credential to be deleted
   - Then the system should delete the account



## Installation

- Open Terminal - Ctrl+Alt+T

- git clone ```https://github.com/Olliemint/Password-Locker.git```

- open vs code with <code>code .</code>

### Running the Application

To run the application, in your terminal:

- <code>$ #!/usr/bin/env python3.8 or your python version</code>

- <code>$ chmod +x run.py</code>

- <code>$ ./run.py</code>

## Technology Use

- Python3.8

- pip3

## Reference

1. official python documentation <a href="https://docs.python.org/3/">docs</a>

2. GeekFlare<a href="https://geekflare.com/password-generator-python-code/">here</a>

3. official flask documentation <a href="https://flask.palletsprojects.com/en/2.1.x/">docs</a>

## Licence

   copyright © Oliver Maiyo 2022 

## Authors Info

-LinkedIn - [Oliver Maiyo](https://www.linkedin.com/in/oliver-maiyo-191943225/)

-twitter - [@Furymint](https://twitter.com/Furymint)

-[Go Back to the top](#Password-Locker)
