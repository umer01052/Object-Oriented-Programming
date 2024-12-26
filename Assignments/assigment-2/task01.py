class Date:
    def __init__(self, date):
        self.day, self.month, self.year = map(int, date.split('-'))
        

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if value > 31:
            print("write valid date  day is not greater than 31")
        else:
            self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if value > 12:
            print("write valid date month is not greater than 12")
        elif value == 2 and self._day > 28:
            print("write valid date feb is of 28 ")
        elif value in [4, 6, 9, 11] and self._day > 30:
           print("write valid date  4,6,9,11 is of 30 days day is not in range ")
        elif self._day > 31:
            print("write valid date")
        else:
            self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < 1000:
            print("write valid date year must be in 4 digit")
        else:
            self._year = value

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def __str__(self):
        return f"{self.street}, {self.city}"

class Item:
    def __init__(self, name, rate, quantity):
        self.name = name
        self.rate = rate
        self.quantity = quantity

    def get_amount(self):
        return self.rate * self.quantity

class Bill:
    def __init__(self, date, customer_name, customer_address,sig):
        self.date = date
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.sig=sig
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_amount()
        return total
    def generate_bill(self):
        print("MOBILO")
        print("Mobile City")
        print("Deals in all kinds of Mobile sets and Accessories")
        print("Cell No: 0321-0008000")
        print("CASHMENO")
        print("No: 2")
        print(f"Date: {self.date}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Customer Address: {self.customer_address}\n")
        print("Particulars                Rate    Qty      Amount")
        print("_" * 50)

        for item in self.items:
            print(f"{item.name.ljust(25)}   {str(item.rate).ljust(6)}  {str(item.quantity).ljust(7)}  {item.get_amount()}")
        
        print("_" * 50)
        print(f"Total \t\t\t\t\t     {self.calculate_total()}\n")
        print("Signature:",self.sig)
        print("Adress: Basement # 2, Allahwala Plaza, Markaz K8, lahore")


date = Date('31-12-2023')
address = Address("C-1 House No 52 ", "Wapda Town GujranwaLA")

bill = Bill(date, "Haider", address,"umer")
bill.add_item(Item("Hand free", 10, 2))
bill.add_item(Item("Mouse", 15, 2))
bill.add_item(Item("keyboard", 5, 4))

bill.generate_bill()
