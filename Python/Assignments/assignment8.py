# Employee Time Tracker System

def add_employee(log, name):
    if name not in log:
        log[name] = []
        print(f"Added new employee: {name}")
    else:
        print(f"Employee {name} already exists.")

def add_working_hours(log, name, hours):
    if name in log:
        log[name].append(hours)
        print(f"Added {hours} hours to {name}")
    else:
        print(f"Employee {name} does not exist.")

def get_total_hours(log):
    totals = {}
    for name, hours in log.items():
        totals[name] = sum(hours)
    return totals

def find_most_hardworking(log):
    totals = get_total_hours(log)
    if totals:
        max_person = max(totals, key=totals.get)
        return max_person, totals[max_person]
    return None, 0

def main():
    time_log = {}
    
    while True:
        print("\n=== Employee Time Tracker ===")
        print("1. Add new employee")
        print("2. Add working hours")
        print("3. Get total hours for each employee")
        print("4. Find most hardworking employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter employee name: ")
            add_employee(time_log, name)

        elif choice == '2':
            name = input("Enter employee name: ")
            try:
                hours = float(input("Enter hours worked: "))
                add_working_hours(time_log, name, hours)
            except ValueError:
                print("Please enter a valid number for hours.")

        elif choice == '3':
            totals = get_total_hours(time_log)
            if totals:
                print("\nTotal Hours Worked:")
                for name, total in totals.items():
                    print(f"{name}: {total} hours")
            else:
                print("No employee records found.")

        elif choice == '4':
            name, hours = find_most_hardworking(time_log)
            if name:
                print(f"{name} has worked the most: {hours} hours")
            else:
                print("No data available.")

        elif choice == '5':
            print("Exiting Employee Time Tracker.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
