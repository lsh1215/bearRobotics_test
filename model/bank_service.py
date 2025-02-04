from abc import ABC, abstractmethod

class BankService(ABC):
    @abstractmethod
    def verify_pin(self, card_number: str, pin: str) -> bool:
        """카드 번호와 PIN을 검사."""
        pass

    @abstractmethod
    def get_accounts(self, card_number: str) -> list:
        """카드 번호로 조회 가능한 계좌 목록을 반환"""
        pass

    @abstractmethod
    def get_balance(self, account_id: str) -> int:
        """계좌 잔액을 반환"""
        pass

    @abstractmethod
    def deposit(self, account_id: str, amount: int):
        """계좌에 amount만큼 입금"""
        pass

    @abstractmethod
    def withdraw(self, account_id: str, amount: int) -> bool:
        """
        계좌에서 amount만큼 출금
        출금 성공 시 True, 실패 시 False
        """
        pass