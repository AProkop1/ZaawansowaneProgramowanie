# zadanie 1
def hello(name: str, surname: str) -> str:
    sentence = f"Cześć {name} {surname}!"
    return sentence


my_name = "Agnieszka"
my_surname = "Prokop"
result = hello(my_name, my_surname)

print(result)