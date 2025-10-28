import json
import datetime
import os

DATA_FILE = "ecotrack_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_activity(data):
    print("\n--- Add Sustainability Activity ---")
    date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ") or str(datetime.date.today())
    category = input("Category (Energy/Water/Waste/Transport/etc): ").capitalize()
    description = input("Description: ")
    impact = input("Impact Level (Low/Medium/High): ").capitalize()

    entry = {
        "date": date,
        "category": category,
        "description": description,
        "impact": impact
    }
    data.append(entry)
    save_data(data)
    print("✅ Activity added successfully!")

def view_activities(data):
    print("\n--- Sustainability Activities ---")
    if not data:
        print("No records found.")
        return
    for i, item in enumerate(data, start=1):
        print(f"\n{i}. Date: {item['date']}")
        print(f"   Category: {item['category']}")
        print(f"   Description: {item['description']}")
        print(f"   Impact: {item['impact']}")

def update_activity(data):
    view_activities(data)
    if not data:
        return
    try:
        idx = int(input("\nEnter activity number to update: ")) - 1
        if 0 <= idx < len(data):
            print("Leave field blank to keep existing value.")
            new_desc = input(f"New description [{data[idx]['description']}]: ") or data[idx]['description']
            new_impact = input(f"New impact [{data[idx]['impact']}]: ") or data[idx]['impact']
            data[idx]['description'] = new_desc
            data[idx]['impact'] = new_impact
            save_data(data)
            print("✅ Activity updated successfully!")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Invalid input.")

def delete_activity(data):
    view_activities(data)
    if not data:
        return
    try:
        idx = int(input("\nEnter activity number to delete: ")) - 1
        if 0 <= idx < len(data):
            deleted = data.pop(idx)
            save_data(data)
            print(f"🗑️ Deleted: {deleted['description']}")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Invalid input.")

def summary_by_category(data):
    print("\n--- Summary by Category ---")
    if not data:
        print("No records found.")
        return
    summary = {}
    for item in data:
        summary[item["category"]] = summary.get(item["category"], 0) + 1
    for cat, count in summary.items():
        print(f" - {cat}: {count} activity(ies)")

def summary_by_date(data):
    print("\n--- Summary by Date ---")
    if not data:
        print("No records found.")
        return
    summary = {}
    for item in data:
        summary[item["date"]] = summary.get(item["date"], 0) + 1
    for date, count in summary.items():
        print(f" - {date}: {count} activity(ies)")

def main():
    data = load_data()
    while True:
        print("\n=== EcoTrack – Daily Sustainability Logger ===")
        print("1. Add Activity")
        print("2. View Activities")
        print("3. Update Activity")
        print("4. Delete Activity")
        print("5. Summary by Category")
        print("6. Summary by Date")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_activity(data)
        elif choice == "2":
            view_activities(data)
        elif choice == "3":
            update_activity(data)
        elif choice == "4":
            delete_activity(data)
        elif choice == "5":
            summary_by_category(data)
        elif choice == "6":
            summary_by_date(data)
        elif choice == "7":
            print("🌱 Thank you for using EcoTrack! Stay sustainable!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
