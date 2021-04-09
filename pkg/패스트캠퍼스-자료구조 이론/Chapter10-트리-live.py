# # 1. 트리(Tree) 구조
# # 트리 : Node와 Branch를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조
# # 실제로 사용 하는곳
# # - 트리 중 이진트리(Binary Tree)형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용

# # 2. 알아둘 용어
# # Node        : 트리에서 데이터를 저장하는 기본 요소(데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
# # Root Node   : 트리 맨 위에 있는 노드
# # Level       : 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
# # Parent Node : 어떤 노드의 다음 레벨에 연결된 노드
# # Child Node  : 어떤 노드의 상위 레벨에 연결된 노드
# # Leaf Node(Terminal Node) : Child Node가 하나도 없는 노드
# # Sibling (Brother Node)   : 동일한 Parent Node를 가진 노드(즉, 형제)
# # Depth : 트리에서 Node가 가질 수 있는 최대 Level

# # 3. 이진 트리와 이진 탐색 트리(Binary Search Tree)
# # 이진 트리 : 노드의 최대 Branch가 2인 트리★
# # 이진 탐색 트리(Binary Search Tree, BST) : 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
# # - ★왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음
# # 출처 : https://www.mathwarehouse.com/programming/.gifs/binary-search-tree.php#binary-search-tree-insertion-node)

# # ★탐색★에서 많이 쓰인다

# # 4. 자료 구조 이진 탐색 트리의 장점과 주요 용도
# # 주요 용도 : 데이터 검색(탐색)
# # 장점 : 탐색 속도를 개선할 수 있다

# # 이진트리와 정렬된 배열간의 탐색 비교
# # 출처 : https://www.mathwarehouse.com/programming/.gifs/binary-serach-tree.php#binary-search-tree-insertion-node

# # 5. 파이썬 객체지향 프로그래밍으로 Linked List 구현하기
# # 5-1 노드 클래스 만들기
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# # 5-2 이진 탐색 트리에 데이터 넣기
# # - 이진 탐색 트리 조건에 부합하게 데이터를 넣어야 한다.
# class NodeMgmt:
#     def __init__(self, head):
#         self.head = head # 노드를 직접 넣는다.

#     def insert(self, value) :
#         self.current_node = self.head
#         while True :
#             if value < self.current_node.value:
#                 if self.current_node.left != None : # 왼쪽에 해당 노드가 존재한다면
#                     self.current_node = self.cuurent_node.left
#                 else : # 노드가 존재하지 않는다면
#                     self.current_node.left = Node(value) 
#                     break # while문 종료
#             else : # head에 있는 노드보다 값이 크다면
#               if self.current_node.right != None :
#                   self.current_node = self.current_node.right
#               else :
#                   self.current_node.right = Node(value)
#                   break # while문 종료

# head = Node(1)
# BST = NoneMgmt(head)
# BST.insert(2)

# # 5-3 이진 탐색 트리 탐색
# class NodeMgmt:
#     def __init__(self, head):
#         self.head = head # 노드를 직접 넣는다.

#     def insert(self, value) :
#         self.current_node = self.head
#         while True :
#             if value < self.current_node.value:
#                 if self.current_node.left != None : # 왼쪽에 해당 노드가 존재한다면
#                     self.current_node = self.cuurent_node.left # 왼쪽에 더해준다.
#                 else : # 왼쪽에 노드가 존재하지 않는다면
#                     self.current_node.left = Node(value) # 왼쪽에 노드를 만들어 준다.
#                     break # while문 종료
#             else : # head에 있는 노드보다 값이 크다면
#               if self.current_node.right != None : # 오른쪽에 노드가 존재한다면
#                   self.current_node = self.current_node.right # 오른쪽에 더해준다.
#               else : # 오른쪽에 노드가 존재하지 않는다면
#                   self.current_node.right = Node(value) # 오른쪽에 노드를 만들어 준다.
#                   break # while문 종료

#     def search(self, value):
#         self.current_node = self.head
#         # 이진 탐색 트리를 통한 데이터 검색
#         while self.current_node : # None일 경우 종료 즉, 노드가 존재하는 경우 while문 계속 실행
#             if self.current_node.value == value: # 입력받은 value값이 현재 head와 동일한지
#                 return True
#             elif value < self.current_node.value:# 입력받은 value값이 현재 head값 보다 작다면
#               self.current_node = self.current_node.left # 그 value값은 현재 왼쪽에 있다.
#             else :
#                 self.current_node = self.current_node.right
#         # while문 종료가 된다면 Node자체가 아예 없다는 것
#         return False # 없음 표시

# head = Node(1)
# BST = NodeMgmt(head)
# BST.insert(2)
# BST.insert(3)
# BST.insert(0)
# BST.insert(4)
# BST.insert(8)
# print(BST.search(-2))

