def solution(record):
    answer = []
    info = {}
    states = {"Enter":"들어왔습니다.", "Leave":"나갔습니다."}
    for state in record:
        state_split = state.split(" ")
        if len(state_split)==3:
            info[state_split[1]] = state_split[2]
            
    for state in record:
        state_split = state.split(" ")
        if state_split[0]=='Enter' or state_split[0]=='Leave':
            answer.append(f"{info[state_split[1]]}님이 {states[state_split[0]]}")
    return answer