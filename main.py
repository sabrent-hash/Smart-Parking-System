from datasets import parking_slots
from functions import register_vehicle_entry, register_vehicle_exit
user = True

if __name__ == "__main__":
    while True:
        plate = input("\nLicense plate (or 'q' to quit): ").strip().upper()

        if plate == "Q":
            print("Goodbye!")
            break

        if plate == "":
            print("Error: License plate cannot be empty.")

        elif plate in parking_slots.values():
            # The car is inside, so this is an EXIT
            hours = float(input("Hours parked: "))
            register_vehicle_exit(parking_slots, plate, hours)

        else:
            # The car is not inside, so this is an ENTRY
            spot = register_vehicle_entry(parking_slots, plate)
            if spot is None:
                print("Sorry, the parking is full.")
            else:
                print(f"Vehicle {plate} assigned to spot {spot}.")
