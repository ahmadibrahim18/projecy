class menudrivers:
    
    def __init__(self,name,startcity) :
    
        self.workerid = "id00"
        self.name = name
        self.startcity = startcity
    
    def view_drivers():
        for i in driverlist:
            print(driverlist[i],end="\n")

        
driver1 = menudrivers("max verstappen","akkar")



