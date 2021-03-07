# 뱀
from collections import deque

queue = deque()

N = int(input())
K = int(input())

count = 0
list_heading = []
old_heading = None
new_heading = None
INF = float('inf')

# 전체 그래프를 0으로 초기화
graph = [[0 for _ in range(N)] for _ in range(N)]

# 사과가 있는 곳은 1로 변경
for _ in range(K):
    temp1, temp2 = map(int, input().split())
    graph[temp1-1][temp2-1] = 1

L = int(input())

for _ in range(L):
    X, C = input().split()
    list_heading.append([int(X), C])

# 처음 (1, 1)을 큐에 넣는다. 초기 방향은 오른쪽
queue.append([1, 1])
old_heading = 'R'

# 큐 중복검사 함수 - 몸통 충돌
def col_body(par_queue):
    temp_len = len(par_queue)
    for i in range(1, temp_len):
        if par_queue[0] == par_queue[i]:
            return False
    return True

def col_wall(par_queue):


# Baam 방향 함수
def move(par_queue, par_old_head, par_new_head):
    if par_old_head == 'R' & par_new_head == 'D':
        par_queue[0][0] += 1
        par_old_head = 'D'
    elif par_old_head == 'R' & par_new_head == 'L':
        par_queue[0][0] -= 1
        par_old_head = 'U'

    if par_old_head == 'L' & par_new_head == 'D':
        par_queue[0][0] -= 1
        par_old_head = 'U'
    elif par_old_head == 'L' & par_new_head == 'L':
        par_queue[0][0] += 1
        par_old_head = 'D'

    if par_old_head == 'U' & par_new_head == 'D':
        par_queue[0][1] += 1
        par_old_head = 'R'
    elif par_old_head == 'R' & par_new_head == 'L':
        par_queue[0][1] -= 1
        par_old_head = 'U'

    if par_old_head == 'L' & par_new_head == 'D':
        par_queue[0][1] -= 1
        par_old_head = 'U'
    elif par_old_head == 'L' & par_new_head == 'L':
        par_queue[0][1] += 1
        par_old_head = 'D'

# 사과를 만나는 함수
def apple(par_queue):
    
        

while collision(queue):
    move(queue, old_heading, new_heading)
    print(count)

