n = int(input("Enter no of enteries: "))
student = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    student[key] = value

print("Student dictionary:", student)