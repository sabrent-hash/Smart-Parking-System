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


def register_vehicle_entry(parking_slots: dict[int, str | None], license_plate: str) -> int | None:
    """
    Register a vehicle entry into the parking system.

    Args:
        parking_slots (dict): All parking slots with key: slot number and value: license plate or None if empty.
        license_plate (str): License plate of the entering vehicle.

    Returns:
        int | None: The number of the assigned parking slot, or None if the parking is full.
    """
    # Loop through the parking slots to find the first available one
    for slot_number, plate in parking_slots.items():
        if plate is None:
            parking_slots[slot_number] = license_plate.upper()
            return slot_number

    # Return None if no spaces are available
    return None


"""Parking fee calculation."""
default_price_per_minute = 0.03  # euros per minute


def calculate_fees(parking, price_per_minute=default_price_per_minute):
    """Calculates the payment for each car in the parking lot.

    Args:
        parking: matrix (list of pairs) where each row is [car_id, minutes].
            The same car may appear several times (several stays);
            in that case its payments are added together.
        price_per_minute: price charged for each minute of stay.
    Returns:
        dict with {car_id: total_payment}, rounded to 2 decimals.
    Raises:
        ValueError: if any row is not a pair or the minutes are negative.
    """
    payments = defaultdict(float)

    # Error cases

    for row in parking:
            if not row:  # free spot: None or empty list
                continue

            if len(row) != 2:   # Error in case of a list that is not a pair
                raise ValueError(f"Each row must be a pair [id, minutes]: {row}")

            car_id, minutes = row
            if car_id is None:  # free spot: [None, ...]
                minutes = 0

            if minutes < 0:   #Error in case of a negative number
                raise ValueError(f"Negative minutes for car {car_id}")

            # Calculation of the payment
            payments[car_id] += minutes * price_per_minute

    # Diccionary assembly rounded to two decimals
    return {car_id: round(total, 2) for car_id, total in payments.items()}


def register_vehicle_exit(parking_slots: dict[int, str | None],
                          license_plate: str,
                          hours: float) -> dict[int, str | None]:
    """Frees the car's spot, prints the price and returns the parking."""

    # Error: plate not found
    if license_plate not in parking_slots.values():
        print(f"Error: license plate {license_plate} not found in the parking.")
        return parking_slots

    # Error: negative hours
    if hours < 0:
        print("Error: hours cannot be negative.")
        return parking_slots

    # Calculate the price
    total_price = parking_fee(hours)

    # Free the spot
    for spot, plate in parking_slots.items():
        if plate == license_plate:
            parking_slots[spot] = None
            print(f"Vehicle {license_plate} left spot {spot}. Total price: {total_price} €")
            return parking_slots
