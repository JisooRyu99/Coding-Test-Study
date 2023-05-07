from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre = defaultdict(list)
    total_play = defaultdict(int)
    
    for idx, (g,p) in enumerate(zip(genres,plays)):
        total_play[g]+=p
        genre[g].append([idx,p])
    
    for k,v in sorted(total_play.items(), key=lambda x:-x[1]):
        answer.extend([(num, _)[0] for (num,_) in sorted(genre[k], key=lambda x:-x[1])][:2])
    return answer
