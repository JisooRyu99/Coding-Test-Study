https://www.acmicpc.net/problem/1105
  
  
import sys
L, R =sys.stdin.readline().split()

cnt=0
if len(L) != len(R):
    print(cnt)
else:
    for i in range(len(L)):
        if L[i] == R[i] =='8':
            cnt+=1
        if L[i]!=R[i]:
            break
    print(cnt)

< 풀이 방식 >
1. 두 숫자의 길이가 같은지
2. 다르다면 반복문을 통해 각 자리에 8이 포함되어 있는지 확인. (count 하기)
3. 두 자연수의 자릿수의 값이 다르다면 8을 안세도 됨 break

---------------------------------------------------------

< 시간 초과 >

import sys

L, R = map(int, sys.stdin.readline().split(" "))

cnt= 15

for i in range(L, R+1):
    cnt_temp = str(i).count('8')
    if cnt_temp>0:
        if cnt>=cnt_temp:
            cnt=cnt_temp
    else:
        cnt=0
        break
print(cnt)

1. count 수를 default값으로 15로 지정 (15자리가 넘는 수가 없음)
2. count()를 이용해서 8의 개수를 세기
3. 이전에 8을 count한 값과 비교하여 작은 값을 유지하도록 함
