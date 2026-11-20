name = input("Enter your name: ")

m1 = float(input("Enter marks for python: "))
m2 = float(input("Enter marks for sql: "))
m3 = float(input("Enter marks for excel: "))

total = m1 + m2 + m3
percentage = total / 3 * 100

print(f"student name {name} \n Total marks: {total} \n Percentage: {percentage}")

print("welcome to grading system")

if percentage >= 90 and percentage <= 100:
    print("Grade A+")

elif percentage >= 80 and percentage < 90:
    print("Grade A")

elif percentage >= 70 and percentage < 80:
    print("Grade B")

elif percentage >= 60 and percentage < 70:
    print("Grade C")

else:
    print("Grade D")