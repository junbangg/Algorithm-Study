import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.isHit = False
        self.children = dict()

    def hasChild(self, letter):
        if letter in self.children:
            return True
        return False

    def getChild(self, letter):
        return self.children[letter]

    def reset(self):
        self.isHit = False
        for nxt in self.children:
            self.children[nxt].reset()

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
    
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1 ,-1]
scoreDic = [0, 0, 0, 1, 1, 2, 3, 5, 11]
# word starts with one letter
def dfs(x, y, word, count, node, visited, grid):
    global total, score, maxWord 
    #1. 체크인
    visited[x][y] = 1
    word.append(grid[x][y])
    #2. 목적지에 도달하였는가
    if trie.search(word):
        # 점수 계산
        score += scoreDic[len(word)]
        total += 1
        if count > len(maxWord):
            maxWord = ''.join(word)
        elif count == len(maxWord) and ''.join(word) < maxWord:
            maxWord = ''.join(word)

    #3. 연결된 곳을 순회
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        #4. 가능한가?
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny] and node.hasChild(grid[nx][ny]):
            #5. 간다
            dfs(nx, ny, word, count+1, node.getChild(grid[nx][ny]), visited, grid)
    #6. 체크아웃
    visited[x][y] = 0
    word.pop()

# dfs는 내가 방문하고자 하는 곳에 대한 정보만 parameter로 쓰는게 좋음
trie = Trie()
N = int(input())
for _ in range(N):
    trie.insert(input().rstrip())

input()
tc = int(input().rstrip())
for i in range(tc):
    grid = [list(input().rstrip()) for _ in range(4)]
    visited = [[0] * 4 for _ in range(4)]
    total = score = 0
    maxWord = ''
    for i in range(4):
        for j in range(4):
            letter = grid[i][j]
            if trie.root.hasChild(letter):
                dfs(i, j, [], 1, trie.root.getChild(letter), visited, grid)

    print(score, maxWord, total, sep = ' ')
    trie.root.reset()
    input()