'''# 20, 30 테케 실패

def time_(s, e):
    start = s.split(':')
    end = e.split(':')

    time = int(end[0])*60 + int(end[1]) - int(start[0])*60 + int(start[1])

    return time
    
def solution(m, musicinfos):
    answer = []
    m = m.replace('C#','Z').replace('D#','X').replace('F#','Y').replace('G#','W').replace('A#','V')
    
    for music in musicinfos:
        music = music.split(',')
        music[3] = music[3].replace('C#','Z').replace('D#','X').replace('F#','Y').replace('G#','W').replace('A#','V')
        times = time_(music[0], music[1])        
        
        word = ''.join(music[3]*(times//len(music[3]))) + music[3][:times%len(music[3])]
        if m in word:
            answer.append([times,music[2]])
    answer.sort(key=lambda x:x[0])

    return answer[0][1] if answer else "(None)"'''
    
    
def replacement(s):
    return s.replace('C#','Z').replace('D#','X').replace('F#','Y').replace('G#','W').replace('A#','V')
    
def solution(m, musicinfos):
    answer = []
    m = replacement(m)
    for i,musicinfo in enumerate(musicinfos):
        start, end, name, music = musicinfo.split(',')
        music = replacement(music)
        start, end = list(map(int,start.split(':'))),list(map(int,end.split(':')))
        play_time = (end[0]-start[0])*60 + end[1]-start[1]
        if play_time < len(music):
            music = music[:play_time]
        else:
            music = music*(play_time//len(music)) + music[:(play_time%len(music))]
        
        if m in music:
            answer.append([name, play_time, i])
    answer.sort(key=lambda x:(-x[1], x[0]))
    
    return answer[0][0] if answer else '(None)'
    

# 음악 제목, 끝난 시각, 악보
# C, C#, D, D#, E, F, F#, G, G#, A, A#, B -> 12개
# 1분에 1개씩

# 조건이 일치하는 경우가 여러 개일 경우 : 재생된 시간이 긴 음악 제목 바놘
# 
    

# 음악 제목, 끝난 시각, 악보
# C, C#, D, D#, E, F, F#, G, G#, A, A#, B -> 12개
# 1분에 1개씩

# 조건이 일치하는 경우가 여러 개일 경우 : 재생된 시간이 긴 음악 제목 바놘
# 