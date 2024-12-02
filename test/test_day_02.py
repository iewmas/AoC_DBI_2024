import sys

sys.path.insert(0, '../src')
import day_02 as d2

def test_check_all_increase():
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, -1, 3, 4]
    assert d2.check_all_increase(list1) == True 
    assert d2.check_all_increase(list2) == False 
    

def test_check_all_decrease():
    list1 = [-1, -2, -3, -4]
    list2 = [-1, -2, 1, -3, -4]
    assert d2.check_all_decraese(list1) == True 
    assert d2.check_all_decraese(list2) == False 


def test_check_is_safe():
    results = list() 
    
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9], 
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5], 
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    for report in reports:
        result = d2.check_is_safe(report) 
        results.append(result)

    assert results.count(True) == 2


def test_check_is_safe_problem_dampener():
    results = list() 
    
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9], 
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5], 
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    for report in reports:
        result = d2.check_is_safe_problem_dampener(report) 
        results.append(result)

    assert results.count(True) == 4
    
    