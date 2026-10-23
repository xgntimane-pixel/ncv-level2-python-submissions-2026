
marks = []


def capture_marks():
    mark = int(input("Enter mark (-1 to stop capturing): "))

    while mark != -1:
        if 0 <= mark <= 100:
            marks.append(mark)
            print("Mark captured successfully.")
        else:
            print("Invalid mark. Enter a mark from 0 to 100.")

        mark = int(input("Enter mark (-1 to stop capturing): "))


def check_number():
    print(f"Number of marks: {len(marks)}")


def calculate_sum():
    print(f"Sum of marks: {sum(marks)}")


def highest_mark():
    if len(marks) == 0:
        print("No marks have been captured.")
    else:
        print(f"Highest mark: {max(marks)}")


while True:
    print("\n===== MARKS MENU =====")
    print("1. Capture marks")
    print("2. Check number of marks")
    print("3. Calculate sum of marks")
    print("4. Find highest mark")
    print("-1. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        capture_marks()

    elif choice == "2":
        check_number()

    elif choice == "3":
        calculate_sum()

    elif choice == "4":
        highest_mark()

    elif choice == "-1":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
