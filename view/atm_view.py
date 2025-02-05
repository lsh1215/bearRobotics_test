from controller.atm_controller import ATMController
from model.bank_service_impl import BankServiceImpl

class ATMView:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        # 간단한 콘솔 흐름 예시
        while True:
            print("=== ATM ===")
            print("1. Insert Card")
            print("2. Enter PIN")
            print("3. Select Account")
            print("4. Check Balance")
            print("5. Deposit")
            print("6. Withdraw")
            print("7. Exit")

            choice = input("Select menu: ")

            if choice == "1":
                card_number = input("Card number: ")
                try:
                    self.controller.insert_card(card_number)
                    print("Card inserted.")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "2":
                pin = input("PIN: ")
                try:
                    success = self.controller.enter_pin(pin)
                    if success:
                        print("PIN correct.")
                    else:
                        print("PIN incorrect.")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "3":
                account_id = input("Account ID: ")
                try:
                    self.controller.select_account(account_id)
                    print("Account selected.")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "4":
                try:
                    balance = self.controller.check_balance()
                    print(f"Balance: {balance}")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "5":
                amount_str = input("Deposit amount: ")
                try:
                    amount = int(amount_str)
                    self.controller.deposit(amount)
                    print(f"Deposited {amount}")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "6":
                amount_str = input("Withdraw amount: ")
                try:
                    amount = int(amount_str)
                    success = self.controller.withdraw(amount)
                    if success:
                        print(f"Withdrew {amount}")
                    else:
                        print("Withdrawal failed (insufficient funds?)")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "7":
                print("ATM session ended.")
                break

            else:
                print("Invalid selection.")

if __name__ == "__main__":
    bank_service = BankServiceImpl()  # 임의의 Fake 구현체
    controller = ATMController(bank_service)
    atm_view = ATMView(controller)
    atm_view.run()