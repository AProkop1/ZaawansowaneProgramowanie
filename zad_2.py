# zadanie 1
# potrzebna klasa Student do klasy Order
class Student:
    def __init__(self, name: str, mark: int):
        self.name = name
        self.mark = mark

    def is_passed(self) -> bool:
        if self.mark > 50:
            return True
        else:
            return False


# zadanie 2

class Library:
    def __init__(self, city: str, street: str, zip_code: int, open_hours: str, phone: int):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library is located in {self.city} at {self.zip_code} {self.street}. Open hours: {self.open_hours}. You " \
               f"can contact the library with this phone number: {self.phone} "


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: int, phone: int):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee named {self.first_name} {self.last_name } was born {self.birth_date } and is hired since " \
                f"{self.hire_date}. Employee address is {self.city} {self.street} {self.zip_code}. Phone number is {self.phone}"


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book written by {self.author_name} {self.author_surname} is in library is located in {self.library.city} at "\
               f"{self.library.zip_code} {self.library.street}. Open hours: {self.library.open_hours} You "\
               f"can contact the library with this phone number: {self.library.phone}. The book was published {self.publication_date} "\
               f"and has {self.number_of_pages} pages."


class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Order was made by {self.student.name} and prepared by {self.employee.first_name} on {self.order_date}."\
               f" Order contains books written by {[x.author_name + ' ' + x.author_surname for x in self.books]} "


first_library = Library("Wrocław", "Władysława Łokietka", 50243, "12-19", 965147389)
second_library = Library("Wrocław", "Zielińskiego", 53532, "12-19", 965147389)

first_book = Book(first_library, "2021-10-27", "Remigiusz", "Mróz", 304)
second_book = Book(first_library, "2021-11-10", "Magdalena", "Kostyszyn", 117)
third_book = Book(second_library, "22021-02-10", "Natalia", "de Barbaro", 256)
fourth_book = Book(second_library, "2021-09-06", "Edyta", "Prusinowska", 312)
fifth_book = Book(second_library, "2021-11-10", "Jonny", "Thomson", 129)

first_employee = Employee("Anna", "Krzyka", "2021-03-12", "1995-10-09", "Wrocław", "Owsiana", 50631, 186254398)
second_employee = Employee("Andrzej", "Śródmiejski", "2020-08-01", "1999-11-19", "Wrocław", "Krakowska", 50243,
                           864764987)
third_employee = Employee("Anita", "Karłowicka", "2018-10-13", "1989-01-27", "Wrocław", "Robotnicza", 53532, 703576548)

first_student = Student("Mariusz", 27)
second_student = Student("Marzena", 56)
third_student = Student("Magdalena", 99)

first_book_list = [first_book, second_book]
second_book_list = [third_book, fourth_book, fifth_book]
first_order = Order(first_employee, first_student, first_book_list, "2021-11-23")
second_order = Order(second_employee, second_student, second_book_list, "2021-10-11")

print(first_order)
print(second_order)