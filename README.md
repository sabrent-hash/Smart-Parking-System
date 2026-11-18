# 🚗 Smart Parking System

**Automated capacity tracking, spot assignment and fee calculation in Python.**

Manual parking management causes delays, confusion and billing errors. This lightweight, modular program automates the whole parking lifecycle: it checks the free slots in real time, assigns the lowest free slot to each arriving car, calculates the exact fee from the parked time and frees the slot when the car leaves.

> Project for *Professional Skills for Engineers – Technical Projects* (ULPGC, 2026).

---

## 👥 Team and responsibilities

All the functions are in `functions.py`, each one in its own section.

| Member | Function | What it does |
|---|---|---|
| Alfred Ernst Falcon | `available_spots()` | Returns the number and the list of free slots |
| María Montecristo Fontes González | `register_vehicle_entry()` | Validates the plate format (4 digits + 3 letters), prevents duplicates and assigns the lowest free slot (`None` if full) |
| Rubén García Cuesta | `calculate_fees()` | Calculates the fee of one or several stays (0.03 €/min) |
| Nahún Quintana Granado | `register_vehicle_exit()` | Gets the price with `calculate_fees()`, frees the slot and prints the price |

`main.py` connects the four functions in an interactive program.

---

## 📁 Repository structure

```
├── functions.py                # The four team functions
├── parking_data.py             # Initial parking: 50 slots, 35 occupied
├── main.py                     # Interactive program
├── Smart_Parking_System.ipynb  # Google Colab notebook (live demo)
├── LICENSE                     # MIT License
└── README.md
```

---

## ▶️ How to run

**Requirements:** Python 3.10 or newer. No external libraries are needed.

```bash
git clone https://github.com/sabrent-hash/Smart-Parking-System.git
cd Smart-Parking-System
python main.py
```

Then type a license plate:

- A **new** plate (format `0000AAA`, e.g. `8492LMP`) → the car **enters** and gets the lowest free slot.
- A plate that is **already inside** → the car **exits**: type the hours parked (e.g. `2.5`) and the price is shown.
- Type **`q`** to quit and see the **daily report** (what each car paid and the total income).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sabrent-hash/Smart-Parking-System/blob/main/Smart_Parking_System.ipynb)

**Google Colab:** open `Smart_Parking_System.ipynb` in Colab and click *Runtime → Run all*.
Colab link: https://colab.research.google.com/github/sabrent-hash/Smart-Parking-System/blob/main/Smart_Parking_System.ipynb

---

## 🔢 Inputs and outputs

| Inputs | Outputs |
|---|---|
| `parking_slots` (`dict[int, str \| None]`) | Number and list of free slots |
| `license_plate` (str, format `0000AAA`) | Assigned slot number (`None` if full) |
| `hours` parked (float, `2.5` = 2 h 30 min) | Price in euros and daily income report |

Data format:

```python
parking_slots = {1: "0001BCD", 2: None}   # {slot_number: license_plate or None}
```

---

## 💡 Worked example

1. Parking with **50 slots**, **35 occupied** → 15 available.
2. Car **8492LMP** arrives → assigned **slot #36** → 14 available.
3. It leaves after **2.5 hours** → 2.5 × 60 min × 0.03 €/min = **4.50 €** → slot #36 freed.

```
=== SMART PARKING SYSTEM ===
Type a NEW plate to ENTER, or a plate that is INSIDE to EXIT and pay.
Plate format: 4 digits + 3 letters (e.g. 8492LMP).
Total: 50 | Occupied: 35 | Available: 15

License plate (or 'q' to quit): 8492LMP
Vehicle 8492LMP assigned to spot 36. (Type 8492LMP again when it leaves.)
Total: 50 | Occupied: 36 | Available: 14

License plate (or 'q' to quit): 8492LMP
Vehicle 8492LMP is inside -> EXIT
Hours parked (e.g. 2.5): 2.5
Vehicle 8492LMP left spot 36. Total price: 4.50 €
Total: 50 | Occupied: 35 | Available: 15

License plate (or 'q' to quit): q

--- Daily report ---
  8492LMP: 4.50 €
  TOTAL INCOME: 4.50 €
Goodbye!
```

---

## ✅ Validation

Wrong data is detected and reported without stopping the program:

- Empty license plate → error message
- Plate with a wrong format (e.g. `ABC123` or `A`) → error message, for entries and exits (`register_vehicle_entry()` also raises `ValueError`)
- A car that is already inside tries to enter → `ValueError` (handled in `main.py`)
- Parking full → `register_vehicle_entry()` returns `None`
- Hours that are not a number (e.g. `abc`) or negative hours → error message
- Rows that are not pairs or negative minutes in `calculate_fees()` → `ValueError`

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file.
We chose MIT because it is short and widely known, it lets anyone (universities, municipalities or companies) use and modify the code, and it keeps our copyright notice while protecting us from liability.
