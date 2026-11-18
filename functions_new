# Copyright (c) 2026 Smart Parking Team (ULPGC)
# Licensed under the MIT License. See LICENSE file for details.
"""Functions of the Smart Parking System.

Each team member is responsible for one function: Alfred checks the
available spots, Cristo registers the entries, Rubén calculates the
fees and Nahún registers the exits. All of them share the same data
format: parking_slots = {spot_number: license_plate or None}.
"""
import re  # CHANGED: needed to check the license plate format
from collections import defaultdict  # CHANGED: missing import (calculate_fees crashed)

# Spanish license plate format: 4 digits + 3 letters (e.g. 8492LMP)
PLATE_PATTERN = re.compile(r"^[0-9]{4}[A-Z]{3}$")


# =====================================================================
# ALFRED - available_spots()
# =====================================================================
def available_spots(parking_slots: dict[int, str | None]) -> tuple[int, list[int]]:
    """Checks the number of available parking slots.

    Steps:
        1. Create an empty list and a counter for the free slots.
        2. Go through every slot of the parking.
        3. If a slot is empty (None), add it to the list and count it.
        4. Return the counter and the list of free slots.

    Args:
        parking_slots: All parking slots, with key: slot number and
            value: license plate, or None if the slot is empty.

    Returns:
        A tuple (number of free slots, list of free slot numbers).
        (0, []) means that the parking is full.

    Example:
        >>> available_spots({1: "1234BCD", 2: None, 3: None})
        (2, [2, 3])
    """
    # Step 1: list of free slot numbers and counter of free slots
    available_slots = []
    available_count = 0

    # Steps 2 and 3: loop through the parking slots and count the empty ones
    for slot in parking_slots:
        if parking_slots[slot] is None:
            available_count += 1
            available_slots.append(slot)

    # Step 4: return the count and the list of free slots
    # CHANGED: comment fixed (it returns the count AND the list)
    return available_count, available_slots


# =====================================================================
# CRISTO - register_vehicle_entry()
# =====================================================================
def register_vehicle_entry(parking_slots: dict[int, str | None],
                           license_plate: str) -> int | None:
    """Registers a vehicle entry and assigns it the lowest free slot.

    Steps:
        1. Clean the license plate (remove spaces and hyphens, use uppercase).
        2. Check that the plate is not empty, that it has the Spanish
           format (4 digits + 3 letters, e.g. 8492LMP) and that the car
           is not already inside the parking.
        3. Ask Alfred's available_spots() for the free slots.
        4. If there are no free slots, return None (parking full).
        5. Assign the lowest free slot to the car and return its number.

    Args:
        parking_slots: All parking slots, with key: slot number and
            value: license plate, or None if the slot is empty.
            It is modified in place when the car gets a slot.
        license_plate: License plate of the entering vehicle.

    Returns:
        The number of the assigned parking slot, or None if the
        parking is full.

    Raises:
        ValueError: If the plate is empty, has a wrong format or the car
            is already inside.

    Example:
        >>> slots = {1: "1234BCD", 2: None, 3: None}
        >>> register_vehicle_entry(slots, "8492lmp")
        2
    """
    # Step 1: clean the plate ("8492-lmp" -> "8492LMP")
    plate = license_plate.strip().upper().replace(" ", "").replace("-", "")

    # Step 2: validations  # CHANGED: added (empty plate, format and duplicates)
    if plate == "":
        raise ValueError("License plate cannot be empty.")
    if not PLATE_PATTERN.match(plate):
        raise ValueError(f"Invalid license plate '{plate}'. "
                         "Use 4 digits + 3 letters, e.g. 8492LMP.")
    if plate in parking_slots.values():
        raise ValueError(f"Vehicle {plate} is already inside the parking.")

    # Step 3: use Alfred's function to get the free slots
    # CHANGED: now uses available_spots() so both functions are connected
    free_count, free_slots = available_spots(parking_slots)

    # Step 4: parking full
    if free_count == 0:
        return None

    # Step 5: assign the lowest free slot
    slot_number = min(free_slots)
    parking_slots[slot_number] = plate
    return slot_number


