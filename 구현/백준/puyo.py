from collections import deque
puyo = []
for i in range(12) :
  temp = list(input())
  puyo.append(temp)

dx= [1,-1,0,0]
dy = [0,0,1,-1]

##터질 수 있는 푸요 찾기
def bfs(x,y) :
  q = deque()
  q.append((x,y))
  ##x,y좌표를 확인 그리고 그 근방 4ㅐ 확인
  temp.append((x,y))
  while q :
    #q의 모든 원소 a,b에 대해
    a,b = q.popleft()
    for i in range(4):
      ##해당 큐의 상하좌우 원소 nx에 대해
      nx = a+dx[i]
      ny = b+dy[i]
      ##이때 nx가 세로로 12미만, ny가 6미만
      ##그리고 원래 x,y랑 원소가 같고
      if 0<= nx <12and 0<=ny <6 and puyo[nx][ny] == puyo[x][y] and visited[nx][ny] == 0 :
        q.append((nx,ny))
        temp.append((nx,ny))
        visited[nx][ny] = 1


def delete(temp) :
  for a,b in temp :
    puyo[a][b] = "."

def down():
  for i in range(6) :
    for j in range(10,-1,-1) :
      for k in range(11,j,-1) :
        if puyo[j][i] != "." and puyo[k][i] == "." :
          puyo[k][i] = puyo[j][i]
          puyo[j][i] = '.'
          break

ans = 0
while 1:
    flag = 0
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                temp = []
                bfs(i,j)
                # 4칸확인
                if len(temp) >= 4:
                    flag = 1
                    delete(temp)
    if flag == 0:
        break
    down()
    ans += 1

print(ans)
