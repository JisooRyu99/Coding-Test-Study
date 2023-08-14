def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        count=0
        while True:
            if count==len(skill_tree):
                break
            if skill_tree[count] not in list(skill):
                skill_tree = skill_tree.replace(skill_tree[count],"")
            else:
                count+=1
        
        if skill_tree == skill[:len(skill_tree)]: answer+=1
    return answer