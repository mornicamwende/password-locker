import unittest
from account import Account
# import pyperclip

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account  class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("facebook","mwesh","2020") 
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Account.account_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"facebook")
        self.assertEqual(self.new_account.user_name,"mwesh")
        self.assertEqual(self.new_account.password,"2020")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),1)

    def test_save_multiple_account(self):
        '''
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Account("facebook","mwesh","2020") # new account
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
        '''
        test_delete_account to test if we can remove a account from our account list
        '''
        self.new_account.save_account()
        test_account = Account("facebook","mwesh","2020") # new account
        test_account.save_account()

        self.new_account.delete_account()# Deleting a contact object
        self.assertEqual(len(Account.account_list),1)

    def test_find_account_by_account_name(self):
        '''
        test to check if we can find an account by account name and display information
        '''

        self.new_account.save_account()
        test_account = Account("facebook","mwesh","2020") # new account
        test_account.save_account()

        found_account = Account.find_by_account_name("facebook")

        self.assertEqual(found_account.user_name,test_account.user_name)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account= Account("facebook","mwesh","2020") # new account
        test_account.save_account()

        account_exists = Account.account_exist("0711223344")

        self.assertTrue(not(account_exists))

    def test_display_all_account(self):
        '''
        method that returns a list of all account saved
        '''

        self.assertEqual(Account.display_account(),Account.account_list)




if __name__ == '__main__':
    unittest.main()