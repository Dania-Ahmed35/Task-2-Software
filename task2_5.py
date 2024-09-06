class robot:
    def __init__(self,name,battery_level):
      self.name=name
      self.battery_level=battery_level

    def status(self):
       print(self.name  + " " + str (self.battery_level))
    
    
    def move(self):
       pass

    def getBatteryLevel(self):
      return self.battery_level
    
    def setBatteryLevel(self,batteryLevel):
       self.battery_level=batteryLevel

class  GroundRobot(robot):
   def __init__(self,name,battery_level,wheels):
      super().__init__(name,battery_level)
      self.wheels=wheels

   def move(self):
      print("This Robot moves on the ground")

 
         
        
class  AerialRobot(robot):
   def __init__(self,name,battery_level,rotors):
      super().__init__(name,battery_level)
      self.rotors=rotors

   def move(self):
      print("This Robot flies") 

class FleetManagement:
   def status(self,robotName):
      robotName.status()


GroundBot = GroundRobot("GroundBot", 95, 4)
AirBot = AerialRobot("AirBot", 90, 6)
Fleet = FleetManagement()
GroundBot.move()
AirBot.move()
Fleet.status(GroundBot)
Fleet.status(AirBot)

     