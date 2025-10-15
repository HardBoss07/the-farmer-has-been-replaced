dirs = [North, East, South, West]

def move_dir(d, pos):
    move(d)
    if d == North:
        pos[1] += 1
    elif d == South:
        pos[1] -= 1
    elif d == East:
        pos[0] += 1
    elif d == West:
        pos[0] -= 1

def opposite(d):
    if d == North:
        return South
    if d == South:
        return North
    if d == East:
        return West
    if d == West:
        return East

def explore(pos, visited):
    if get_entity_type() == Entities.Treasure:
        harvest()
        return True

    key = str(pos[0]) + "," + str(pos[1])
    visited[key] = True

    for d in dirs:
        if can_move(d):
            # simulate next coordinate
            if d == North:
                new_key = str(pos[0]) + "," + str(pos[1] + 1)
            elif d == South:
                new_key = str(pos[0]) + "," + str(pos[1] - 1)
            elif d == East:
                new_key = str(pos[0] + 1) + "," + str(pos[1])
            else:
                new_key = str(pos[0] - 1) + "," + str(pos[1])

            if new_key not in visited:
                move_dir(d, pos)
                if explore(pos, visited):
                    return True
                move_dir(opposite(d), pos)
    return False

def solve_maze():
    pos = [0, 0]
    visited = {}
    explore(pos, visited)
    
