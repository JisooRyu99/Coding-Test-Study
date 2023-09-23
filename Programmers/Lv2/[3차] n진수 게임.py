# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def convert(n,base):
    T = '0123456789ABCDEF'
    q,r = divmod(n,base)
    return convert(q,base) + T[r] if q else T[r]
def solution(n, t, m, p):
    answer = ''
    tmp = ''
    for i in range(t*m):
        tmp +=convert(i,n)
    for i in range(p-1,t*m,m):
        answer+=(tmp[i])
    return answer