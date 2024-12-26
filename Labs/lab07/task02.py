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
    def __init__(self,e_no,name,cnic,phone,address,w_salary,no_of_weeks,dep):
        self.w_salary=w_salary
        self.no_of_weeks=no_of_weeks
        self.dep=dep
        super().__init__(e_no,name,cnic,phone,address)
    def calsalary(self):
        total_salary=self.w_salary*self.no_of_weeks
        return total_salary
    def __str__(self):
        s=super().__str__() + f"TOtal Salary: {self.calsalary()}"+f"\nand his department is {self.dep}"
        
        return s
        
         
class hourEmp(Employee):
    def __init__(self,e_no,name,cnic,phone,address,h_salary,no_of_hours,dep):
        self.h_salary=h_salary
        self.no_of_hours=no_of_hours
        self.dep=dep
        super().__init__(e_no,name,cnic,phone,address)
    def calsalary(self):
        total_salary=self.h_salary*self.no_of_hours
        return total_salary
    def __str__(self):
        s=super().__str__()+ f"TOtal Salary: {self.calsalary()}"+ f"\nand his department is {self.dep}"
        return s
class comEmp(Employee):
    def __init__(self,e_no,name,cnic,phone,address,percentage,no_of_saletotl,dep):
        self.no_of_saletotl=no_of_saletotl
        self.percentage=percentage
        self.dep=dep
        super().__init__(e_no,name,cnic,phone,address,)
    def calsalary(self):
        total_salary=self.percentage*self.no_of_saletotl
        return total_salary
    def __str__(self):
        s=super().__str__()+ f"TOtal Salary: {self.calsalary()}" +f"\nand his department is {self.dep}"
        return s
class payroll:
    
    def __init__(self,object1,object2,object3):
        self.list=[]
        self.list.append(object1)
        self.list.append(object2)
        self.list.append(object3)
    def len(self):
        return self.list
class Department:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def __str__(self) :
        s=f"{self.name} and city is {self.location}"
        return s
    
        
            
a1=Department("HOur","Lahore")     
a2=Department("sales","qasoor")   
a3=Department("weekly","sultanpoora")    

        

a=hourEmp("1","umer","34101555","030264855","LAhore",1000,5,a1)
b=comEmp("2","ali","34101555","030264855","Qasoor",20,56,a2)
c=salaried("1","saad","34101555","030264855","Sultan poorA",1000,6,a3)
g=payroll(a,b,c)
a=g.len()
for i in range (len(a)):
    print(a[i])


        