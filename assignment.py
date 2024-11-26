class Smartphone:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def myphone(self):
        print("This are my phone " + self.brand + self.model)
Apple = Smartphone("iphone", "Xseries") 
Samsung = Smartphone("Samsung", "Sxeries")
Techno = Smartphone("HOT","Phantom")

Apple.myphone()
Samsung.myphone()
Techno.myphone()




class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Toyota", "Camry")       
boat1 = Boat("Spain", "Sailing") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
        