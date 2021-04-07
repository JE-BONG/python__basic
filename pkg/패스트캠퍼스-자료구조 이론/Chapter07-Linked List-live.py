# # 대표적인 데이터 구조 : 링크드 리스트(Linked List)
# # 1. 구조
# # - 연결 리스트
# # - 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
# # - 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 구조
# # - 리스트 타입 존재 / 기능 지원
# #
# # 2. 기본 구조와 용어
# # - 노드(Node) : 데이터 저장 단위(데이터값, 포인터) 로 구성
# # - 포인터(Pointer) : 각 노드 안에서, 노드와의 연결 정보를 가지고 있는 공간

# # 배열은 데이터를 넣기만 하면되지만
# # Linked List는 자신의 데이터 + 다음데이터(Pointer)를 가르키는 주소를 포함해 
# # 하나의 데이터로 인식 즉, Node라고 한다.
# # Linked List 배열에 첫번째 데이터를 찾으면 해당 배열에 있는 데이터를 모두 찾을 수 있다.

# # 파이썬 객체지향 문법 이해 참고
# # https://www.fun-coding.org/PL&OOP1-3.html

# # Linked List의 장단점
# # <장점>
# # - 미리 데이터 공간을 할당하지 않아도 된다
# # - 배열은 미리 추가해야 한다

# # <단점>
# # - 연결을 위한 별도 데이터 공간(pointer)까지 필요, 저장공간 효율성이 높지 않다
# # - 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느리다
# # - 중간 데이터 삭제 시, 앞 뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요
# # 연습
# class Node:    
#         # Node를 만들기 위한 초기화 작업 
#     def __init__(self, data): 
#         self.data = data # 데이터 저장
#         self.next = None # 다음 주소를 가르킬 포인터 # 현재 아직 없음

# # 객체 두개 만들기
# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2
# head = node1 # Linked List로 된 배열을 찾기 위해 가장 앞에 있는 데이터의 주소를 head변수에 저장

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# # Linked List로 데이터 추가하기
# class Node:
#     def __init__(self, data, next=None): # 또 다른 생성자
#         self.data = data
#         self.next = next()

#     def add(data):
#         node = head            # LinkedList에 있는 맨 앞에 데이터 주소를 의미
#                                # 마지막 node에 데이터를 입력해야 하기 때문에 while문으로 node의 존재를 찾는다.
#         while node.next:       # node(맨 앞)에 있는 그 다음 데이터(next)가 있다면 주소가 존재한다면
#             node = node.next
#                                # node.next가 None면 아래 코드 실행 / 현재 node는 마지막 node이고 None상태이다.
#         node.next = Node(data) # 마지막 node에 data를 넣는다.

# node1 = Node(1)
# head = node1 # Linked List로 된 배열을 찾기 위해 가장 앞에 있는 데이터의 주소를 head변수에 저장

# for index in range(1, 10) :    # range : 1 ~ 9
#     add(index)

# node = head                    # head에는 맨앞에 Node값이 있다.
# while node.next :              # node에 None이 아닐 경우 실행 
#     print(node.data)
#     node = node.next
# print(node.data)
# --------------------------------------------------------------------------------------------------------------
# # 1번 데이터와 2번 데이터 사이에 1.5데이터 넣기(데이터 연결의 재구성)
# node3 = Node(1.5)              # 1과 2사이에 넣기 위함
# node = head                    # 맨 앞에 Node값이 있다.
# search = True     
# while search :

#     # 1번 데이터를 찾아야 1번과 2번사이에 값을 넣을 수 있기 때문에
#     # if문을 통해 1번이 맞으면 false로 설정 후 while문 종료
#     if node.data == 1 :        # 현재 Node(head)의 데이터가 1인지 확인 후
#         search = False         # while문 종료
#     else :
#     # 1이 아니라면 아래 코드 실행  
#         node = node.next

# node_next = node.next          # head앞에 주소를 node_next변수에 넣어준다.
# node.next = node3              # head앞에 있는 데이터 주소에 node3(1.5)를 넣는다.
# node3.next = node_next         # node3(1.5)앞에 있는 2에 head 앞 데이터(2)를 넣어서 1 -> 1.5 -> 2를 완성

# node = head
# while node.next :
#     print(node.data)
#     node = node.next
# print(node.data)

