grades = {}
no_of_Students= int(input("Enter the Class Strength: "))
for no_of_Students in range (no_of_Students):
    name = input("Enter the Student Name: ")
    while True:
     try:
      marks = float(input("Enter the Marks: "))
      break
     except ValueError:
         print("Invalid Marks")
    grades[name]=marks

print("\n Student Results: ")
for name,marks in grades.items():
       print(f" {name}: {marks}")

print(" Class Results: ")
average = sum(grades.values())/len(grades)
print(f" Average Grade: {average:.2f}")

