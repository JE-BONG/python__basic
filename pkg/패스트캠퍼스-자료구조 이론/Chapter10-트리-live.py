# 1. 트리(Tree) 구조
# 트리 : Node와 Branch를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조
# 실제로 사용 하는곳
# - 트리 중 이진트리(Binary Tree)형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용

# 2. 알아둘 용어
# Node        : 트리에서 데이터를 저장하는 기본 요소(데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
# Root Node   : 트리 맨 위에 있는 노드
# Level       : 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
# Parent Node : 어떤 노드의 다음 레벨에 연결된 노드
# Child Node  : 어떤 노드의 상위 레벨에 연결된 노드
# Leaf Node(Terminal Node) : Child Node가 하나도 없는 노드
# Sibling (Brother Node)   : 동일한 Parent Node를 가진 노드(즉, 형제)
# Depth : 트리에서 Node가 가질 수 있는 최대 Level

# 3. 이진 트리와 이진 탐색 트리(Binary Search Tree)
# 이진 트리 : 노드의 최대 Branch가 2인 트리★
# 이진 탐색 트리(Binary Search Tree, BST) : 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
# - ★왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음
# 출처 : https://www.mathwarehouse.com/programming/.gifs/binary-search-tree.php#binary-search-tree-insertion-node)

# ★탐색★에서 많이 쓰인다

# 4. 자료 구조 이진 탐색 트리의 장점과 주요 용도
# 주요 용도 : 데이터 검색(탐색)
# 장점 : 탐색 속도를 개선할 수 있다

# 이진트리와 정렬된 배열간의 탐색 비교
# 출처 : https://www.mathwarehouse.com/programming/.gifs/binary-serach-tree.php#binary-search-tree-insertion-node

# 5. 파이썬 객체지향 프로그래밍으로 Linked List 구현하기
# 5-1 노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 5-2 이진 탐색 트리에 데이터 넣기
# - 이진 탐색 트리 조건에 부합하게 데이터를 넣어야 한다.
class NodeMgmt:
    def __init__(self, head):
        self.head = head # 노드를 직접 넣는다.

    def insert(self, value) :
        self.current_node = self.head
        while True :
            if value < self.current_node.value:
                if self.current_node.left != None : # 왼쪽에 해당 노드가 존재한다면
                    self.current_node = self.cuurent_node.left
                else : # 노드가 존재하지 않는다면
                    self.current_node.left = Node(value) 
                    break # while문 종료
            else : # head에 있는 노드보다 값이 크다면
              if self.current_node.right != None :
                  self.current_node = self.current_node.right
              else :
                  self.current_node.right = Node(value)
                  break # while문 종료

head = Node(1)
BST = NoneMgmt(head)
BST.insert(2)

# 5-3 이진 탐색 트리 탐색
class NodeMgmt:
    def __init__(self, head):
        self.head = head # 노드를 직접 넣는다.

    def insert(self, value) :
        self.current_node = self.head
        while True :
            if value < self.current_node.value:
                if self.current_node.left != None : # 왼쪽에 해당 노드가 존재한다면
                    self.current_node = self.cuurent_node.left # 왼쪽에 더해준다.
                else : # 왼쪽에 노드가 존재하지 않는다면
                    self.current_node.left = Node(value) # 왼쪽에 노드를 만들어 준다.
                    break # while문 종료
            else : # head에 있는 노드보다 값이 크다면
              if self.current_node.right != None : # 오른쪽에 노드가 존재한다면
                  self.current_node = self.current_node.right # 오른쪽에 더해준다.
              else : # 오른쪽에 노드가 존재하지 않는다면
                  self.current_node.right = Node(value) # 오른쪽에 노드를 만들어 준다.
                  break # while문 종료

    def search(self, value):
        self.current_node = self.head
        # 이진 탐색 트리를 통한 데이터 검색
        while self.current_node : # None일 경우 종료 즉, 노드가 존재하는 경우 while문 계속 실행
            if self.current_node.value == value: # 입력받은 value값이 현재 head와 동일한지
                return True
            elif value < self.current_node.value:# 입력받은 value값이 현재 head값 보다 작다면
              self.current_node = self.current_node.left # 그 value값은 현재 왼쪽에 있다.
            else :
                self.current_node = self.current_node.right
        # while문 종료가 된다면 Node자체가 아예 없다는 것
        return False # 없음 표시

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
print(BST.search(-2))

# 5-4 이진 탐색트리 삭제
# 매우 복잡 경우를 나누어서 이해하는것이 좋다

# 5-4-1 Leaf Node 삭제 (★삭제할 브랜치(노드끼리 잇는 줄) 노드가 없을 때★)
# Leaf Node : Child Node가 없는 Node (즉, 해당노드 밑으로 아무 데이터도 없다.)
# 삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.

# 5-4-2 Child Node가 ★하나★인 Node 삭제
# 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.
# 삭제할 Node : 실제 삭제할 Node의 한단계 위 Parent Node
# Parent Node : head를 의미?

# 5-4-3 Child Node가 ★두개★인 Node 삭제
# 1. 삭제할 Node의 오른쪽 자식 중, ★가장 작은 값★을 삭제할 Node의 Parent Node가 가리키도록 한다

# <삭제할 Node의오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 할 경우>
# 1) 삭제할 Node의 오른쪽 자식 선택
# 2) 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
# 3) 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함
# 4) 해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
# 5) 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
# 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우에는 해당 Node의 본래 
# Parent Node의 왼쪽 Branch가 해당 오른쪽 Child Node를 가리키게 함

# 2. 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다










































