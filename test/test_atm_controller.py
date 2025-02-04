import unittest
from unittest.mock import MagicMock
from model.bank_service import BankService
from controller.atm_controller import ATMController

class TestATMController(unittest.TestCase):

    def shortDescription(self):
        # 각 테스트 함수의 docstring(`_testMethodDoc`)을 사용해 출력
        return self._testMethodDoc


    def setUp(self):
        self.mock_bank_service = MagicMock(spec=BankService)
        self.controller = ATMController(self.mock_bank_service)
        self.test_card_number = "1111-2222-3333-4444"
        self.test_pin = "1234"

    def test_insert_card(self):
        """[카드 삽입] 카드 번호가 정상적으로 저장되는지 확인"""
        self.controller.insert_card(self.test_card_number)
        self.assertEqual(self.controller.card_number, self.test_card_number)
        self.assertFalse(self.controller.authorized)

    def test_enter_pin_correct(self):
        """[PIN 검증] 올바른 PIN -> 인증 성공"""
        self.mock_bank_service.verify_pin.return_value = True
        self.controller.insert_card(self.test_card_number)

        result = self.controller.enter_pin(self.test_pin)
        self.assertTrue(result)
        self.assertTrue(self.controller.authorized)
        self.mock_bank_service.verify_pin.assert_called_once_with(
            self.test_card_number, self.test_pin
        )

    def test_enter_pin_incorrect(self):
        """[PIN 검증] 틀린 PIN -> 인증 실패"""
        self.mock_bank_service.verify_pin.return_value = False
        self.controller.insert_card(self.test_card_number)

        result = self.controller.enter_pin(self.test_pin)
        self.assertFalse(result)
        self.assertFalse(self.controller.authorized)


    def test_select_account_success(self):
        """[계좌 선택] 올바른 계좌 선택 성공"""
        self.mock_bank_service.verify_pin.return_value = True
        self.mock_bank_service.get_accounts.return_value = ["ACC123", "ACC456"]

        self.controller.insert_card(self.test_card_number)
        self.controller.enter_pin(self.test_pin)
        self.controller.select_account("ACC123")
        self.assertEqual(self.controller.current_account, "ACC123")

    def test_select_account_failure(self):
        """[계좌 선택] 잘못된 계좌 선택 실패"""
        self.mock_bank_service.verify_pin.return_value = True
        self.mock_bank_service.get_accounts.return_value = ["ACC999"]

        self.controller.insert_card(self.test_card_number)
        self.controller.enter_pin(self.test_pin)
        with self.assertRaises(Exception):
            self.controller.select_account("ACC123")

    def test_check_balance(self):
        """[잔액 조회] 잔액이 정상적으로 조회되는지 확인"""
        self.mock_bank_service.verify_pin.return_value = True
        self.mock_bank_service.get_accounts.return_value = ["ACC123"]
        self.mock_bank_service.get_balance.return_value = 100

        self.controller.insert_card(self.test_card_number)
        self.controller.enter_pin(self.test_pin)
        self.controller.select_account("ACC123")

        balance = self.controller.check_balance()
        self.assertEqual(balance, 100)
        self.mock_bank_service.get_balance.assert_called_once_with("ACC123")

    def test_deposit(self):
        """[입금] 입금이 정상적으로 처리되는지 확인"""
        self.mock_bank_service.verify_pin.return_value = True
        self.mock_bank_service.get_accounts.return_value = ["ACC123"]

        self.controller.insert_card(self.test_card_number)
        self.controller.enter_pin(self.test_pin)
        self.controller.select_account("ACC123")

        self.controller.deposit(50)
        self.mock_bank_service.deposit.assert_called_once_with("ACC123", 50)

    def test_withdraw_success(self):
        """[출금] 출금이 정상적으로 처리되는지 확인"""
        self.mock_bank_service.verify_pin.return_value = True
        self.mock_bank_service.get_accounts.return_value = ["ACC123"]
        self.mock_bank_service.withdraw.return_value = True

        self.controller.insert_card(self.test_card_number)
        self.controller.enter_pin(self.test_pin)
        self.controller.select_account("ACC123")

        result = self.controller.withdraw(40)
        self.assertTrue(result)
        self.mock_bank_service.withdraw.assert_called_once_with("ACC123", 40)

    def test_withdraw_failure(self):
        """[출금] 출금 실패 (잔액 부족)"""
        self.mock_bank_service.verify_pin.return_value = True
        self.mock_bank_service.get_accounts.return_value = ["ACC123"]
        self.mock_bank_service.withdraw.return_value = False

        self.controller.insert_card(self.test_card_number)
        self.controller.enter_pin(self.test_pin)
        self.controller.select_account("ACC123")

        result = self.controller.withdraw(1000)
        self.assertFalse(result)
        self.mock_bank_service.withdraw.assert_called_once_with("ACC123", 1000)


if __name__ == "__main__":
    unittest.main(verbosity=2)