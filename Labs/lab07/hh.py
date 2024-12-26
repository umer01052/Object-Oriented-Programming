class Bird:
  a=10
  print(a)
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
     
class ostrich(Bird):
    Bird.a*=85
    def flight(self):
        print("Ostriches cannot fly.")
    print(Bird.a)
     
class ost(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
    print(Bird.a)
    

     
obj_bird = Bird()
obj_ost = ostrich()
obj_os=ost()
 
obj_bird.intro()
obj_bird.flight()
 
obj_ost.intro()
obj_ost.flight()
print(ostrich.__dict__)