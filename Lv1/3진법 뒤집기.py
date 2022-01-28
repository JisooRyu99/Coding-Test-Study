def ternary(n,q):   # 3진법 만들기
    rev_base=''
    while n:
        n,mod = divmod(n,q)
        rev_base += str(mod)
    return rev_base[::-1]
  
def solution(n):
    answer = 0
    cnt=3
    s =(ternary(n,3))
    while cnt>0: 
        m=''
        for digit in s:   # 뒤집기
            m=digit+m
        s=m
        cnt-=1
    return int(s,3)       # 10진법 return 
            
