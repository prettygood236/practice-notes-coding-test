# w = input()
# vowels = ['A','E','I','O','U']
# answer = []

# def dfs(word):
#   for i in range(len(vowels)):
#     word = word + vowels[i]
#     if len(word) > 5:
#       return
#     answer.append(word)  #! 넣고!
#     dfs(word) #! 돌리고!
#     word = word[:-1] #! 뺴고! #?

# dfs('')
# print(answer.index(w)+1)



#? 와 진짜 도저히 모르겠다. 왜 시간 초과가 나는지 도저히 진짜 알수가 없다 삶이 너무나 힘들다

# from collections import deque
# # 900
# # board = [[0,0,0],[0,0,0],[0,0,0]]	
# # 3800
# # board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# # 2100 
# # board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	
# # 3200
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	


# def bfs(y,x):
#     n = len(board)
#     dp = [[[int(1e9)]*n for _ in range(n)] for _ in range(4)]
#     for i in range(4):
#         dp[i][0][0] = 0 
#     queue = deque()
#     dir = -1
#     cost = 0
#     queue.append((0,0,dir,cost))
# # right down left up
#     dy = [0,1,0,-1]  
#     dx = [1,0,-1,0]
#     while queue:
#         y,x,dir,cost = queue.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if board[ny][nx]:
#                 continue

#             c = cost + (100 if dir == i or dir == -1 else 600)
#             if dp[i][ny][nx] >= c:
#                 dp[i][ny][nx] = c
#                 queue.append((ny,nx,i,c))
#     answer = int(1e9)
#     for i in range(4):
#         answer = min(answer,dp[i][n-1][n-1])
#     return answer

# print(bfs(0,0))
