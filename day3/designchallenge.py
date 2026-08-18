mport numpy as np
import pandas as pd

# Student names
names = ["Alice", "Bob", "Charlie", "David", "Emma"]

# Generate random marks (60 to 100)
python_marks = np.random.randint(60, 101, 5)
ai_marks = np.random.randint(60, 101, 5)
ml_marks = np.random.randint(60, 101, 5)

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Python": python_marks,
    "AI": ai_marks,
    "ML": ml_marks
})

# Calculate average
df["Average"] = (df["Python"] + df["AI"] + df["ML"]) / 3

# Add Result column
df["Result"] = np.where(df["Average"] >= 75, "Pass", "Fail")

# Display DataFrame
print("Student Marks:")
print(df)

# Find topper
topper = df.loc[df["Average"].idxmax()]

print("\nTopper:")
print("Name:", topper["Name"])
print("Average:", round(topper["Average"], 2))import numpy as np
import pandas as pd

# Student names
names = ["Alice", "Bob", "Charlie", "David", "Emma"]

# Generate random marks (60 to 100)
python_marks = np.random.randint(60, 101, 5)
ai_marks = np.random.randint(60, 101, 5)
ml_marks = np.random.randint(60, 101, 5)

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Python": python_marks,
    "AI": ai_marks,
    "ML": ml_marks
})

# Calculate average
df["Average"] = (df["Python"] + df["AI"] + df["ML"]) / 3

# Add Result column
df["Result"] = np.where(df["Average"] >= 75, "Pass", "Fail")

# Display DataFrame
print("Student Marks:")
print(df)

# Find topper
topper = df.loc[df["Average"].idxmax()]

print("\nTopper:")
print("Name:", topper["Name"])
print("Average:", round(topper["Average"], 2))\



the proper basic python program done was the given below

subjects=("Python","SQL","AI")
students=[]

def add_student(name,age):
    student={"Name":name,"Age":age}
    students.append(student)
    
add_student("Rahul",20)
add_student("Ananya",21)
add_student("Kiran",22)

print("Subjects:",subjects)
for student in students:
    print(student)
