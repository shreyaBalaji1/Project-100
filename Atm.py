class AtmClass (object) :
    def __init__(self, cardNumber, pinNumber) :
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def cashWithdrawal(self) :
        print("Cash has been withdrawn")

    def balanceEnquiry(self) :
        print("Your balance is $8000")
    
    def cashDeposit(self) :
        print("Cash has been deposited")
  
    def transferCash(self) :
        print("Cash has been transferred")

atm1 = AtmClass(3473387284234327, 4837)
atm1.cashWithdrawal()
atm1.balanceEnquiry()
atm1.cashDeposit()
atm1.transferCash()


