class BankAccount(object):
    def __init__(self,AccountName,ATMCardNumber,PinCode,Money):
        self.AccountName = AccountName
        self.ATMCardNumber = ATMCardNumber
        self.PinCode = PinCode
        self.Money = Money
    
    def WithdrawalSmall(self):
        print('You have withdrawn 500₿')
    
    def WithdrawalMedium(self):
        print('You have withdrawn 5000₿')

    def WithdrawalLarge(self):
        print('You have withdrawn 50000₿')

    def DepositSmall(self):
        print('You have deposited 500₿')

    def DepositMedium(self):
        print('You have deposited 5000₿')

    def DepositLarge(self):
        print('You have deposited 50000₿')

    def BalanceEnquiry(self):
        print(self.Money)

Aanandan = BankAccount('AanandanBiswas','8080808212','220921','1000000000000')
Aanandan.BalanceEnquiry()