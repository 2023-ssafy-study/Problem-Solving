import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def makeTree(currentNode, parent):
    for Node in E[currentNode]:
        if Node != parent:
            tree[currentNode].append(Node)  # add Node to currentNode’s child
            parents[Node] = currentNode  # set Node’s parent to currentNode
            makeTree(Node, currentNode)


def countSubtreeNodes(currentNode):
    size[currentNode] = 1  # 자신도 자신을 루트로 하는 서브트리에 포함되므로 0이 아닌 1에서 시작한다.
    for childNode in tree[currentNode]:
        countSubtreeNodes(childNode)
        size[currentNode] += size[childNode]


N, R, Q = map(int, input().split())
E = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

tree = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)  # 노드 i의 부모
size = [0] * (N + 1)  # 노드 i를 루트로 하는 서브트리에 속한 정점 수
makeTree(R, -1)  # R을 루트로 하는 트리
countSubtreeNodes(R)  # 각 정점을 루트로 하는 서브트리에 속한 정점 수 계산

for _ in range(Q):
    print(size[int(input())])
