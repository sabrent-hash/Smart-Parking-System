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


def register_vehicle_exit(parking_slots: dict[int, str | None], license_plate: str) -> dict[int, str | None]:
    """
    Register a vehicle exit from the parking system.
    """
    # Comment
    pass
