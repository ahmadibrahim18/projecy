class menudrivers:
    
    def __init__(self,name,startcity) :
    
        self.workerid = "id00"
        self.name = name
        self.startcity = startcity
    
    def view_drivers():
        for i in driverlist:
            print(driverlist[i],end="\n")

    def add_drivers():
        driver_name = input("enter the driver name:")
        
        driver_startcity = input("enter the driver start city:")
        newdriver = (driver_name,driver_startcity)
        driverlist.append(newdriver)
        


driver1 = menudrivers("max verstappen","akkar")
driverlist=[]


