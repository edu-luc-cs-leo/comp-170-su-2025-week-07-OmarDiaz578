#Superclass for Ales
class Ales:
    def __init__(self, name: str, abv: float) -> None:
        """
        - Initializes ales with a name and abv
        - Parameter name: Name of the ale
        - Parameter abv: Alcohol by volume
        """
        self.name: str = name
        self.abv: float = abv
    def alcohol_content(self, volume_in_oz: float) -> float:
        """
        - Calculates the amount of alcohol in a given volume of the ale
        - Parameter volume_in_oz: Volume of drink in ounces
        - Return: Alcohol content in ounces
        """
        return self.abv * volume_in_oz
    def description(self) -> str:
       # Returns a formatted string with ale name and ABV percentage
       # Converts decimal ABV to percentage and formats it to 1 decimal place
        return f"{self.name}: {self.abv * 100:.1f}% ABV"
    
    
#Subclasses for ales
class PaleAle(Ales):
    def __init__(self) -> None:
        super().__init__("Pale Ale", 0.055)

class IPA(Ales):
    def __init__(self) -> None:
        super().__init__("IPA", 0.065)

class Stout(Ales):
    def __init__(self) -> None:
        super().__init__("Stout", 0.07)

class Porter(Ales):
    def __init__(self) -> None:
        super().__init__("Porter", 0.06)



#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 