from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque([begin, 0])
    v = [0 for i in range(len(words))]
    if target not in words:
        return 0
    
    while queue:
        word, cnt = queue.popleft()
        if word==target:
            return cnt
        for i in range(len(words)):
            tmp_cnt = 0
            if not v[i]:
                for j in range(len(word)):
                    if word[j]!=words[i][j]:
                        tmp_cnt+=1
                if tmp_cnt==1:
                    queue.append([words[i], cnt+1])
                    v[i]=1
            
    return answer