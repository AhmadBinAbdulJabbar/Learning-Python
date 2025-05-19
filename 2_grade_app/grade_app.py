
def report(students):
    print("Report: ")

    average_grades = {}

    for i, student in enumerate(sorted(students), start=1):
        
        # print("; ".join([f"{key}: {value}" for key, value in capitals.items()]))
        grades_output = ", ".join([f"{key}: {value}" for key, value in students[student].items()])
        # print(grades_output)
        # grades_num = [int(grade) for grade in students[student].values()]
        grades_num = list(students[student].values())
        average = sum(grades_num)/len(students[student])

        average_grades[student] = average

        print(f"{i}. {student} - Grades: {grades_output} | Average: {average:.2f}")

    return average_grades
    


def performers(averages_dict):
    if not averages_dict:
        print("⚠️ No students to analyze.")
        return
    top_student = max(averages_dict, key=averages_dict.get)
    low_student = min(averages_dict, key=averages_dict.get)

    print(f"Top Performer: {top_student} with average {averages_dict[top_student]:.2f}")
    print(f"Lowest Performer: {low_student} with average {averages_dict[low_student]:.2f}")


def add_students(students):
    num_of_students = int(input("How many students? ").strip())
    num_of_subject = int(input("How many subjects? ").strip())

    subjects = []

    for i in range(1, num_of_subject + 1):
        subject_name = input(f"Enter subject name {i}: ").strip().capitalize()
        subjects.append(subject_name)
    
    students = {}
    for i in range(1, num_of_students + 1):
        name = input(f"Enter name of student {i}: ").strip().capitalize()
        grades = {}

        for i in range(len(subjects)):
            while True:
                subject_name = subjects[i]
                grade_num = int(input(f"Enter Marks of subject {subject_name} for {name}: ").strip())
                if grade_num < 0 or grade_num > 100:
                    print("Invalid Input please enter marks in range 0-100.")
                    continue
                grades[subject_name] = grade_num
                break
        
        students[name] = grades
        print(f"✅ {name} was added successfully!")
    print("✅ Student(s) added successfully!")

    return students

    # print(students)

    # averages_dict = report(students)
    # print(averages_dict)

    # performers(averages_dict)



def main():
    print("📘 Welcome to Grade App\n")
    students = {}

    while True:
        print("\n📚 Menu")
        print("1. Add Students")
        print("2. View Report")
        print("3. Show Top & Lowest Performer")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            students = add_students(students)
        elif choice == "2":
            if students:
                report(students)
            else:
                print("⚠️ No students added yet.")
        elif choice == "3":
            if students:
                averages_dict = report(students)
                performers(averages_dict)
            else:
                print("⚠️ No data to analyze.")
        elif choice == "4":
            print("👋 Exiting Grade App. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()