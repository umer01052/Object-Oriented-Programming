class Employee(object):
    def __init__(self,e_no,name,cnic,phone,address):
        self.e_no=e_no
        self.name=name
        self.cnic=cnic
        self.phone=phone
        self.address=address
    def __str__(self) :
        s=f"Empoly.No: {self.e_no}\nName:{self.name}\nCnic:{self.cnic}\nPhoneNO:{self.phone}\nAddress:{self.address}\n"
        return s
class salaried(Employee):
    def __init__(self,e_no,name,cnic,phone,address,w_salary,no_of_weeks):
        self.w_salary=w_salary
        self.no_of_weeks=no_of_weeks
        super().__init__(e_no,name,cnic,phone,address)
    def calsalary(self,):
        total_salary=self.w_salary*self.no_of_weeks
        return total_salary
    def __str__(self):
        s=super().__str__() +f"Total Salary: {self.calsalary()}"
        return s
        
         
class hourEmp(Employee):
    def __init__(self,e_no,name,cnic,phone,address,h_salary,no_of_hours):
        self.h_salary=h_salary
        self.no_of_hours=no_of_hours
        super().__init__(e_no,name,cnic,phone,address)
    def calsalary(self):
        total_salary=self.h_salary*self.no_of_hours
        return total_salary
    def __str__(self):
        s=super().__str__() + f"total Salary :{self.calsalary()}"
        return s
class comEmp(Employee):
    def __init__(self,e_no,name,cnic,phone,address,percentage,no_of_saletotl):
        self.no_of_saletotl=no_of_saletotl
        self.percentage=percentage
        super().__init__(e_no,name,cnic,phone,address)
    def calsalary(self):
        total_salary=self.percentage*self.no_of_saletotl
        return total_salary
    def __str__(self):
        s=super().__str__() + f"TOtal Salary: {self.calsalary()}"
        return s
class payroll:
    
    def __init__(self,object1,object2,object3):
        self.list=[]
        self.list.append(object1)
        self.list.append(object2)
        self.list.append(object3)
    def len(self):
        return self.list
    
        
            
        

        

a=hourEmp("1","umer","34101555","030264855","LAhore",1000,10)
b=comEmp("2","ali","34101555","030264855","Gujranwla",20,100)
c=salaried("3","saad","34101555","030264855","Hyderabad",5000,20)
g=payroll(a,b,c)
a=g.len()
for i in range (len(a)):
    print(a[i])

class Department:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    
        

        

    
        
        
            
