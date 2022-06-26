'''
문제
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다. N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.
'''



l = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


A.sort()
B.sort(reverse=1)
print(A)
print(B)
sum=0
for i in range(l):
    sum += A[i]*B[i]
print(sum)

'''
< 설명 >
1. A가 작은 것과 B가 큰 것을 곱해야지 최솟값을 구할 수 있음
2. A는 sort(), B는 sort(reverse=1)를 해줌
3. 정렬된 값 곱해서 더해줌 => 최솟값 완성
