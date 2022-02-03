def solution(n):
    answer = [num for num in range(1,n) if n%num==1]
    return min(answer)
