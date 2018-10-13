import datetime 

class MotorBike():
    def __init__(self, brand, max_speed, gear):
        self.brand = brand
        self.max_speed = max_speed
        self.current_speed = 0
        self.current_gear = gear

    def accelerate(self, speed_diff):
        new_speed = self.current_speed + speed_diff
        if new_speed < self.max_speed:
            self.current_speed = new_speed
            return datetime.datetime.now().time()
        else:
            self.current_speed = self.max_speed
            return datetime.datetime.now().time()
        #return self.current_speed

    def get_speed(self):
        return self.current_speed

    def brake(self):
        self.current_speed = self.current_speed - 5
        print("Brake Applied, Your Current Speed is decreased by 5kms ")
        return datetime.datetime.now().time()
        
    def get_gear(self):
        print ("Your Motor bike is currently running on Gear ")
        return self.current_gear

    def change_gear(self, new_gear):
        if new_gear > 5:
            print("Invalid input..Switching back to Previous Gear")
        elif new_gear == 0: 
            print ("Vehicle is in Rest, Please change the Gear to move")
            self.current_gear =new_gear
        else:
            print ("Changed the Gear, Check Current Gear")
            self.current_gear = new_gear
    def Bikestate(self):
        print ("Gear Status",self.current_gear)
        if self.current_gear > 0:
            print ("Bike is in a moving state @ speed",self.current_speed)
        else:
            print("Bike is in Neutral")
    def LastBreak(self):
         print ("Last Break Applied @")

