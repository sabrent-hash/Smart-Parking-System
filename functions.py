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


def register_vehicle_entry(parking_slots: dict[int, str | None], license_number: str) -> int:
    """
    Register a vehicle entry into the parking system.
    Args:
        parking_slots(dict): All parking slots with key: slot number and value: license number or None if empty.
        license_number(str): The license number of the vehicle entering.
    Returns:
        int: The slot number where the vehicle is parked, or -1 if no slot is available.
    """
    # Comment
    pass


def parking_fee():
    """
    Calculate the parking fee based on the duration of stay.
    Returns:
        float: The calculated parking fee.
    """
    # Comment
    pass


def register_vehicle_exit():
    """
    Register a vehicle exit from the parking system.
    """
    # Comment
    pass
