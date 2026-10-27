
# Vaccination Tracker

A simple, privacy-respecting command-line tool for recording vaccine doses and checking who is fully vaccinated. Built in Python using Object-Oriented Programming (OOP).

**Module:** PROG211 – Object-Oriented Programming 1
**Assignment:** Real-World Solutions under DPG Standards
**Domain:** Health
**Student:** ANDREW BAI CONTEH | **Student ID:** 905005973
**Institution:** Limkokwing University of Creative Technology, Sierra Leone

---

## 1. Problem Statement

Health workers often need a quick way to know which people have completed their vaccine course and which still need further doses. This program lets a user register recipients, record doses, and check vaccination status, without storing any personal or sensitive information.

## 2. Features

- Add a new recipient using an anonymous ID and age group
- Record a vaccine dose with its date
- View all records
- Check whether one person is fully vaccinated for a chosen vaccine
- List everyone who is not yet fully vaccinated
- Show the total number of recipients
- Input validation (duplicate IDs, unknown IDs, invalid menu choices)

## 3. Project Structure

```
vaccination-tracker/
├── vaccination_tracker.py   # Source code (classes, data structure, menu)
└── README.md                # Documentation
```

## 4. How to Run

**Requirements:** Python 3.8 or newer. No external libraries needed.

```bash
git clone https://github.com/[your-username]/vaccination-tracker.git
cd vaccination-tracker
python vaccination_tracker.py
```

## 5. OOP Concepts Used 

### Task 1: Classes, Attributes and Objects
| Class | Attributes | Methods |
|---|---|---|
| `Vaccine` | `name`, `doses_required` | `display_info()` |
| `Recipient` | `recipient_id`, `age_group`, `doses` | `record_dose()`, `doses_of()`, `is_fully_vaccinated()`, `display_info()` |

Objects interact when a `Vaccine` object is passed into a `Recipient` method, e.g. `recipient.record_dose(vaccine, date)`.

### Task 2: Python Data Structure
- A **dictionary** (`records`) stores all `Recipient` objects, using the recipient ID as the key for fast lookup.
- `add_record()` adds a recipient and `display_records()` prints all of them.
- **Tuples :** each dose is stored as a `(vaccine_name, date)` tuple, and the available vaccines are kept in a fixed tuple, `AVAILABLE_VACCINES`.

### Task 3: Methods
- **Instance methods:** `record_dose()`, `is_fully_vaccinated()`, `display_info()`, which work on one specific object.
- **Class method:** `Recipient.get_total_recipients()` (decorated with `@classmethod`), which reports on the class as a whole using the class attribute `total_recipients`.

## 6. Digital Public Goods (DPG) Alignment

| DPG Principle | How this project meets it |
|---|---|
| **Open-source** | The full source code is published openly on GitHub. |
| **Inclusive and accessible** | Plain text menu, simple numbered options, clear messages, no special hardware or internet required. Runs on any system with Python. |
| **Privacy-respecting** | No names, phone numbers, addresses or exact ages are stored. Recipients are identified only by an anonymous ID (e.g. `R001`) and a broad age group (`0-5`, `6-17`, `18+`). |
| **Modular and reusable** | Logic is split into separate classes and small functions, so parts such as `Vaccine` or `Recipient` can be reused or extended in other health tools. |

## 7. Example Usage

**Sample session** (user input shown after each prompt):

```
===== Vaccination Tracker =====
1. Add new recipient
2. Record a vaccine dose
3. Show all records
4. Check one person's vaccination status
5. List people not fully vaccinated
6. Show total recipients
0. Exit
Choose an option: 1
Enter anonymous ID (e.g. R001): R001
Age groups: 1) 0-5  2) 6-17  3) 18+
Choose age group: 3
Added record R001.

Choose an option: 2
Enter anonymous ID (e.g. R001): R001
Available vaccines:
  1. COVID-19 (doses required: 2)
  2. Polio (doses required: 3)
  3. Measles (doses required: 2)
Choose a vaccine number: 1
Enter date given (YYYY-MM-DD): 2026-09-01
Recorded COVID-19 dose for R001 on 2026-09-01.

Choose an option: 4
Enter anonymous ID (e.g. R001): R001
Choose a vaccine number: 1
R001: 1/2 doses of COVID-19 -> NOT fully vaccinated

Choose an option: 3

=== All Vaccination Records ===
ID: R001 | Age group: 18+
  - COVID-19 on 2026-09-01

Choose an option: 0
```

## 8. Limitations and Future Improvements

- Data is stored in memory only and is lost when the program closes.
- Future versions could save records to a file or database, add dose-interval reminders, or add a graphical interface.


## 9. Acknowledgements

Developed for PROG211 under lecturer Julius Laggar.
