from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    dungeons.sort(key=lambda x:(x[0],x[1]), reverse=True)
    for d in list(permutations(dungeons)):
        cnt=0
        least = k
        for i in d:
            if i[0] <= least:
                least-=i[1]
                cnt+=1
            else: break
        answer = max(cnt, answer)
    return answer