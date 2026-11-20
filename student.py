name = input("Enter your name:")

m1 = int(input("Enter Python Marks:"))
m2 = int(input("Enter SQL Marks:"))
m3 = int(input("Enter Exel Marks:"))

total = m1 + m2 + m3
percentage = total / 3 * 100

print(f"Student Name: {name} \n Total Marks: {total} \n Percentage: {percentage}")
