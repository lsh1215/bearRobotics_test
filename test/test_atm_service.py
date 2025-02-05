import unittest
from model.bank_service_impl import BankServiceImpl

class TestBankServiceImpl(unittest.TestCase):
    def setUp(self):
        self.bank_service = BankServiceImpl()

    def test_verify_pin_success(self):
        # Given
        card_number = "1111-2222-3333-4444"
        pin = "1234"

        # When
        result = self.bank_service.verify_pin(card_number, pin)

        # Then
        self.assertTrue(result)

    def test_verify_pin_fail_wrong_pin(self):
        # Given
        card_number = "1111-2222-3333-4444"
        wrong_pin = "9999"

        # When
        result = self.bank_service.verify_pin(card_number, wrong_pin)

        # Then
        self.assertFalse(result)

    def test_verify_pin_fail_no_card(self):
        # Given
        card_number = "1234-1234-1234-1234"
        pin = "1234"

        # When
        result = self.bank_service.verify_pin(card_number, pin)

        # Then
        self.assertFalse(result)

    def test_get_accounts_success(self):
        # Given
        card_number = "1111-2222-3333-4444"

        # When
        accounts = self.bank_service.get_accounts(card_number)

        # Then
        self.assertEqual(accounts, ["ACC123", "ACC456"])

    def test_get_accounts_empty(self):
        # Given
        card_number = "1234-1234-1234-1234"

        # When
        accounts = self.bank_service.get_accounts(card_number)

        # Then
        self.assertEqual(accounts, [])

    def test_get_balance_success(self):
        # Given
        account_id = "ACC123"

        # When
        balance = self.bank_service.get_balance(account_id)

        # Then
        self.assertEqual(balance, 100)

    def test_get_balance_missing(self):
        # Given
        account_id = "NOTEXIST"

        # When
        balance = self.bank_service.get_balance(account_id)

        # Then
        self.assertEqual(balance, 0)


    def test_deposit_existing_account(self):
        # Given
        account_id = "ACC123"
        deposit_amount = 50
        original_balance = self.bank_service.get_balance(account_id)

        # When
        self.bank_service.deposit(account_id, deposit_amount)
        updated_balance = self.bank_service.get_balance(account_id)

        # Then
        self.assertEqual(updated_balance, original_balance + deposit_amount)

    def test_deposit_new_account(self):
        # Given
        new_account_id = "ACCNEW"
        deposit_amount = 100

        # When
        self.bank_service.deposit(new_account_id, deposit_amount)
        balance = self.bank_service.get_balance(new_account_id)

        # Then
        self.assertEqual(balance, deposit_amount)

    def test_withdraw_success(self):
        # Given
        account_id = "ACC123"
        withdraw_amount = 50
        original_balance = self.bank_service.get_balance(account_id)

        # When
        result = self.bank_service.withdraw(account_id, withdraw_amount)
        updated_balance = self.bank_service.get_balance(account_id)

        # Then
        self.assertTrue(result)
        self.assertEqual(updated_balance, original_balance - withdraw_amount)

    def test_withdraw_insufficient_funds(self):
        # Given
        account_id = "ACC123"
        original_balance = self.bank_service.get_balance(account_id)
        withdraw_amount = original_balance + 1

        # When
        result = self.bank_service.withdraw(account_id, withdraw_amount)
        updated_balance = self.bank_service.get_balance(account_id)

        # Then
        self.assertFalse(result)
        self.assertEqual(updated_balance, original_balance)

    def test_withdraw_no_account(self):
        # Given
        account_id = "NOTEXIST"
        withdraw_amount = 10

        # When
        result = self.bank_service.withdraw(account_id, withdraw_amount)
        balance = self.bank_service.get_balance(account_id)

        # Then
        self.assertFalse(result)
        self.assertEqual(balance, 0)



if __name__ == '__main__':
    unittest.main()
