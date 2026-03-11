"""
Student Marks Analyzer

A simple Python program that collects student marks
and generates a report including:
- Average marks
- Highest scorer
- Lowest scorer
- Detailed student list

Author: Shrestha Sarangi

"""

def collect_student_data():
    students = {}

    while True:
        name = input("Enter the student name or done to exit: ").strip()
        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists!")
            continue

        try:
            marks = float(input(f"Enter marks for {name}: "))
            if marks < 0:
                print("Marks cannot be negative.")
                continue
            else:
                students[name] = marks
        except ValueError:
            print("Please enter a valid number.")
    return students

def display_report(students):
    if not students:
        print("No student data.")
        return
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks) / len(marks)

    topper = [name for name, score in students.items() if score == max_score]
    bottomer = [name for name, score in students.items() if score == min_score]

    print("\n ===== Students Marks Report =====")
    print("-" * 30)
    print(f"Total students: {len(students)}")
    print(f"Average marks for students: {average:.2f}")
    print(f"Highest mark: {max_score} by {", ".join(topper).title()}")
    print(f"Lowest mark: {min_score} by {", ".join(bottomer).title()}")
    print("-" * 30)
    print("Detailed Marks")
    for name, score in sorted(students.items()):
        print(f" - {name} : {score}")

def main():
    students = collect_student_data()
    display_report(students)
    print("-" * 30)

if __name__ == "__main__":
    main()
