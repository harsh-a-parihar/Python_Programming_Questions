'''Bio-data of a student.'''

# Solution

# creating a Parent class
class Person:
    # initiating function that is automatically gets called by constructor
    def __init__(self,name,age):    # 'self' is container used to store current object
        self.name=name
        self.age=age
    
    def display(self):  # display function returns the behaviour/result of the class
        print(self.name,self.age)

# creating a child class 'Student' with the inherited properties of parent class
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)  # method to copy the all properties from the parent class(super_class)
        self.marks=marks
    
    def display(self):
        super().display()   # method to display all the copied properties from the super class
        print(self.marks)

# creating a child class 'Employee' with the inherited properties of parent class
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)  # method to copy the all properties from the parent class(super_class)
        self.salary=salary

    def display(self):
        super().display()   # method to display all the copied properties from the super class
        print(self.salary)

st=Student('Harsh',19,100)        # assign constructor to object 'st'
st.display()      # calling object(data) behaviour

em=Student('Rama',40,300000)        # assign constructor to object 'st'
em.display()    # calling object(data) behaviour

#-----------------------------------------------------------------------------------------------------#
