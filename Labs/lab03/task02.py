class Timespan():
    def __init__ (self,total_mins):
        self.total_mins = total_mins
        
    def show(self):
        hours = self.total_mins // 60
        minute = self.total_mins % 60   
        print(f'{hours} hours and {minute} minutes')
    
    def add_hour(self,hrs):
        self.total_mins = self.total_mins + (hrs*60)
        hours = self.total_mins//60
        
        
    def add_min(self,minute):
        self.total_mins = self.total_mins + minute
        
        
    def change(self,ts):
        self.total_mins = self.total_mins- ts
        print("Minutes:",self.total_mins)
        
        
my_time = Timespan(123)
my_time.show()
my_time.change(15)
