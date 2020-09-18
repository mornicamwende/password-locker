#!/usr/bin/env python3.8
from account import Account

def create_account(account_name,user_name,password):
    '''
    Function to create a new accounts
    '''
    new_account = Account(account_name,user_name,password)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to deletes an account
    '''
    account.delete_account()

def find_account(string):
    '''
    Function that finds a account by account name and returns the account
    '''
    return Account.find_by_account_name(string)

def check_existing_account(string):
    '''
    Function that check if an account exists with that account_name and return a Boolean
    '''
    return Account.account_exist(string)

def display_account():
    '''
    Function that returns all the saved account
    '''
    return Account.display_account()


def main():
    print("Hello! Welcome to your password locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}! what would you like to do?")
    print('\n')
    while True:
                    print("Use these short codes : cc - create a new account, dc - display accounts, fc -find an account, ex -exit the account list ")
                    short_code = input().lower()
                    if short_code == 'cc':
                            print("New Account")
                            print("-"*10)
                            print ("account name ....")
                            account_name = input()
                            print("Username ...")
                            user_name = input()
                            print("password ...")
                            password = input()
                            save_account(create_account(account_name,user_name,password)) # create and save new account.
                            print ('\n')
                            print(f"New Account {account_name} {user_name} with the password {password} created")
                            print ('\n')
                    elif short_code == 'dc':
                            if display_account():
                                    print("Here is a list of all your accounts")
                                    print('\n')
                                    for account in display_account():
                                        print(f"Name: {account.account_name} {account.user_name} {account.password}")
                                    #     print(f": {contact.phone_number}")
                                    # print(f"Email address: {contact.email}")
                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any account saved yet")
                                    print('\n')
                    elif short_code == 'fc':
                            print("Enter the account name you want to search for")
                            # search_number = input()                            
                            search_string = input()


                            if check_existing_account(search_string):
                                    search_account = find_account(search_string)
                                    print(f"{search_account.account_name} {search_account.user_name}")
                                    print('-' * 20)
                                    print(f"account_name.......{search_account.account_name}")
                                    print(f"user_name.......{search_account.user_name}")
                            else:
                                    print("That  does not exist")
                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()


