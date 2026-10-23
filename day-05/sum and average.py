marks = []
mark = int(input('Enter mark (or -1 to stop): '))

while mark != -1:
    marks.append(mark)

    mark = int(input('Enter mark (or -1 to stop): '))

print(f'Our list has {len(marks)} elements')
print(marks)

# for sum 
print(f'The sum of the marks is {sum(marks)}')

#Average for all

if len(marks) > 0:
    average = sum(marks) / len(marks)
    print(f'The average mark is {average:.2f}')
