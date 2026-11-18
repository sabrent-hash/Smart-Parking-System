# Copyright (c) 2026 Smart Parking Team (ULPGC)
# Licensed under the MIT License. See LICENSE file for details.
"""Smart Parking System - main program.

Interactive program that connects the four team functions: the user
types a license plate; if the car is not inside it is an ENTRY
(register_vehicle_entry), and if it is inside it is an EXIT
(register_vehicle_exit, which uses calculate_fees to print the price).
After every operation the free slots are shown with available_spots,
and when the user quits, the income of the day is shown.
Run it with: python main.py  (type 'q' to quit).
"""
from parking_data import parking_slots  # CHANGED: "datasets" -> "parking_data"
from functions import (PLATE_PATTERN, available_spots, calculate_fees,
                       register_vehicle_entry, register_vehicle_exit)
# CHANGED: removed "user = True" (it was never used)


def clean_plate(text: str) -> str:
    """Cleans a license plate typed by the user.

    Uses the same format as the team functions: no spaces, no hyphens
    and uppercase letters ("8492-lmp" -> "8492LMP").

    Args:
        text: Plate as typed by the user.

    Returns:
        The clean plate.
    """
    return text.strip().upper().replace(" ", "").replace("-", "")


def show_status(parking_slots: dict[int, str | None]) -> None:
    """Prints how many slots are free, using Alfred's available_spots().

    Args:
        parking_slots: All parking slots {slot number: plate or None}.
    """
    free_count, _ = available_spots(parking_slots)
    print(f"Total: {len(parking_slots)} | Occupied: {len(parking_slots) - free_count}"
          f" | Available: {free_count}")


def ask_hours() -> float | None:
    """Asks how many hours the car was parked and checks the answer.

    Steps:
        1. Read the text typed by the user.
        2. Accept "2.5" and also "2,5" (Spanish decimal comma).
        3. If it is not a number, print an error and return None.

    Returns:
        The hours as a float, or None if the input is not a number.
    """
    text = input("Hours parked (e.g. 2.5): ").strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:  # CHANGED: before, a wrong number crashed the program
        print("Error: hours must be a number, e.g. 2.5")
        return None


def print_daily_report(stays_log: list[list]) -> None:
    """Prints how much each car paid and the total income of the day.

    Rubén's calculate_fees() adds together all the stays of the same
    car, so a car that parked twice appears once with its total.

    Args:
        stays_log: Finished stays as [plate, minutes] rows.
    """
    print("\n--- Daily report ---")
    if not stays_log:
        print("No car has left the parking yet. Income: 0.00 €")
        return
    totals = calculate_fees(stays_log)
    for plate, total in totals.items():
        print(f"  {plate}: {total:.2f} €")
    print(f"  TOTAL INCOME: {sum(totals.values()):.2f} €")


def main() -> None:
    """Runs the parking until the user types 'q'.

    Steps:
        1. Show the instructions and the initial state of the parking.
        2. Ask for a license plate ('q' to quit) and check its format
           (4 digits + 3 letters). Wrong plates are rejected here, both
           for entries and exits.
        3. If the car is inside -> EXIT: ask the hours and call Nahún's
           register_vehicle_exit(), which prints the price using Rubén's
           calculate_fees(). The stay is saved for the daily report.
        4. If the car is not inside -> ENTRY: call Cristo's
           register_vehicle_entry() (which uses Alfred's available_spots()).
        5. Show the new state and repeat.
        6. When the user quits, print the daily report.
    """
    stays_log: list[list] = []  # finished stays [plate, minutes]

    # Step 1: instructions and initial state
    print("=== SMART PARKING SYSTEM ===")
    print("Type a NEW plate to ENTER, or a plate that is INSIDE to EXIT and pay.")
    print("Plate format: 4 digits + 3 letters (e.g. 8492LMP).")
    show_status(parking_slots)

    while True:
        # Step 2: read the plate
        plate = clean_plate(input("\nLicense plate (or 'q' to quit): "))

        if plate == "Q":
            # Step 6: daily report
            print_daily_report(stays_log)
            print("Goodbye!")
            break

        if plate == "":
            print("Error: License plate cannot be empty.")
            continue

        # CHANGED: the format is checked here too, for ENTRIES and EXITS
        if not PLATE_PATTERN.match(plate):
            print(f"Error: Invalid license plate '{plate}'. "
                  "Use 4 digits + 3 letters, e.g. 8492LMP.")
            continue

        if plate in parking_slots.values():
            # Step 3: the car is inside, so this is an EXIT
            print(f"Vehicle {plate} is inside -> EXIT")
            hours = ask_hours()
            if hours is None:
                continue
            register_vehicle_exit(parking_slots, plate, hours)
            if plate not in parking_slots.values():  # the exit was correct
                stays_log.append([plate, hours * 60])
        else:
            # Step 4: the car is not inside, so this is an ENTRY
            try:
                spot = register_vehicle_entry(parking_slots, plate)
            except ValueError as error:
                print(f"Error: {error}")
                continue
            if spot is None:
                print("Sorry, the parking is full.")
            else:
                print(f"Vehicle {plate} assigned to spot {spot}. "
                      f"(Type {plate} again when it leaves.)")

        # Step 5: new state of the parking
        show_status(parking_slots)


if __name__ == "__main__":
    main()
