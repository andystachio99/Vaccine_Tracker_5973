"""
Vaccination Tracker
"""

class Vaccine:
    """A vaccine type."""

    def __init__(self, name, doses_required):
        self.name = name
        self.doses_required = doses_required

    def display_info(self):
        print(f"{self.name} (doses required: {self.doses_required})")


class Recipient:
    """A person receiving vaccines. Uses an anonymous ID, NOT a real name."""

    total_recipients = 0  # class attribute

    def __init__(self, recipient_id, age_group):
        self.recipient_id = recipient_id
        self.age_group = age_group
        self.doses = []  # list of (vaccine_name, date) tuples
        Recipient.total_recipients += 1

    # ---- Instance methods ----
    def record_dose(self, vaccine, date):
        self.doses.append((vaccine.name, date))
        print(f"Recorded {vaccine.name} dose for {self.recipient_id} on {date}.")

    def doses_of(self, vaccine):
        return sum(1 for name, _ in self.doses if name == vaccine.name)

    def is_fully_vaccinated(self, vaccine):
        return self.doses_of(vaccine) >= vaccine.doses_required

    def display_info(self):
        print(f"ID: {self.recipient_id} | Age group: {self.age_group}")
        if not self.doses:
            print("  No doses recorded yet.")
        for name, date in self.doses:
            print(f"  - {name} on {date}")

    # ---- Class method ----
    @classmethod
    def get_total_recipients(cls):
        return cls.total_recipients


# Tuple of available vaccines 
AVAILABLE_VACCINES = (
    Vaccine("COVID-19", 2),
    Vaccine("Polio", 3),
    Vaccine("Measles", 2),
)

# ---- ONE data structure: dictionary keyed by recipient ID ----
records = {}


def add_record(recipient):
    if recipient.recipient_id in records:
        print(f"A record with ID {recipient.recipient_id} already exists.")
        return False
    records[recipient.recipient_id] = recipient
    print(f"Added record {recipient.recipient_id}.")
    return True


def display_records():
    if not records:
        print("No records yet.")
        return
    print("\n=== All Vaccination Records ===")
    for recipient in records.values():
        recipient.display_info()
        print()



def ask_id():
    return input("Enter anonymous ID (e.g. R001): ").strip().upper()


def find_recipient():
    rid = ask_id()
    recipient = records.get(rid)
    if recipient is None:
        print(f"No record found for ID {rid}.")
    return recipient


def choose_vaccine():
    print("Available vaccines:")
    for i, vaccine in enumerate(AVAILABLE_VACCINES, start=1):
        print(f"  {i}. ", end="")
        vaccine.display_info()
    choice = input("Choose a vaccine number: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(AVAILABLE_VACCINES):
        return AVAILABLE_VACCINES[int(choice) - 1]
    print("Invalid vaccine choice.")
    return None


# ---------- Menu actions ----------
def add_new_recipient():
    rid = ask_id()
    if not rid:
        print("ID cannot be empty.")
        return
    if rid in records:
        print(f"A record with ID {rid} already exists.")
        return
    print("Age groups: 1) 0-5  2) 6-17  3) 18+")
    groups = {"1": "0-5", "2": "6-17", "3": "18+"}
    age_group = groups.get(input("Choose age group: ").strip())
    if age_group is None:
        print("Invalid age group.")
        return
    add_record(Recipient(rid, age_group))


def add_dose():
    recipient = find_recipient()
    if recipient is None:
        return
    vaccine = choose_vaccine()
    if vaccine is None:
        return
    date = input("Enter date given (YYYY-MM-DD): ").strip()
    if not date:
        print("Date cannot be empty.")
        return
    recipient.record_dose(vaccine, date)


def check_status():
    recipient = find_recipient()
    if recipient is None:
        return
    vaccine = choose_vaccine()
    if vaccine is None:
        return
    given = recipient.doses_of(vaccine)
    if recipient.is_fully_vaccinated(vaccine):
        status = "FULLY VACCINATED"
    else:
        status = "NOT fully vaccinated"
    print(f"{recipient.recipient_id}: {given}/{vaccine.doses_required} "
          f"doses of {vaccine.name} -> {status}")


def show_unvaccinated():
    vaccine = choose_vaccine()
    if vaccine is None:
        return
    pending = [r.recipient_id for r in records.values()
               if not r.is_fully_vaccinated(vaccine)]
    if pending:
        print(f"Not fully vaccinated for {vaccine.name}: {', '.join(pending)}")
    else:
        print(f"Everyone is fully vaccinated for {vaccine.name}.")


def menu():
    print("\n===== Vaccination Tracker =====")
    print("1. Add new recipient")
    print("2. Record a vaccine dose")
    print("3. Show all records")
    print("4. Check one person's vaccination status")
    print("5. List people not fully vaccinated")
    print("6. Show total recipients")
    print("0. Exit")
    return input("Choose an option: ").strip()


def main():
    actions = {
        "1": add_new_recipient,
        "2": add_dose,
        "3": display_records,
        "4": check_status,
        "5": show_unvaccinated,
        "6": lambda: print("Total recipients:", Recipient.get_total_recipients()),
    }
    while True:
        choice = menu()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()