# # 5-4 이진 탐색트리 삭제
# # 매우 복잡 경우를 나누어서 이해하는것이 좋다

# # 5-4-1 Leaf Node 삭제 (★삭제할 브랜치(노드끼리 잇는 줄) 노드가 없을 때★)
# # Leaf Node : Child Node가 없는 Node (즉, 해당노드 밑으로 아무 데이터도 없다.)
# # 삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.

# # 5-4-2 Child Node가 ★하나★인 Node 삭제
# # 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.
# # 삭제할 Node : 실제 삭제할 Node의 한단계 위 Parent Node
# # Parent Node : head를 의미?

# # 5-4-3 Child Node가 ★두개★인 Node 삭제
# # 1. 삭제할 Node의 오른쪽 자식 중, ★가장 작은 값★을 삭제할 Node의 Parent Node가 가리키도록 한다

# # <삭제할 Node의오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 할 경우>
# # 1) 삭제할 Node의 오른쪽 자식 선택
# # 2) 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
# # 3) 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함
# # 4) 해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
# # 5) 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
# # 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우에는 해당 Node의 본래 
# # Parent Node의 왼쪽 Branch가 해당 오른쪽 Child Node를 가리키게 함

# # 2. 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다

# # 5.5 이진 탐색 트리 삭제 코드 구현과 분석
# # 1) 삭제할 Node가 없는 경우도 처리해야 한다.
# # - 이를 위해 삭제할 Node가 없는 경우는 False를 리턴하고, 함수 종료

# # def delete(self, value):
#     searched = False # 삭제할 Node의 상태를 의미
#     self.current_node = self.head # 삭제할 Node
#     self.parent = self.head # 삭제할 Node의 부모Node를 의미
#     while self.current_node:# Node가 존재할 경우 실행
#         if self.current_node.value == value: # 해당 Node를 찾은 경우
#             searched = True
#             break
#         elif value < self.current_node.value: # 입력받은 값이 해당 위 값보다 작을 경우 즉, 왼쪽에 있는 경우
#             self.parent = self.current_node
#             self.current_node = self.current_node.left
#         else:
#             self.parent = self.current_node
#             self.current_node = self.current_node.right


#     if searched == False:
#         return False

# ## 이후부터 Case들을 분리해서 코드 작성 ##

# # 5.5-2
# # Case1 : 삭제할 Node가 Leaf Node인 경우
# # current_node = 삭제할 Node
# # parent_node = 삭제할 Node의 부모

# # self.current_node가 삭제할 Node
# # self.parent는 삭제할 Node의 Parent Node인 상태
# if self.current_node.left == None and self.current_node == None :
#     if value < self.parent_node:
#         self.parent_left = None
#     else : 
#         self.parent_right = None
#     del self.current_node # 객체 메모리상에서도 삭제

# # 5.5-3 
# # Case2 : 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
# # type1 : 삭제할 Node의 Child Node가 왼쪽에 있는 경우 
# # type2 : 삭제할 Node의 Child Node가 오른쪽에 있는 경우
# # parent_node : 가장 상단에 있는 Node
# # current_node: 상단 아래에 있는 Node
# # current_node_left   : 가장 아래에 있는 왼쪽 Node
# # current_node_right  : 가장 아래에 있는 오른쪽 Node

# # 1) 삭제할 Node의 Child Node가 왼쪽에 있는 경우(자신보다 작은값의 경우)
# if self.current_node_left != None and self.current_node_right == None :
#     # 입력 받은 값이 삭제할 Node의 값보다 작은 경우
#     if value < self.parent.value: 
#         # 가장 상단에 있는 값이랑 연결되어야 하기 때문에 
#         # parent_left에는
#         # 삭제할 Node의 왼쪽에 위치해 있는 Child Node값을 연결해준다.
#         self.parent_left = self.current_node_left
#     else:
#         self.parent_right = self.current_node_left
# # 2) 삭제할 Node의 Child Node가 오른쪽에 있는 경우(자신보다 큰 값의 경우)
# elif self.current_node_right != None and self.current_node_left == None:
#     if value < self.parent.value:
#         self.parent_left = self.current_node_right
#     else :
#         self.parent_right = self.current_node_right

# # 5.5-3 
# # Case3 : 삭제할 Node가 Child Node를 두 개 가지고 있을 경우(삭제할 Node가 Parent Node 왼쪽에 있을 경우)
# # 1. 기본 사용 가능 전략
# # 1) 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다
# # 2) 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다

# # 2. 기본 사용 가능 전략 중, 1번 전략을 사용하여 코드를 구현
# # 경우의 수가 또 다시 두가지가 있음
# # Case3-1-1 : 삭제할 Node가 Parent Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 
# #             가장 작은 값을 가진 Node의 Child Node가 없을 때

