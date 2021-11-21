# zadanie 6

def delete_duplicates_power_of_3(list1: list, list2: list) -> list:
    temp_set = set(list1 + list2)
    final_list =[]
    for num in temp_set:
        final_list.append(num * num * num)
    return final_list