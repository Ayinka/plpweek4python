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

car = Car("Toyota", "Camry")       
boat = Boat("Spain", "Sailing") 
plane = Plane("Boeing", "747")     


car.move()
boat.move()
plane.move()
# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()
        