"""Parking fee calculation."""
from collections import defaultdict

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



if __name__ == "__main__":
    parking = [
        [101, 45], [102, 120], [103, 15], [101, 30],
        [105, 60], [106, 180], [107, 77], [108, 10]
    ]
    print(calculate_fees(parking))
