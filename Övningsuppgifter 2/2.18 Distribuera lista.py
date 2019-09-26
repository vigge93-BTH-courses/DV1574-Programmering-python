def distribute(my_item, my_list):
    new_list = []
    for el in my_list:
        new_el = el.copy()
        new_el.append(my_item)
        new_list.append(new_el)
    return new_list


old_list = [['kangar'], ['z'], ['f']]
print(distribute('oo', old_list))
print(old_list)
