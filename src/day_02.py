
def check_all_increase(list_in): 
    for l in list_in: 
        if l < 0: return False
    return True 


def check_all_decraese(list_in):
    for l in list_in:
        if l > 0: return False
    return True 


def check_is_safe(list_in):
    list1 = list_in[:-1]
    list2 = list_in[1:]
    list3 = [a-b for a, b in zip(list1, list2)]

    if (check_all_decraese(list3) or check_all_increase(list3)):
        for l in list3:
            if abs(l) < 1 or abs(l) > 3: return False
    else:
        return False

    return True


def check_is_safe_problem_dampener(list_in):
    if check_is_safe(list_in):
        return True 
    else: 
        for idx in range(len(list_in)):
            list_new = list_in.copy()
            list_new.pop(idx)
            if check_is_safe(list_new): return True
            
    return False  