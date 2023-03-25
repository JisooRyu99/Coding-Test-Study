def solution(s):
    stack=[]    # 빈 list 만들어주기
    for i in s:
        if not stack:   
            stack.append(i)
            continue

        if stack[-1]==i:    # stack의 마지막 원소와 i와 같으면 pop
            stack.pop()
        else: stack.append(i)   # 같지 않으면 stack에 넣기

    if not stack:
        return 1    # stack에 아무것도 없으면 1
    else: return 0    # stack에 하나라도 있으면 0
