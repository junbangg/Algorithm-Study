import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.isHit = False
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word : str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.isEnd = True

    def search(self, word : str)-> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]
# 여기다가 isHit 구현
        if node.isEnd and not node.isHit:
            node.isHit = True
            return True
        return False
    
    def hasChild(self, letter):
        return letter in self.root.children

    def reset(self):
        def subReset(node):
            for nxt in node.children:
                nxt.isEnd = False
                nxt.isHit = False
                subReset(nxt)
        subReset(self.reset)

# dfs 에 트라이를 직접 넣지말고, 그냥 루트 노드를 넣는게 맞을 수도 있음. 강사는 그렇게 함


dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1 ,-1]
score = [0, 0, ]
# word starts with one letter
def dfs(x, y, word, trie, visited, grid):
    global sum, count, words
    #1. 체크인
    visited[x][y] = 1
    word.append(grid[x][y])
    #2. 목적지에 도달하였는가
    # if node.isEnd and not node.isHit: node.isHit = True
    if trie.search(word):
        # 점수 계산
        sum += score[len(word)]
        count += 1
        words.append(''.join(word))

    #3. 연결된 곳을 순회
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        #4. 가능한가?
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]: # and node.hasChild(nx,ny)
            #5. 간다
            dfs(nx, ny, node.getChild[grid[nx][ny]], visited, grid)
    #6. 체크아웃
    visited[x][y] = 0
    word.pop()

    

# dfs는 내가 방문하고자 하는 곳에 대한 정보만 parameter로 쓰는게 좋음


trie = Trie()
N = int(input())
for _ in range(N):
    trie.insert(input().rstrip())

input()
tc = int(input())
for i in range(tc):
    grid = [list(input().rstrip()) for _ in range(4)]
    visited = [[0] * 4 for _ in range(4)]
    sum = count = 0
    words = []
    for i in range(4):
        for j in range(4):
            letter = grid[i][j]
            if trie.hasChild(letter):
                dfs(i, j, [], trie, visited, grid)

    print(sum)
    print(count)
    print(sorted(words, key = len))

    trie.reset()
    if i != tc-1:
        input()
    


     