# Different functions for the project
def available_spots(parking_slots: dict[int, str | None]) -> tuple[int, list]:
    """
    Check the number of available parking slots.
    Args:
        parking_slots(dict): All parking slots with key: slot number and value: license number or None if empty.
    Returns:
        tuple:
            int: Number of free parking slots.
            list: List of available slot numbers.
    """
    # Initialize a list to store available slot numbers and a counter for available slots
    available_slots = []
    available_count = 0

    # Loop through the parking slots and count the empty ones
    for slot in parking_slots:
        if parking_slots[slot] is None:
            available_count += 1
            available_slots.append(slot)

    # Return the count of available slots
    return available_count, available_slots


def register_vehicle_entry(parking_slots: dict[int, str | None], license_plate: str) -> int:
    """
    Register a vehicle entry into the parking system.
    """
    # Comment
    pass


def parking_fee(hours: float, hourly_rate: float = 1.5) -> float:
    """
    Calculate the parking fee based on the duration of stay.
    """
    # Comment
    pass


def register_vehicle_exit(parking_slots: dict[int, str | None],
                          license_plate: str,
                          hours: float) -> dict:
    """Frees the spot of the car. Returns {spot: ""} if successful, {} if not."""
    # Error: license plate not found
    if license_plate not in parking_slots.values():
        print(f"Error: license plate {license_plate} not found in the parking.")
        return {}

    # Error: parking fee failed
    if not parking_fee(hours):
        print("Error: parking fee could not be calculated (hours cannot be negative).")
        return {}

    # Free the spot
    for spot, plate in parking_slots.items():
        if plate == license_plate:
            parking_slots[spot] = None
            return {spot: ""}
