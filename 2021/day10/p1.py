with open('input') as f:
    data = f.read()

lines = data.splitlines()
totalscore = 0

closechar = {'(':')','[':']','{':'}','<':'>'}
score = {')':3, ']':57, '}':1197, '>':25137}

for line in lines:
    stack = []
    for char in line:
        if char in ['(','[','{','<']:
            stack.append(char)
        else:
            if char != closechar[stack.pop()]:
                totalscore += score[char]
                break

print(totalscore)
