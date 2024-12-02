import sys

sys.path.insert(0, '../src')
import day_01 as d1

def test_find_dist_from_two_lists():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    assert d1.find_dist_from_two_lists(list1, list2) == 11


def test_find_similarity_score_from_test_lists():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    assert d1.find_similarity_score_from_test_lists(list1, list2) == 31
