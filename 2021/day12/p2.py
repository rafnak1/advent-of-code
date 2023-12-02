def visited_small_cave_twice(history):
    for caveid in history:
        if caveid.islower():
            if history.count(caveid) == 2:
                return True
    return False

with open('input') as f:
    data = f.read()

paths_from = {}
for line in data.splitlines():
    t = line.split('-')
    if 'start' in t:
        paths_from['start'] = paths_from.get('start', set()) 
        paths_from['start'].add(t[0] if t.index('start') == 1 else t[1])
    elif 'end' in t:
        the_other_one = t[0] if t.index('end') == 1 else t[1]
        paths_from[the_other_one] = paths_from.get(the_other_one, set())
        paths_from[the_other_one].add('end')
    else:
        paths_from[t[0]] = paths_from.get(t[0], set())
        paths_from[t[0]].add(t[1])
        paths_from[t[1]] = paths_from.get(t[1], set())
        paths_from[t[1]].add(t[0])

def count(caveid, history):
    global paths_from
    if caveid == 'end': return 1
    if caveid.islower() and caveid in history and visited_small_cave_twice(history): return 0
    history.append(caveid)
    return sum([count(caveid2, history.copy()) for caveid2 in paths_from[caveid]])

print(count('start', []))
