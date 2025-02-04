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