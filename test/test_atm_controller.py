import unittest
from unittest.mock import MagicMock

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