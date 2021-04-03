class ATM(object):
    def __init__(self,pin,cardNo ):
        self.pin = pin
        self.cardNo = cardNo

    def checkBalance(self):
        print("balance - $500000")

    def withDraw(self,amount):
        wD = 5000000 - amount
        print("remaining amount - " + str(wD))

ram = ATM(1107,'541-345-456')

ram.checkBalance()
amount = int(input("MONEY - "))
ram.withDraw(amount)
