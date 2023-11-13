# https://www.acmicpc.net/problem/4568

def LRU(cacheSize, word, idx):
    cache = []
    print('Simulation',idx)
    for w in word:
        if w =='!':
            print("".join(cache))
        else:
            if w not in cache:
                if len(cache) < cacheSize:
                    cache.append(w)
                else:
                    cache.pop(0)
                    cache.append(w)
            else:
                cache.remove(w)
                cache.append(w)
idx = 0
while True:
    idx+=1
    cache_input = list(map(str, input().split()))
    if len(cache_input)==1:
        break
    else:
        LRU(int(cache_input[0]), cache_input[1], idx)