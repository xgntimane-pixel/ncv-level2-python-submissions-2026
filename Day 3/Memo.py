
print("Ehlanzeni TVET College")
print("Electrical Engineering Application")

name = input("Enter your name: ")
maths = float(input("Enter Mathematics mark: "))
science = float(input("Enter Science mark: "))

if maths > 50 and science > 50:
    print(name, "qualifies to apply!")
else:
    print(name, "does not qualify to apply.")
