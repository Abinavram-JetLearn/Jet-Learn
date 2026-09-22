class Bank():
    def __init__(self, name, age, address, balance, pin, cardnum):
        self.name = name
        self.age = age
        self.__address = address
        self.balance = balance
        self.__pin = pin
        self.__cardnum = cardnum
    def printdetails(self):
        answer = input("Type Print to Print Details: ").lower().strip()
        if answer == "print":
            print(self.name, self.age, self.balance)
        answer = input("Type 'yes' to see secret details?: ").lower().strip()
        if answer == "yes":
            answer2 = input("Type the pin: ").lower()
            if answer2 == self.__pin:
                print(self.__address, self.__cardnum, self.balance)
            else:
                print("wrong pin")
    def pinchange(self):
        answer = input("Type yes to change your pin: ").lower().strip()
        if answer == "yes":
            answer = input("Type old pin: ")
            if answer == self.__pin:
                answer = input("Type new pin: ")
                self.__pin = answer
                print("Pin Reset")
            else:
                print("wrong pin")

# object1 = Bank("Abinavram Anbuprabhu", "81", "S73Y01", "31.81", "123456", "1324 1244 1789 1987")
# object1.pinchange()
