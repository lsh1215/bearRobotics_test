from model.bank_service import BankService

class BankServiceImpl(BankService):
    def __init__(self):
        # 카드 번호 -> PIN
        self.pin_db = {
            "1111-2222-3333-4444": "1234"
        }
        # 카드 번호 -> 연결된 계좌 목록
        self.accounts_db = {
            "1111-2222-3333-4444": ["ACC123", "ACC456"]
        }
        # 계좌 -> 잔액
        self.balances = {
            "ACC123": 100,
            "ACC456": 50
        }

    def verify_pin(self, card_number: str, pin: str) -> bool:
        correct_pin = self.pin_db.get(card_number, None)
        return (correct_pin is not None) and (correct_pin == pin)

    def get_accounts(self, card_number: str) -> list:
        return self.accounts_db.get(card_number, [])

    def get_balance(self, account_id: str) -> int:
        return self.balances.get(account_id, 0)

