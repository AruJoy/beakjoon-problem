from sys import stdin
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def virus_fighting():
    for column in range(chalet_size):
        for row in range(chalet_size):
            if chalet[column][row] != 0:
                for d in range(4):
                    if 0 <= row + dx[d] < chalet_size and 0 <= column + dy[d] < chalet_size:
                        virus_diffusion[chalet[column][row]].append([column + dy[d], row + dx[d]])

    for virus in range(1, virus_types +1):
        while virus_diffusion[virus]:
                diffusion_coordinate = virus_diffusion[virus].pop()
                if chalet[diffusion_coordinate[0]][diffusion_coordinate[1]] == 0:
                    chalet[diffusion_coordinate[0]][diffusion_coordinate[1]] = virus
    return

chalet_size, virus_types = map(int, stdin.readline().split(' '))
virus_coordinate = [list() for _ in range(virus_types+1)]
virus_diffusion = deque([list() for _ in range(virus_types+1)])
chalet = list()

for column in range(chalet_size):
    line = list(map(int, stdin.readline().split(' ')))
    chalet.append(line)
    for rows in range(chalet_size):
        if line[rows] != 0:
            virus_coordinate[line[rows]].append([column, rows])

target_rows, target_column, look_time= map(int, stdin.readline().split(' '))
time = 0
while time < look_time:
    virus_fighting()
    time += 1

print(chalet[target_column-1][target_rows-1])