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