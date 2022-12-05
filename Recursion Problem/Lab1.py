import math

def getStudentNumber():
    return "500689794"

def sum_exists(n, i, p_list):
    if n%p_list[i] == 0:
        return True
    if i == len(p_list) - 1 and n%p_list[i] != 0:
        return False
    if n == 0:
        return True
    if n - p_list[i] < 0:
        return False
    return sum_exists(n-p_list[i], i, p_list) or sum_exists(n, i+1, p_list)

def find_sum(n, i, p_list, sum_list):
    if n%p_list[i] == 0:
        list1 = list(sum_list)
        list1.extend([p_list[i]] * (n // p_list[i]))
        return list1
    if i == len(p_list) - 1 and n%p_list[i] != 0:
        return []
    if n == 0:
        return sum_list
    if n - p_list[i] < 0:
        return []
    list1 = list(sum_list)
    list1.append(p_list[i])
    sol1 = find_sum(n - p_list[i], i,  p_list, list1 )
    if len(sol1) != 0:
        return sol1
    sol2 = find_sum(n , i+1 ,  p_list, sum_list)
    if len(sol2) != 0:
        return sol2
    return []
