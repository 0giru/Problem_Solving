from itertools import combinations

def select_index(arridx, array):
    result = []
    for i in range(len(array)+1):
        temp = list(combinations(arridx, i))
        result += temp
    return result

def solution(numbers, target):
    answer = 0
    array_index = []
    indexes = []

    for i in range(len(numbers)):
        array_index.append(i)

    indexes = select_index(array_index, numbers)

    while indexes:
        temp = indexes.pop()
        temp2 = 0
        for i in temp:
            temp2 += numbers[i]
        if sum(numbers) - 2*temp2 == target:
            answer += 1

    return answer

"""
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
"""