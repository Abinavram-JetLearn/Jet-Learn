from Bank_Account_Class import Bank
class Student(Bank):
    def __init__(self, name, age, address, balance, pin, cardnum, parent_name, parent_num):
        super().__init__(name, age, address, balance, pin, cardnum)
        self.parent_name = parent_name
        self.parent_num = parent_num
        self.__pin = pin
        self.__address = address
        self.__cardnum = cardnum
    def StudentPrintDetails(self):
        self.printdetails()
        if self.answer3 == self.__pin:
            print(self.parent_name, self.parent_num)
    def StudentPinChange(self):
        self.pinchange()

object1 = Student("Abinavram", 14, "Sm6OI9", 31.76, "123456", "1234 5678 9012 3456", "Bavani", "07927483749")
object1.StudentPinChange()