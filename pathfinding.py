import heapq
import time
import os

# Directions: up, down, left, right
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_grid():
    width = int(input('Grid width: '))
    height = int(input('Grid height: '))
    print('Enter start position as x y (e.g. 0 0):')
    sx, sy = map(int, input().split())
    print('Enter end position as x y (e.g. 9 9):')
    ex, ey = map(int, input().split())
    print('How many obstacles?')
    n_obs = int(input())
    obstacles = set()
    print('Enter obstacle positions as x y (one per line):')
    for _ in range(n_obs):
        ox, oy = map(int, input().split())
        obstacles.add((ox, oy))
    return width, height, (sx, sy), (ex, ey), obstacles

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def in_bounds(pos, width, height):
    x, y = pos
    return 0 <= x < width and 0 <= y < height

def neighbors(pos, width, height, obstacles):
    for dx, dy in DIRS:
        nx, ny = pos[0] + dx, pos[1] + dy
        if in_bounds((nx, ny), width, height) and (nx, ny) not in obstacles:
            yield (nx, ny)

def print_grid(width, height, start, end, obstacles, path=None, open_set=None, closed_set=None):
    for y in range(height):
        row = ''
        for x in range(width):
            pos = (x, y)
            if pos == start:
                row += 'S '
            elif pos == end:
                row += 'E '
            elif obstacles and pos in obstacles:
                row += '# '
            elif path and pos in path:
                row += '* '
            elif open_set and pos in open_set:
                row += 'o '
            elif closed_set and pos in closed_set:
                row += 'x '
            else:
                row += '. '
        print(row)
    print()

def a_star_visual(width, height, start, end, obstacles):
    open_heap = []
    heapq.heappush(open_heap, (heuristic(start, end), 0, start, None))
    came_from = {}
    g_score = {start: 0}
    open_set = set([start])
    closed_set = set()

    while open_heap:
        _, cost, current, parent = heapq.heappop(open_heap)
        if current in came_from:
            continue
        came_from[current] = parent
        open_set.discard(current)
        closed_set.add(current)
        # Visualization step
        clear_console()
        path = reconstruct_path(came_from, start, current)
        print_grid(width, height, start, end, obstacles, path, open_set, closed_set)
        time.sleep(0.15)
        if current == end:
            break
        for neighbor in neighbors(current, width, height, obstacles):
            tentative_g = cost + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                heapq.heappush(open_heap, (tentative_g + heuristic(neighbor, end), tentative_g, neighbor, current))
                if neighbor not in closed_set:
                    open_set.add(neighbor)
    # Final path
    path = reconstruct_path(came_from, start, end)
    return path if path and path[0] == start else None

def reconstruct_path(came_from, start, end):
    path = []
    node = end
    while node and node in came_from:
        path.append(node)
        node = came_from[node]
    path.reverse()
    return path if path and path[0] == start else None

def main():
    print('A* Yol Bulma Görselleştirme (Konsol)')
    width, height, start, end, obstacles = get_user_grid()
    print('\nInitial grid:')
    print_grid(width, height, start, end, obstacles)
    input('Press Enter to start visualization...')
    path = a_star_visual(width, height, start, end, obstacles)
    clear_console()
    if path:
        print('Final path:')
        print_grid(width, height, start, end, obstacles, path)
    else:
        print('No path found!')
        print_grid(width, height, start, end, obstacles)

if __name__ == '__main__':
    main() 