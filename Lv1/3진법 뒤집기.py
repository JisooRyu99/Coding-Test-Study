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
            

  --------------------------------------------------------------------------
# 다른 사람의 풀이

def solution(n):
    answer = 0
    tmp=''
    while n:
        tmp+= str(n%3)
        n=n//3
        print(tmp)
    return int(tmp,3)




---------------------------------------------------------------------------
    
    n진수 -> 10진수
    * 결과값은은 모두 string
    
    2진법 -> 10진수 : int('101',2)
    3진법 -> 10진수 : int('101',3)
    16진법 -> 10진수 : int('ACF',16)
        
        
    
    10진수 -> 2,8,16진수 => bin(), oct(), hex()
    
    
-------------------------------------------------------------------------------
    10진수 -> n진수 
    def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
------------------------------------------------------------------------------------

    n진수 -> n진수 => print(solution(int('c',16),4)) # 16진수인 C를 4진수로 바꾸는것

   
    
