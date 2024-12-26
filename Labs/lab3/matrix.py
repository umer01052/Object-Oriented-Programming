import random

class Matrix():
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.data = [[random.randint(0, 9) for j in range(self.cols)] for i in range(self.rows)]
    def __str__(self) :
       
        result = ""
        for i in range (self.rows):
           for j in range(self.cols):
               result=result+str(self.data[i][j])
               result=result+" "
           result=result+"\n"
        return result
    def trans(self):
        result=""
        for i in range (self.cols):
            for j in range (self.rows):
                result=result+str(self.data[j][i])
                result=result+" "
            result=result+"\n"
        return result
    def add(self,other):
        result=""
        for i in range (self.rows):
            for j in range (self.cols):
                result=result+str(self.data[i][j]+other.data[i][j])
                result=result+" "
            result=result+"\n"
        return result
    def negate(self):
        result=""
        for i in range (self.rows):
            for j in range (self.cols):
                result=result+str(-self.data[i][j])
                result=result+" "
            result=result+"\n"
        return result
    def set_value(self,rows,cols,value):
        self.data[rows][cols]=value
    def get_value(self,rows,cols):
        return self.data[rows][cols]
          
        
c=Matrix(5,3)
c1=Matrix(5,3)

print(c)
c.set_value(2,1,10)
print(c.get_value(2,1))
print(c)
