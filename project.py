
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
    
   


# here is the add driver function
    def add_drivers():
        result = True
        #while loop to add another driver
        while result == True:
            driver_name = input("enter the driver name:")
        
            driver_startcity = input("enter the driver start city:")
            # check if the added city by the user is already exist or not 
            for i in cities.citylist:
                if cities.citylist != driver_startcity:
                    user_answer = input("this city is not added , do you want to add it ? :")
                    if user_answer == "yes":
                        # ask the user if he want to add the city to database
                        cities.citylist.append(driver_startcity)
                    else:
                        print("the city will not be added")
            # create an object for a new driver
            newdriver = (driver_name,driver_startcity)

            #add the driver to driver list
            menudrivers.driverlist.append(newdriver)

            # ask the user if he want to add another driver
            answer = input("do you want to add another driver ?")
            if answer == "yes" :
                result = True
                
            else:
                result == False
                print(menudrivers.view_drivers())
        

    
    
    def view_drivers():
        counter = 0
        for i in menudrivers.driverlist:
            #print all the drivers in the list
            print(menudrivers.driverlist[counter],end="\n")
            counter+=1
        



print(menudrivers.add_drivers())
print(menudrivers.view_drivers())


class cities:
    
    def __init__(self,name) :
        self.name = name

    beirut = ("beirut")
    jbeil = ("jbeil")
    akkar = ("akkar")
    zahle =("zahle")

    def add_city(cities city):














