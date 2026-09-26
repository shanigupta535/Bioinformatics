# 🧠 OOP kya hota hai?

# OOP = Object-Oriented Programming

# Ye programming ka ek way/style hai jisme hum program ko objects ke around organize karte hain.

# Real life mein dekho:

# Ek Student ke paas kuch information hoti hai — name, age, course
# aur kuch kaam hote hain — study(), attend_class(), give_exam()

# Programming mein hum isi idea ko represent kar sakte hain:

# Student
# │
# ├── Data
# │   ├── name
# │   ├── age
# │   └── course
# │
# └── Functions/Methods
#     ├── study()
#     ├── attend_class()
#     └── give_exam()

# Yahi basic idea OOP ka hai.


class Student:

    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)
        print("My branch is", self.branch)


# Creating objects
student1 = Student("Shani", 20, "Biotechnology")
student2 = Student("Rahul", 21, "Computer Science")

# Calling method
student1.introduce()
print()
student2.introduce()