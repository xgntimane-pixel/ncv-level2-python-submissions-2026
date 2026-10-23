
total = 0
count = 0

while True:
    mark = int(input("Enter mark (-1 to stop): "))

    if mark == -1:
        break
    elif mark < 0 or mark > 100:
        print("Invalid mark")
    else:
        total += mark
        count += 1

if count > 0:
    print("Number of valid marks:", count)
    print("Total:", total)
    print("Average: {:.2f}".format(total / count))
else:
    print("No valid marks were entered.")
