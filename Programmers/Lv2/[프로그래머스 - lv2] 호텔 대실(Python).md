
## 문제 설명
호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

## 제한사항
- 1 ≤ book_time의 길이 ≤ 1,000
    - book_time[i]는 ["HH:MM", "HH:MM"]의 형태로 이루어진 배열입니다
        - [대실 시작 시각, 대실 종료 시각] 형태입니다.
    - 시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00" 부터 "23:59" 까지로 주어집니다.
        - 예약 시각이 자정을 넘어가는 경우는 없습니다.
        - 시작 시각은 항상 종료 시각보다 빠릅니다.

## 입출력 예
![image](https://github.com/user-attachments/assets/e12eee4d-defe-4a08-a7a3-bbc7f0d2947d)


## 접근
1. 입실시간을 기준으로 정렬
2. room이 비어있는지 체크 </br>
    2-1. room이 비어 있다면 입실 </br>
    2-2. room이 비어있지 않다면 새로운 room 배정
3. 퇴실자 체크


## 구현 Code
```python 
from heapq import heappush, heappop
def convert_time(t):
    return int(t[:2])* 60 + int(t[3:])

def solution(book_time):
    rooms = []
    re_book_time = [(convert_time(s), convert_time(e)) for s, e in book_time]
    re_book_time.sort(key = lambda x:(x[0], x[1]))
    for s, e in re_book_time:
        if rooms and rooms[0] <= s:
            heappop(rooms)
        heappush(rooms, e + 10)


    return len(rooms)

solution(book_time)
```

## 주의점
- [입실 시간, 퇴실 시간] HH:MM 포멧이기 때문에 시간을 분으로 환산시켜줘야한다.
- 퇴실에 청소시간 10분을 추가해줘야 한다.
