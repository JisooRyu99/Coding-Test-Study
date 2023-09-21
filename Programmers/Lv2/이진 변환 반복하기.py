# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def to_binary(number):
    answer = ''
    value = int(number)
    while value > 1:
        mod = value % 2
        value = value // 2
        answer += str(mod)
    answer += str(value)
    return answer[::-1]

def solution(s):
    zero_cnt = 0
    cnt=0
    while True:
        new_s = ''
        if s=='1':
            return [cnt,zero_cnt]
        else:
            cnt+=1
            for i in s:
                if i=='0':
                    zero_cnt+=1
                else:
                    new_s+=i
            s = (to_binary(len(new_s)))
