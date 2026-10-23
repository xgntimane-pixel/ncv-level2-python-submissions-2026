def get_marks():
    marks = []

    mark = int(input("Enter mark (or -1 to stop): "))

    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark (or -1 to stop): "))

    return marks


def calculate_average(marks):
    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


results = get_marks()

print("Marks:", results)
print("Total:", sum(results))
print("Number of marks:", len(results))
print(f"Average: {calculate_average(results):.2f}")
