# 촌수계산 https://www.acmicpc.net/problem/2644

n = int(input())

p1, p2 = map(int, input().split())

m = int(input())

graph = [[] for _ in range(101)]
count = 0

for _ in range(m):
    # x는 y의 부모
    x, y = map(int, input().split())
    graph[x].append(y)

# p1의 부모 알아내기
def findP1(p1):
    global count
    index = 0
    for i in range(1, 101):
        if p1 in graph[i]:
            count+=1
            index = i
            return index
        else:
            continue
    # 부모가 없는 최종 노드라면 자기자신을 반환
    index = p1
    return index

# p2의 부모 알아내기
def findP2(p2):
    global count
    index = 0
    for i in range(1, 101):
        if p2 in graph[i]:
            count+=1
            index = i
            return index
        else:
            continue
    # 부모가 없는 최종 노드라면 자기자신을 반환
    index = p2
    return index

def Search(p1, p2):
    global count
    last1 = False
    last2 = False

    P1 = findP1(p1)
    P2 = findP2(p2)

    # 두 노드의 부모가 동일하다면 출력 후 종료
    if P1 == P2:
        print(count)
        return
    
    for i in range(1, 101):
        if P1 in graph[P2]:
            print(count+1)
            return
        elif P2 in graph[P1]:
            print(count+1)
            return

    # 최종 노드인지 검사
    for i in range(1, 101):
        if P1 not in graph[i]:
            last1 = True
        else:
            break
    for i in range(1, 101):
        if P2 not in graph[i]:
            last2 = True
        else:
            break

    # 연관 없는 최종 노드뿐이라면 촌수 관계 없음
    if last1 == True and last2 == True:
        print(-1)
        return

    Search(P1, P2)

Search(p1, p2)