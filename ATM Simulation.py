class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []
        self.add_transaction("Account created", initial_balance)
    def add_transaction(self, type, amount):
        self.transactions.append({
            'type': type,
            'amount': amount,
            'balance': self.balance
        })
    def check_balance(self):
        print("\n" + "=" * 40)
        print(f"💰 Your current balance is: ${self.balance:.2f}")
        print("=" * 40)
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            print("\n" + "=" * 40)
            print(f"✅ Successfully deposited ₹{amount:.2f}")
            print(f"💰 New balance: ${self.balance:.2f}")
            print("=" * 40)
            return True
        else:
            print("\n❌ Invalid amount! Please enter a positive number.")
            return False
    def withdraw(self, amount):
        if amount <= 0:
            print("\n❌ Invalid amount! Please enter a positive number.")
            return False
        elif amount > self.balance:
            print("\n" + "=" * 40)
            print(f"❌ Insufficient balance!")
            print(f"   Requested: ${amount:.2f}")
            print(f"   Available: ${self.balance:.2f}")
            print("=" * 40)
            return False
        else:
            self.balance -= amount
            self.add_transaction("Withdrawal", amount)
            print("\n" + "=" * 40)
            print(f"✅ Successfully withdrew ₹{amount:.2f}")
            print(f"💰 New balance: ₹{self.balance:.2f}")
            print("=" * 40)
            return True
    def show_transactions(self):
        if not self.transactions:
            print("\n📭 No transactions yet.")
            return
        print("\n" + "=" * 50)
        print("📋 TRANSACTION HISTORY")
        print("=" * 50)
        for i, trans in enumerate(self.transactions, 1):
            print(f"{i}. {trans['type']:15} ₹{trans['amount']:10.2f} | Balance: ₹{trans['balance']:.2f}")
        print("=" * 50)
class ATMController:
    def __init__(self):
        self.atm = ATM(1000)  
        self.running = True
    def display_menu(self):
        print("\n" + "🏦" * 15)
        print("     WELCOME TO ATM SIMULATION")
        print("🏦" * 15)
        print("\n📋 MENU:")
        print("   1. Check Balance")
        print("   2. Deposit Money")
        print("   3. Withdraw Money")
        print("   4. Transaction History")
        print("   5. Exit")
        print("-" * 30)
    def get_amount(self, action):
        try:
            amount = float(input(f"💰 Enter amount to {action}: ₹"))
            return amount
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            return -1
    def run(self):
        print("\n🏦 ATM System Initialized 🏦")
        print("Your account has been created with ₹1000")
        while self.running:
            self.display_menu()  
            choice = input("\n🔢 Choose an option (1-5): ").strip()    
            if choice == '1':
                self.atm.check_balance()        
            elif choice == '2':
                amount = self.get_amount("deposit")
                if amount > 0:
                    self.atm.deposit(amount)
                elif amount != -1:
                    print("❌ Deposit amount must be positive!")              
            elif choice == '3':
                amount = self.get_amount("withdraw")
                if amount > 0:
                    self.atm.withdraw(amount)
                elif amount != -1:
                    print("❌ Withdrawal amount must be positive!")     
            elif choice == '4':
                self.atm.show_transactions() 
            elif choice == '5':
                print("\n" + "=" * 40)
                print("👋 Thank you for using our ATM!")
                print(f"   Final balance: ${self.atm.balance:.2f}")
                print("   Have a great day!")
                print("=" * 40)
                self.running = False    
            else:
                print("❌ Invalid choice! Please select 1-5.")
            if self.running:
                input("\n⏎ Press Enter to continue...")

if __name__ == "__main__":
    try:
        atm_system = ATMController()
        atm_system.run()
    except KeyboardInterrupt:
        print("\n\n👋 ATM session interrupted. Goodbye!")