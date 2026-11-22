
import os
import csv

# Step 1: Create a folder named data
folder_name = "data"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Data folder created successfully!")
else:
    print("Data folder already exists.")

# Step 2: Define student information
students = [
    ["Name", "Age", "Department", "Marks"],
    ["Kashif", 22, "Software Engineering", 90],
    ["Ali", 21, "Computer Science", 85],
    ["Ahmed", 23, "IT", 88],
    ["Sara", 22, "Software Engineering", 92]
]

# Step 3: Create CSV file path
file_path = os.path.join(folder_name, "students.csv")

# Step 4: Write information into CSV
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created successfully!")

# Step 5: Read CSV file
with open(file_path, mode="r") as file:
    reader = csv.reader(file)

    print("\nStudent Information:")

    for row in reader:
        print(row)
