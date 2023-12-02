with open('input') as f:
    data = f.read()

lines = data.splitlines()

closechar = {'(':')','[':']','{':'}','<':'>'}
scoretable = {')':1, ']':2, '}':3, '>':4}

scores = []
for line in lines:

    stack = []
    iscorrupted = False
    for char in line:
        if char in ['(','[','{','<']:
            stack.append(char)
        else:
            if char != closechar[stack.pop()]:
                iscorrupted = True
                break

    if iscorrupted: continue
    
    score = 0
    while len(stack) != 0:
        score *= 5
        score += scoretable[closechar[stack.pop()]]

    scores.append(score)

print(sorted(scores)[len(scores)//2])