# # Case3-1-2 : 삭제할 Node가 Parent Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중,
# #             가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때
# # 가장 작은 값을 가진 Node의 Child Node가 왼쪽에 있을 경우는 없음 이유는 왼쪽 Node가 있다는 것은
# # 해당 Node보다 더 작은 값을 가진 Node가 있다는 뜻

# # 1) 삭제할 Node가 Child Node를 두개 가지고 있는 경우 
# # Case3
# if self.current_node_left != None and self.current_node_right != None :
#     # case 3-1
#     # 1) 삭제할 Node가 왼쪽에 있는 경우
#     if value < self.parent.value: 
#         self.change_node = self.current_node.right
#         self.change_node_parent = self.current_node_right
        
#         # 가장 작은값을 찾기 위해 순환
#         # change_node에 왼쪽에 값이 있는 경우 실행
#         while self.change_node_left != None: 
#             self.change_node_parent = self.change_node
#             self.change_node = self.change_node_left
#         self.change_node_parent.left = None
        
#         if self.change_node_right != None:
#             # change_node_right를 change_node_parent에 왼쪽에 위치시킨다.
#             self.change_node_parent.left = self.change_node_right
#         else :
#             self.change_node_parent.left = None

#         self.parent_left = self.change_node # 가장 상단에 있는 Parent Node의 왼쪽에 배치

#         # change Node가 가장 상단 Parent Node의 왼쪽에 위치 후 
#         # change Node_left 와 right와 연결해야 한다.
#         self.change_node_right = self.current_node_right
#         self.change_node_left = self.change_node_left

#     # 2) 삭제할 Node가 오른쪽에 있는 경우
#     else :
#         self.change_node = self.current_node_right
#         self.change_node_parent = self.current_node_right

#         # 가장 작은 값을 찾기 위해 순환
#         while self.change_node_left != None:
#             self.change_node_parent = self.change_node
#             self.change_node = self.change_node_left
#         if self.change_node_right != None:
#             self.change_node_parent.left = self.change_node_parent_right
#         else:
#             self.change_node_parent.left = None
#         self.parnet_node_right = self.change_node
#         self.change_node_left = self.current_node_left
#         self.change_node_right = self.current_node_right
        
# 파이썬 전체 코드 구현
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head
    
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)

    def search(self, value):
        # 삭제할 노드 탐색
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

        # Case1 : 삭제할 Node가 Leaf Node인 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # Case2 : 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # Case3 : 삭제할 Node가 Child Node를 두 개 가지고 있을 경우(삭제할 Node가 Parent Node 왼쪽에 있을 경우)
        elif self.current_node.left != None and self.current_node.right != None:
            # Case3-1 : 삭제할 Node가 왼쪽에 있는 경우
            if value < self.parent.value:
                self.change_node = self.change_node.right
                self.change_node_parent = self.current_node.right
                # 가장 작은 값을 찾기 위한 순환루트
                while self.change_node.left != None:
                      self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent_left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            
            # Case3-2 : 삭제할 Node가 오른쪽에 있는 경우 
            else:
                self.change_node = self.change_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                      self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
        
        return True

# 5.5-4 파이썬 전체 코드 테스트
# random 라이브러리 활용
# random/randint(첫번째 숫자, 마지막 숫자): 첫번째부터 마지막 숫자 사이 랜덤 출력
# ex) random.randint(0, 99):0~99 랜덤 선택

# 1 ~ 999 숫자 중 임의로 100개를 추출 후, 이진 탐색 트리에 입력, 검색, 삭제
import random

# 1) 1 ~ 999 중 100 개의 숫자 랜덤 선택 
bst_nums = set() # 중복과 순서 방지 위한 set() 활용
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999)) # add함수를 통해 bst_nums 길이가 100이 전까지 추가
# print(bst_nums)

# 2) 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 3) 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print('search faild', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums) # 인덱스로 접근하기 위한 list생성
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete faild', del_num)

# 6. 이진 탐색 트리의 시간 복잡도와 단점
# 6-1 시간 복잡도 (탐색 시)
# depth(트리의 높이)를 h라고 표기한다면, O(h)
# n개의 노드를 가진다면 시간복잡도는 O(logn)
# 참고: Big(O) 표기법에서 logn에서의 log밑은 10이 아닌 2이다.
# ★한번 실행시 50%의 실행할 수도 있는 명령을 제거한다는 의미, 즉 50%의 확률 실행시간을 단축

# 6-2 이진 탐색 트리 단점
# 평균 시간 복잡도는 O(logn) 이지만
# - 이는 트리가 균형있게 잡힌경우에 시간복잡도 이지만
# ★반대로, 작은 수가 가장 위(head)에 있는 경우 
# 최악의 경우는 Linked List 등과 동일한 성능을 가지게 된다( O(n) )

# 탐색의 경우
# 배열의 경우는 o(n)정도 시간이 걸리지만
# 이진 탐색의 경우 O(logn)의 시간이 걸린다. 















        



















        































    






































































