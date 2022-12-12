data = [line.strip().split(' ') for line in open('test.txt', 'r')]

def move_head(head, direction):
    match direction:
        case 'U':
            head[1] += 1
        case 'D':
            head[1] -= 1
        case 'L':
            head[0] -= 1
        case 'R':
            head[0] += 1
    
def is_touching(head, tail):
    return abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2
    
head = [0, 0]
tail = [0, 0]
previous_head = [0, 0]
visited_spots = set()
for line in data:
    direction = line[0]
    amount = int(line[1])
    for _ in range(0, amount):
        previous_head = head.copy()
        move_head(head, direction)  
        if not is_touching(head, tail):
            tail = previous_head
        visited_spots.add(tuple(tail))

print(len(visited_spots))
