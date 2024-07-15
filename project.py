
class main:
    def welcome():
        option1 = input("1.to go to the drivers menu:")
        option2 = input("2.to go to the cities menu:")
        option3 = input("3.to exit the system:")



class menudrivers:
    
    def __init_subclass__(cls):
        pass
    def __init__(self,name,startcity) :
    
       self.workerid = "id00"
       self.name = name
       self.startcity = startcity
    
    #function to view drivers


# here is the add driver function
    def add_drivers():
        
        driver_name = input("enter the driver name:")
        
        driver_startcity = input("enter the driver start city:")
        newdriver = (driver_name,driver_startcity)
        driverlist.append(newdriver)
    
    
    def view_drivers():
        for i in driverlist:
            print(driverlist[i],end="\n")
        



print(menudrivers.add_drivers())
print(menudrivers.view_drivers())





