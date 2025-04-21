grades = {}

def add_student():
    name = input("Enter student name to add: ")
    scores = list(map(int, input(f"Enter scores for {name} (space-separated): ").split()))
    if name in grades:
        print(f"{name} already exists.")
    else:
        grades[name] = scores
        print(f"{name} added with scores {scores}")

def add_scores():
    name = input("Enter student name to add scores to: ")
    if name in grades:
        new_scores = list(map(int, input(f"Enter additional scores for {name} (space-separated): ").split()))
        grades[name].extend(new_scores)
        print(f"Scores {new_scores} added for {name}")
    else:
        print(f"{name} not found.")

def calculate_averages():
    averages = {}
    for student, scores in grades.items():
        avg = round(sum(scores) / len(scores), 1) if scores else 0
        averages[student] = avg
        print(f"Average for {student}: {avg}")
    return averages

def find_top_and_lowest_students(averages):
    if not averages:
        print("No students to compare.")
        return
    top_student = max(averages, key=averages.get)
    lowest_student = min(averages, key=averages.get)
    print(f"Top student: {top_student}")
    print(f"Lowest scoring student: {lowest_student}")

# Main loop
while True:
    print("\nOptions:\n1. Add new student\n2. Add scores to student\n3. Show averages\n4. Show top & lowest students\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        add_scores()
    elif choice == '3':
        averages = calculate_averages()
    elif choice == '4':
        if 'averages' not in locals():
            averages = calculate_averages()
        find_top_and_lowest_students(averages)
    elif choice == '5':
        print("Exiting Grade Book Manager.")
        break
    else:
        print("Invalid choice. Try again.")
