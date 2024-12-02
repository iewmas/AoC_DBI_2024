

def find_dist_from_two_lists(list1, list2):
    distance = 0

    for a, b in zip(sorted(list1), sorted(list2)):
        distance = distance + abs(a-b)

    return distance


def find_similarity_score_from_test_lists(list1, list2):
    similarity = 0

    for a in list1:
        similarity = similarity + (a * list2.count(a) )

    return similarity