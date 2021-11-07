# wersja for
def double_num(num_list: list):
    for x in range(len(num_list)):
        num_list[x] = num_list[x] * 2
    return num_list


# wersja lista składana

def double_num(num_list: list):
    num_list = [num * 2 for num in num_list]
    return num_list

#num_list = [1,2,3,4,5]

#print(double_num(num_list))