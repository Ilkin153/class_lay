class Student:
    def __init__(self, name, surename, age):
        self.name = name
        self.surename = surename
        self.age = age
    def show_info(self):
        print(self.name, self.surename, self.age)

student1 = Student("Ilkin", "Alamanov", 18)
student2 = Student("Abbas", "Abbaszade", 20)

student1.show_info()
student2.show_info()