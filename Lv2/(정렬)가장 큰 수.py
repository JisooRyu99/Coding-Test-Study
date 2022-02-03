# 시간 초과
# permutations 풀려고 했으나 시간초과로 실패

from itertools import permutations
def solution(numbers):
    answer = []
    
    for i in (list(permutations(numbers,len(numbers)))):
        answer.append("".join(map(str,i)))
    
    return max(answer)
--------------------------------------------------------------------------

def solution(numbers):
    answer = []
    
    num = list(map(str,numbers))
    num.sort(key = lambda x : x*3, reverse = True)
    # x*3을 하는 이유 : num의 인수값이 1000이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 의미
    return str(int("".join(num)))

