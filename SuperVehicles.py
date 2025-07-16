
#Superclass for vehicles
class Vehicle:
    def __init__(self, name: str, mpg: float):
        """
        - Initialize a vehicle with a name and its fuel efficiency in miles per gallon
        - Parameter(name): Name of the vehicle
        - Parameter mpg: Miles per gallon (fuel efficiency)
        """
        self.name: str = name
        # Stores the vehicle's name
        self.mgp: float = mpg
        # Stores the vehicle's fuel efficiency

    def fuel_needed(self, distance: float) -> float:
        """ 
        - Calculates fuel needed for a given distance.
        - Parameter(distance): Distance in MILES
        - Returns fuel needed in gallons
        """
        return distance / self.mgp
    def description(self) -> str:
        """
        - Returns a description of the vehicle's fuel efficiency.
        - Return: a formatted string
        """

        return f"{self.name} gets {self.mpg} miles per gallon."

# Subclasses for different vehicles
class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__("Car", 30)
        # Calls super().__init__() which calls the parent Vehicles.__init__() 
        # To initialize the base class with "Car" as the name and 30 mpg
            
class Truck(Vehicle):
    def __init__(self) -> None:
        super().__init__("Truck", 15)

class Motorcycle(Vehicle):
    def __init__(self) -> None:
        super().__init__("Motorcycle", 50)
            
class Bus(Vehicle):
    def __init__(self) -> None:
        super().__init__("Bus", 8)









#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 