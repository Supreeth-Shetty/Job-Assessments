class Father:
    def __init__(self, father_name, father_age):
        self.father_name = father_name
        self.father_age = father_age
    def father_details(self):
        print("Father Name:", self.father_name)
        print("Father Age:", self.father_age)

class Mother:
    def __init__(self, mother_name, mother_age):
        self.mother_name = mother_name
        self.mother_age = mother_age
    def mother_details(self):
        print("Mother Name:", self.mother_name)
        print("Mother Age:", self.mother_age)


class Child(Father, Mother):
    def __init__(self, father_name, father_age, mother_name, mother_age , child_name, child_age):
        Father.__init__(self, father_name, father_age)
        Mother.__init__(self, mother_name, mother_age)
        self.child_name = child_name
        self.child_age = child_age
    def child_details(self):
        print("Child Name:", self.child_name)
        print("Child Age:", self.child_age)
        Father.father_details(self)
        Mother.mother_details(self)


child = Child("Raghuvaran", 30, "Leela", 25, "Rocky", 10) # Child class inherits Father and Mother class and hence we can use the methods of Father and Mother class
# child.father_details() # child class inherites Father class and hence we can use the method of Father class
# child.mother_details() # child class inherites of Mother class and hence we can use the method of Mother class
child.child_details() # child class inherites of Father and Mother class and hence we can use the method of Father and Mother class
print(f"\n{'#'*120}")

print("""Notes
1. The child class inherits the attributes of both the parent classes.
2. The child class can override the attributes of the parent classes.
3. The child class can override the methods of the parent classes.""")