# =====================================================================
# RUBÉN - calculate_fees()
# =====================================================================
default_price_per_minute = 0.03  # euros per minute


def calculate_fees(parking: list[list],
                   price_per_minute: float = default_price_per_minute
                   ) -> dict[str, float]:  # CHANGED: type hints added
    """Calculates the payment for each car in the parking lot.

    Steps:
        1. Go through every row [car_id, minutes].
        2. Skip empty rows and reject rows that are not pairs.
        3. Reject negative minutes.
        4. Add minutes x price to the total of that car (the same car
           can appear several times: several stays).
        5. Return every total rounded to 2 decimals.

    Args:
        parking: matrix (list of pairs) where each row is [car_id, minutes].
            The same car may appear several times (several stays);
            in that case its payments are added together.
        price_per_minute: price charged for each minute of stay.

    Returns:
        dict with {car_id: total_payment}, rounded to 2 decimals.

    Raises:
        ValueError: if any row is not a pair or the minutes are negative.

    Example:
        >>> calculate_fees([["8492LMP", 150]])
        {'8492LMP': 4.5}
    """
    payments = defaultdict(float)

    # Step 1: go through every row  # CHANGED: indentation fixed (4 spaces, was 12)
    for row in parking:
        # Step 2: error cases
        if not row:  # free spot: None or empty list
            continue

        if len(row) != 2:   # Error in case of a list that is not a pair
            raise ValueError(f"Each row must be a pair [id, minutes]: {row}")

        car_id, minutes = row
        if car_id is None:  # free spot: [None, ...]
            minutes = 0

        # Step 3: negative minutes
        if minutes < 0:   # Error in case of a negative number
            raise ValueError(f"Negative minutes for car {car_id}")

        # Step 4: calculation of the payment
        payments[car_id] += minutes * price_per_minute

    # Step 5: dictionary assembly rounded to two decimals  # CHANGED: typo "Diccionary"
    return {car_id: round(total, 2) for car_id, total in payments.items()}


# =====================================================================
# NAHÚN - register_vehicle_exit()
# =====================================================================
def register_vehicle_exit(parking_slots: dict[int, str | None],
                          license_plate: str,
                          hours: float) -> dict[int, str | None]:
    """Frees the car's spot, prints the price and returns the parking.

    Steps:
        1. Clean the license plate (remove spaces and hyphens, use uppercase).
        2. Check that the car is in the parking and that the hours
           are not negative.
        3. Convert the hours to minutes and get the price with
           Rubén's calculate_fees().
        4. Find the car's slot, free it and print the receipt.

    Args:
        parking_slots: All parking slots, with key: slot number and
            value: license plate, or None if the slot is empty.
        license_plate: License plate of the vehicle that is leaving.
        hours: Time parked, in decimal hours (2.5 = 2 h 30 min).

    Returns:
        The updated parking_slots (the car's slot is set to None).
        If there is an error, the parking is returned unchanged.

    Example:
        >>> register_vehicle_exit({36: "8492LMP"}, "8492LMP", 2.5)
        Vehicle 8492LMP left spot 36. Total price: 4.50 €
        {36: None}
    """
    # Step 1: clean the plate  # CHANGED: same format as the entry
    license_plate = license_plate.strip().upper().replace(" ", "").replace("-", "")

    # Step 2: error cases
    # Error: plate not found
    if license_plate not in parking_slots.values():
        print(f"Error: license plate {license_plate} not found in the parking.")
        return parking_slots

    # Error: negative hours
    if hours < 0:
        print("Error: hours cannot be negative.")
        return parking_slots

    # Step 3: calculate the price
    # CHANGED: parking_fee() did not exist. Rubén's calculate_fees() uses minutes.
    total_price = calculate_fees([[license_plate, hours * 60]])[license_plate]

    # Step 4: free the spot
    for spot, plate in parking_slots.items():
        if plate == license_plate:
            parking_slots[spot] = None
            # CHANGED: :.2f so the price always has 2 decimals (4.50 €)
            print(f"Vehicle {license_plate} left spot {spot}. Total price: {total_price:.2f} €")
            return parking_slots
