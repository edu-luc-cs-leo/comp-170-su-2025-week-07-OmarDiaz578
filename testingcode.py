# main.py

from Vehicles import Car, Truck, Motorcycle, Bus
from Ales import PaleAle, IPA, Stout, Porter


def run_vehicle_demo() -> None:
    """
    Create and test different vehicle objects.
    Print their description and fuel usage for a fixed distance.
    """
    print("=== VEHICLE INFO ===")
    print(" ")
    distance: float = 100.0  # Distance in miles

    # List of different vehicles to test
    vehicles = [Car(), Truck(), Motorcycle(), Bus()]

    for vehicle in vehicles:
        print(vehicle.description())  # Description of vehicle
        print(f"Fuel needed for {distance} miles: {vehicle.fuel_needed(distance):.2f} gallons")
        print("-" * 40)


def run_ale_demo() -> None:
    """
    Create and test different ale objects.
    Print their description and alcohol content for a fixed volume.
    """
    print("=== ALE INFO ===")
    print(" ")
    volume: float = 12.0  # Volume in ounces (standard beer size)

    # List of different ales to test
    ales = [PaleAle(), IPA(), Stout(), Porter()]

    for ale in ales:
        print(ale.description())  # Description of ale
        print(f"Alcohol in {volume} oz: {ale.alcohol_content(volume):.2f} oz")
        print("-" * 40)


# Entry point of the program
if __name__ == "__main__":
    run_vehicle_demo()
    run_ale_demo()
