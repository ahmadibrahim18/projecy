
class main:
    def welcome():
        option1 = input("1.to go to the drivers menu:\n2.to go to the cities menu: \n 3.to exit the system:")
        

        if option1 == 1:
            menudrivers
        elif option1 ==2:
            cities_menu
        else:
            exit




class menudrivers:
    driverlist = []
    def __init_subclass__(cls):
        pass
    def __init__(self,name,startcity) :
       counter=0
    
       self.workerid = "id00"+counter
       counter+=1
       self.name = name
       self.startcity = startcity
    
    #function to view drivers


# here is the add driver function
    def add_drivers():
        result = True
        while result == True:
            driver_name = input("enter the driver name:")
        
            driver_startcity = input("enter the driver start city:")
            for i in cities.cities:
                if driver_startcity != driver_startcity:
                    input = input("this city is not added , do you want to add it ? :")
                    if input == "yes":
                        cities.cities.append(driver_startcity)
                    else:
                        print("the city will not be added")
            newdriver = (driver_name,driver_startcity)
            menudrivers.driverlist.append(newdriver)
            answer = input("do you want to add another driver ?")
            if answer == "yes" :
                result = True
                
            else:
                result == False
                print(menudrivers.view_drivers())
        

    
    
    def view_drivers():
        counter = 0
        for i in menudrivers.driverlist:

            print(menudrivers.driverlist[counter],end="\n")
            counter+=1
        



print(menudrivers.add_drivers())
print(menudrivers.view_drivers())


class cities:
    cities = []













