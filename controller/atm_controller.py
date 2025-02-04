class ATMController:
    def __init__(self, bank_service):
        # Model 계층 - BankService
        self.bank_service = bank_service

        # Controller가 관리하는 상태
        self.card_number = None
        self.authorized = False
        self.current_account = None

    def insert_card(self, card_number: str):
        if self.card_number is not None:
            raise Exception("카드가 이미 삽입되어 있습니다")
        self.card_number = card_number
        self.authorized = False
        self.current_account = None

    def enter_pin(self, pin: str) -> bool:
        if not self.card_number:
            raise Exception("카드가 삽입되지 않았습니다")
        pin_correct = self.bank_service.verify_pin(self.card_number, pin)
        self.authorized = pin_correct
        return pin_correct

    def select_account(self, account_id: str):
        if not self.authorized:
            raise Exception("아직 인증되지 않았습니다")

        accounts = self.bank_service.get_accounts(self.card_number)
        if account_id not in accounts:
            raise Exception("잘못된 계좌가 선택되었습니다")

        self.current_account = account_id