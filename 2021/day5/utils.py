def fetch_lines(filename):
    with open(filename) as f:
        data = f.read()
    lines = data.splitlines()
    lines = [tuple([tuple(map(int, coord.split(','))) for coord in line.split('->')]) for line in lines]
    return lines

def mark_map(seafloor, line):
    x1,y1,x2,y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    if x1 == x2:
        ymin, ymax = min(y1,y2), max(y1,y2)
        for j in range(ymin, ymax+1):
            seafloor[j][x1] += 1
    elif y1 == y2:
        xmin, xmax = min(x1,x2), max(x1,x2)
        for i in range(xmin, xmax+1):
            seafloor[y1][i] += 1
    elif abs(x2 - x1) == abs(y2 - y1):
        direction_vector = ((x2 - x1)//abs(x2 - x1), (y2 - y1)//abs(y2 - y1))
        painting_coords = [x1, y1]
        seafloor[y1][x1] += 1
        while painting_coords != [x2, y2]:
            painting_coords[0] += direction_vector[0]
            painting_coords[1] += direction_vector[1]
            print(line)
            print(painting_coords[0], painting_coords[0])
            seafloor[painting_coords[1]][painting_coords[0]] += 1

