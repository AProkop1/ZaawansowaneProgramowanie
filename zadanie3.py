# zadanie 3
def even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


my_num = 4

result = even(my_num)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


