# 시간 초과
# permultations으로 푸려고 했으나 시간초과로 실패

from itertools import permutations
def solution(numbers):
    answer = []
    number_list = list(permutations(numbers,len(numbers)))
    
    for n in number_list:
        answer.append("".join(map(str,n)))
    
    return max(answer)
--------------------------------------------------------------------------

def solution(numbers):
    answer = []
    
    num = list(map(str,numbers))
    num.sort(key = lambda x : x*3, reverse = True)
    # x*3을 하는 이유 : num의 인수값이 1000이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 의미
    return str(int("".join(num)))

