import sys

class main:
    def __init__(self):
        self.menu_drivers = MenuDrivers()
        self.cities = Cities()
    
    def welcome(self):
        option1 = input("1.to go to the drivers menu:  2.to go to the cities menu:   3.to exit the system:")
        

        if option1 == "1":
          self.menudriveroption()
        elif option1 =="2":
             self.citiesoption()
        else:
            sys.exit()





#"""""
class menudrivers:
    driverlist = []
   

    # CONSTRUCTOR FOR DRIVER
    def __init__(self,name,startcity) :
       counter=0
    
       self.workerid = "id00"+counter
       counter+=1
       self.name = name
       self.startcity = startcity

    driver1 = ("max verstapen","jbeil")
# LET THE USER CHOOSE THE FUNCTION HE WANT 






# here is the add driver function
    def add_drivers(self):
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
                        
                        near_city = input("enter the nearest city :")
                        # ask the user if he want to add the city to database
                        
                        cities.citylist.append(driver_startcity)
                        
                        return cities.addEdge(cities.city_list,driver_startcity,near_city)
                    
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
               # print(menudrivers.view_drivers())
        

    
    
    def view_drivers(self):
        if len(menudrivers.driverlist) == 0:
            print("no drivers to show")
        counter = 0
        for i in menudrivers.driverlist:
            #print all the drivers in the list
            print(menudrivers.driverlist[counter],end="\n")
            counter+=1
        
    def menudriveroption(self):
        options = input("1. to view all drivers \n 2.to add driver \n 3.to go back to main menu")

        if options == 1 :
            self.add_drivers
        elif options ==2:
            self.view_drivers
        elif options == 3:
            sys.exit
        else:
            print("invalid input, Enter 1,2,3 .")

class cities:
    city_list = []
    city_graph = {}
    def __init__(self,name) :
        self.name = name

    beirut = ("beirut")
    jbeil = ("jbeil")
    akkar = ("akkar")
    zahle =("zahle")
    saida = ("saida")
    def addEdge(adj, main_city, edgecity):

        adj[main_city].append(edgecity)
        adj[edgecity].append(main_city)

    def citiesoption():
        answer = input("1. To Show Cities \n 2.Print Neighboring Cities \n 3.Print Drivers delivering to City")

        if answer == "1":
            return cities.showcities()
        elif answer == "2":
            return cities.neighbor_cities()
        elif answer =="3":
            return cities.drivers_to_city()
        else:
            print("invalid input")

    def add_city(city):
        for i in cities.city_list:
            if city not in cities.city_list:
        
                cities.city_list.append(city)
            else:
                print("this city is already added")

    def show_cities():
        for i in cities.citylist:
            print(i)







#"""

        
    

















