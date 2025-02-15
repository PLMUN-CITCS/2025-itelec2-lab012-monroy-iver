# Iver John R Monroy
# ITELEC2
# Laboratory #12 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def main():
    day = input("Enter a day of the week: ").strip().lower()
    day_messages = {
    "monday": "Today is Monday.",
    "tuesday": "Today is Tuesday.",
    "wednesday": "Today is Wednesday.",
    "thursday": "Today is Thursday.",
    "friday": "Today is Friday.",
    "saturday": "Today is Saturday.",
    "sunday": "Today is Sunday."
    }       
    message = day_messages.get(day, "Invalid day entered.")
    day_type = "Weekend" if day in ("saturday", "sunday") else "Weekday" if day in day_messages else "unknown"
    print(message)
    print("It's a", day_type + "!")

if __name__ == "__main__":
    main()