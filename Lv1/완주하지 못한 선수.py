def solution(participant, completion):
    import collections
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    for key,value in answer.items():
        return key
        