# --------------------------------------------------------------------------------------------------------------
# 5. 파이썬 객체지향 프로그래밍으로 Linked List 구현하기
class Node :
    def __init__(self, data, next=None):
        self.data = data
        self.next = next            # 데이터 주소

class NodeMgmt:
    def __init__(self, data):       # 디폴트 생성자
        self.head = head            # 맨 앞의 Node의 주소

    def add(self,data) :
        # 맨 뒤에 넣는다.
        if self.data == "" :        # data가 없다면 즉, LiekedList가 만들어진게 없다면
            self.head = Node(data)  # head 값에 없다면 Linked List가 없다 생각하고 head에 값을 data를 넣는다.
        else :
            node = self.head        # data가 있다면 즉 만들어진 LinkedList가 있고 data가 있다는 의미
            while node.next :       # head의 next(다음 데이터 주소)가 있다면 확인
                node = node.next    # node(head)에 다음 데이터 주소를 넣는다
            # node가 None인 경우
            node.next = Node(data)  # node(head)에 다음 주소에 데이터를 넣는다

    def desc(self) :                # Linked List를 순회
        node = self.head
        while node :                # node(head)가 존재한다면 node는 1->2->3 이런식으로 다음 데이터주소가 존재한다면 아래 코드 실행
            print(node.data)        # node의 있는 데이터들을 모두 출력
            node = node.next        # node는 매번 바뀐다 next를 통해 다음 데이터주소로 가서 데이터 조회 후 출력 후 다시 다음 데이터주소로 바꾼 후 while문 실행여부 확인

# 6. Linked List의 복잡한 기능2(특정 Node를 삭제)
# 다음 코드는 위의 코드에서 delete 메서드만 추가한 것이므로 해당 메서드만 확인
# 1. head삭제
# 2. 마지막 노드 삭제(삭제할 node의 주소값을 참조하고 있는 노드의 주소값 바꾸기)
# 3. 중간 노드 삭제(앞에 있는 주소값을 삭제한 다음에 있는 데이터 주소로 바꾸기)

    def  delete(self, data):
        if self.head == '' :           # linkedList가 만들어 지지 않았다면 / head가 없다면
            print('해당 값을 가진 노드가 없습니다')
            return
            
        # 1. LinkedList의 head(가장 앞)을 삭제 시 
        if self.head == data:          # head에 데이터가 있다면
            temp = self.head           # temp란 임시변수에 객체를 삭제하기 위해 저장
            self.head = self.head.next # head(가장 앞)는 그 다음에 있는 데이터주소가 head로 지정
            del temp                   # 해당 주소를 넣으면 del 내장함수를 통해 삭제된다.
        else :
            # 2. 중간 데이터 삭제
            node = self.head           # 삭제된 헤드의 다음 Node
            while node.next :          # head 다음에 있는 Node의 주소가 있다면
                    # head 다음에 있는 Node의 데이터가 있다면
                if node.next.data == data :
                    temp = node.next   # temp란 임시변수에 Node 주소를 임시로 넣어놓고
                    # head 다음에 있는 주소에 바로 다음 Node주소를 넣는다.
                    # 즉, 3번째에 있는 데이터 주소를 당겨서 head바로 앞에 있는
                    # 2번째 데이터에 3번째 데이터를 저장시킨다.
                    # node.next : Node의 주소를 의미
                    node.next = node.next.next 
                    del temp # 임시 저장해두었던 기존 node.next의 주소 삭제
                else:
                    # 내가 찾는 주소의 데이터가 아니라면
                    # head에 있는 다음 데이터 주소로 이동
                    node = node.next
linkedlist1 = NodeMgmt(0) # head 생성
linkedlist.desc()

# 1. LinkedList의 head에 있는 값 삭제 경우
linkedlist1.delete(0) # head는 0번째

# 1-2 여러개의 데이터 추가
for i in range(1, 11) :
    linkedlist1.add(data)
linkedlist1.desc() # 데이터 추가 후 출력

# 2. 여러개의 데이터 추가 후 중간에 4번 데이터 삭제
linkedlist1.delete(4) 
# 출력
linkedlist1.desc()

# 3. 마지막 데이터 삭제
linkedlist1.delete(linkedlist1.index(10)) # 10을 가진 데이터의 인덱스 삭제
linkedlist1.delete(len(linkedlist1))      # 마지막 길이를 가진 인덱스 삭제
linkedlist1.desc()











