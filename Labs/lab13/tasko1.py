class NUMBERS:
    def __init__(self):
        self.odd_numbers = []
        self.even_numbers = []

    def add_number(self, number):
        if isinstance(number, (int, float)):
            if number % 2 == 0:
                self.even_numbers.append(number)
            else:
                self.odd_numbers.append(number)
        else:
            print(" Please provide an integer or a float.")

    def delete_number(self, number):
        if number in self.odd_numbers:
            self.odd_numbers.remove(number)
        elif number in self.even_numbers:
            self.even_numbers.remove(number)
        else:
            print("Number not found in the list.")

    def alter_number(self, old_number, new_number):
        self.delete_number(old_number)
        self.add_number(new_number)

    def search_number(self, number):
        
        if number in self.odd_numbers:
            return "Number is present in odd numbers"
        elif number in self.even_numbers:
            return "Number is present in even numbers"
        else:
            return "Number is not present"


    def __iter__(self):
        self.index = 0
        self.numbers = self.odd_numbers + self.even_numbers
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
    def __getitem__(self, index):
        
        if index % 2 == 0 :
            return self.odd_numbers[index // 2] 
        else :
            return self.even_numbers[index // 2]

    def __setitem__(self, index, value):
        if value % 2 == 0:
            self.even_numbers[index // 2] = value
        else:
            self.odd_numbers[index // 2] = value
    



numbers_list = NUMBERS()


numbers_list.add_number(4)
numbers_list.add_number(8)
numbers_list.add_number(4)
numbers_list.add_number(6)


for num in numbers_list:
    print(num)
numbers_list.delete_number(6)


numbers_list.alter_number(8, 10)


print(numbers_list.search_number(4))  
print(numbers_list.search_number(5))  



