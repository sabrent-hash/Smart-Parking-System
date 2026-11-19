# Copyright (c) 2026 Smart Parking Team (ULPGC)
# Licensed under the MIT License. See LICENSE file for details.
"""Initial data of the Smart Parking System.

The parking has 50 slots. Slots 1 to 35 start occupied by demo cars
(0001BCD, 0002BCD, ...) and slots 36 to 50 start free (None), as in the
worked example of our presentation.
"""

TOTAL_SPOTS = 50       # capacity of the parking
INITIAL_OCCUPIED = 35  # slots occupied at the start

# {slot_number: license_plate or None}
parking_slots: dict[int, str | None] = {
    slot: (f"{slot:04d}BCD" if slot <= INITIAL_OCCUPIED else None)
    for slot in range(1, TOTAL_SPOTS + 1)
}
