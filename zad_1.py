# zadanie 1
class Student:
    def __init__(self, name: str, mark: int):
        self.name = name
        self.mark = mark

    def is_passed(self, ) -> bool:
        if self.mark > 50:
            return True
        else:
            return False

student1 = Student("Agata",90)
student2 = Student("Anna", 20)




