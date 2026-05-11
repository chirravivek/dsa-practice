class Student :
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks
    def results(self):
        if self.marks >= 50 :
            print(f"{self.name} - pass")
        else :
            print(f"{self.name} - fail")
student1 = Student("tommy",50)
student2 = Student("jassi", 20)

student1.results()
student2.results()
