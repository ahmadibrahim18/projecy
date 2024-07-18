import sys

class main:
    def __init__(self):
        self.menu_drivers = menudrivers(self)
        self.cities = cities(self)
    
    def welcome(self):
        option1 = input("1. to go to the drivers menu\n2. to go to the cities menu\n3. to exit the system: ")
        
        if option1 == "1":
            self.menu_drivers.menudriveroption()
        elif option1 == "2":
            self.cities.citiesoption()
        else:
            sys.exit()

class menudrivers:
    driverlist = []
    def __init__(self, main_instance):
        self.main_instance = main_instance
   

    def add_drivers(self):
        result = True
        while result:
            driver_name = input("Enter the driver name: ")
            driver_startcity = input("Enter the driver start city: ")
            
            if driver_startcity not in cities.city_list:
                user_answer = input("This city is not added, do you want to add it? (yes/no): ")
                if user_answer.lower() == "yes":
                    near_city = input("Enter the nearest city: ")
                    cities.add_city(driver_startcity)
                    cities.addEdge(cities.city_graph, driver_startcity, near_city)
                else:
                    print("The city will not be added")
                    continue

            newdriver = (driver_name, driver_startcity)
            menudrivers.driverlist.append(newdriver)

            answer = input("Do you want to add another driver? (yes/no): ")
            if answer == "yes":
                result = True
            else:
                main.welcome
                result = False
                
    
    def view_drivers(self):
        if len(menudrivers.driverlist):
            print("No drivers to show")
        else:
            for driver in menudrivers.driverlist:
                print(driver)
        
    def menudriveroption(self):
        options = input("1. to view all drivers\n2. to add driver\n3. to go back to main menu\n")
        while True:
            

            if options == "1":
                self.view_drivers()
            elif options == "2":
                self.add_drivers()
            elif options == "3":
                self.main_instance.welcome()
              
            else:
                print("Invalid input, Enter 1, 2, or 3.")

class cities:
    city_list = []
    city_graph = {}

    def __init__(self, main_instance):
        self.main_instance = main_instance

    @staticmethod
    def addEdge(adj, main_city, edgecity):
        if main_city in adj:
            adj[main_city].append(edgecity)
        else:
            adj[main_city] = [edgecity]
        
        if edgecity in adj:
            adj[edgecity].append(main_city)
        else:
            adj[edgecity] = [main_city]

    def citiesoption(self):
        answer = input("1. To show cities\n2. Print neighboring cities\n3. Print drivers delivering to city\n")
        while True:
           
        
            if answer == "1":
                self.show_cities()
            elif answer == "2":
                self.neighbor_cities()
            elif answer == "3":
                self.drivers_to_city()
            elif answer == "4":
                self.main_instance.welcome()
            else:
                print("invalid input")
                break

    @staticmethod
    def add_city(city):
        if city not in cities.city_list:
            cities.city_list.append(city)
            cities.city_graph[city] = []
        else:
            print("This city is already added")

    def show_cities(self):
        if not cities.city_list:
            print("No cities to show!")
        else:
            for city in cities.city_list:
                print(city)

    def neighbor_cities(self):
        city = input("Enter the name of the city: ")
        if city in cities.city_graph:
            print(f"The neighbors of {city} are: {cities.city_graph[city]}")
        else:
            print(f"{city} is not in the city list.")

    def drivers_to_city(self):
        city = input("Enter the name of the city: ")
        visited = set()
        driver_to_city = self.deliver_to(visited, cities.city_graph, city)
        if not driver_to_city:
            print(f"No available drivers to {city}")
        else:
            for driver in driver_to_city:
                print(driver)

    @staticmethod
    def deliver_to(visited, graph, city):
        driver_to_city = []
        queue = [city]

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                queue.extend(graph.get(current, []))
                for driver in menudrivers.driverlist:
                    if driver[1] == current:
                        driver_to_city.append(driver)
        return driver_to_city

# Initializing cities
citiess = ["jbeil", "beirut", "akkar", "zahle", "saida"]
objectt = cities(main)
for city in citiess:
    objectt.add_city(city)

cities.addEdge(cities.city_graph, "beirut", "jbeil")
cities.addEdge(cities.city_graph, "jbeil", "akkar")
cities.addEdge(cities.city_graph, "saida", "zahle")
2

if __name__ == "__main__":
    system = main()
    system.welcome()
