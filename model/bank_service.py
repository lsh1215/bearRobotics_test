from abc import ABC, abstractmethod

class BankService(ABC):
    @abstractmethod
    def verify_pin(self, card_number: str, pin: str) -> bool:
        """카드 번호와 PIN을 검사."""
        pass