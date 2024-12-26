import random
class Batsman:
   
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self,name):
        self.__country=name
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,name):
        self.__score=name

    
    def __init__(self,no_of_matches=None):
        self.__no_of_matches=no_of_matches
        self.__name=None
        self.__country=None
        self.__score=[]
        if self.__no_of_matches == None:
            self.__no_of_matches=random.randint(1,95)
            self.__randomScore()
        else:
            self.__randomScore()
    def __randomScore(self):
        
        i=1
        while i <=self.__no_of_matches:

            
            
            num=random.randint(1,10)
            if num<=7:
                self.__score.append(random.randint(0,180))
                
            elif num<=9:
                self.__score.append(random.randint(180,350))
                
            else:
                self.__score.append(random.randint(350,500))
                
           
            i+=1
        
    def caltotal(self):
        total=0
        for i in range (len(self.__score)):
            total+=self.__score[i]
        return total
    def calavg(self):
        to=self.caltotal()
        avg=len(self.__score)
        tavg=to/avg
        return tavg
    def MaxScore(self):
        max=0
        for i in range (len(self.__score)):
            if self.__score[i]>max:
                max=self.__score[i]

        return max
    def cout50(self):
        cout=0
        for i in range (len(self.__score)):
            if self.__score[i]>=50:
                cout+=1
        return cout
    def cout100(self):
        cout=0
        for i in range (len(self.__score)):
            if self.__score[i]>=100:
                cout+=1
        return cout
    def show(self):
        
        print("No of Matches :",self.__no_of_matches)
        print("Score",*self.__score)
        print("Total",self.caltotal())
        print("Average ",self.calavg())
        print("Max Score ",self.MaxScore())
        print("No Of 50s ",self.cout50())
        print("No Of 100s ",self.cout100())
g=[]       
b1=Batsman(5)


g.append(b1)
b2=Batsman(4)
g.append(b2)
b3=Batsman(7)
g.append(b3)


for i in range(len(g)):
    (g[i].show())

    


