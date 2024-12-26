class Timespan():
    def __init__ (self,hours,minute):
        self.hours = hours
        self.minute = minute
        
    def show(self):
        print(f'{self.hours} hours and {self.minute} minutes')
    
    def add_hour(self,hrs):
        self.hours = self.hours * 60 + (hrs*60)
        self.hours = self.hours//60
        
    def add_min(self,minute):
        total = self.hours * 60 + self.minute + minute
        self.hours = total // 60
        self.minute = total % 60
        
    def change(self,ts):
        mins = self.hours*60 + self.minute
        mins = mins - ts
        print("Minutes",mins)
        
        
my_time = Timespan(4,35)
my_time.add_min(5)
my_time.show()
my_time.change(15)




              