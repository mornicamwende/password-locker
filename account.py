
class Account:
    """
    Class that generates new instances of accounts
    """
    def __init__(self,account_name,user_name,password):

        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    account_list = [] 
    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    @classmethod
    def find_by_account_name(cls,string):
        '''
        Method that takes in an account name and returns credentials that matches that account name.

        Args:
            string: account name to search for
        Returns :
            Credentials of person that matches the account name
        '''

        for account in cls.account_list:
            if account.account_name == string:
                return account

    @classmethod
    def account_exist(cls,string):
        '''
        Method that checks if an account exists from the account list.
        Args:
            string: account name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.account_name == string:
                    return True

        return False

    @classmethod
    def display_account(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    # @classmethod
    # def copy_email(cls,number):
    #     contact_found = Contact.find_by_number(number)
    #     pyperclip.copy(contact_found.email)

    