def create_an_empty_list():
    return []

def create_a_list():
    new_list = [1, 'apple', True, 3.14]
    return new_list

def add_element_to_end_of_list(my_list, element):
    my_list.append(element)
    return my_list

def add_element_to_start_of_list(my_list, element):
    my_list.insert(0, element)
    return my_list

def remove_element_from_end_of_list(my_list):
    if my_list:
        my_list.pop()
    return my_list

def remove_element_from_start_of_list(my_list):
    if my_list:
        del my_list[0]
    return my_list
    

def retrieve_first_element_from_list(lst):
    if lst:
        return lst[0]
    else:
        return None 

def retrieve_element_from_index(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None

def retrieve_last_element_from_list(lst):
    if lst:
        return lst[-1]
    else:
        return None
