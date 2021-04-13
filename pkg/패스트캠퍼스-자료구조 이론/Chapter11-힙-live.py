# Heap이란(Tree 기반)
# : 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리
# ★ 완전이진트리 : 노드를 삽입할 때 ★최하단 왼쪽 노드부터★ 차례대로 삽입하는 트리
# 
# 1. 힙을 사용하는 이유
# 1) 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n)이 걸림
# 2) 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면 O(logn)이 걸림
# 3) 우선순위 ★큐★와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등 활용
#  

# 2. 힙(Heap) 구조
# ★ 힙은 최대값을 구하기 위한 구조(최대 힙, Max Heap)와 최소값을 구하기 위한 구조(최소 힙, Min Heap)로 분류
# 힙은 다음과 같이 두가지 조건을 가지고 있는 자료구조
# 1) 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
#    - 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 작거나 같다

# 3. 힙과 이진 탐색 트리의 공통점과 차이점
# 이진 트리 : 자식 노드가 2개이다.
# 1) 공통점 : 힙과 이진 탐색 트리는 모두 이진트리 이다.
# 2) 차이점 
#    - ★ 힙은 각 노드의 값이 자식 노드보다 크거나 같다(Max Heap의 경우)
#    - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 크다.
#    - ★ 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽 이라는 조건은 없음
#         힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있다.
#    즉, 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조이다.

# 4. 힙 동작(삽입, 삭제)
# - 힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부터 채워진다.

# 1) 힙에 데이터 삽입 - 삽입할 데이터가 힙의 데이터보다 클 경우(Max Heap의 경우)
# - 먼저 삽입된 데이터는 완전 이진 트리 구조에 맞추어, 최하단부 왼쪽 노드부터 채워진다.
# - 채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복(swap)

# 2) 힙의 데이터 삭제
# - 보통 삭제는 최상단 노드(루트 노드)를 삭제하는 것이 일반적
#   힙의 용도는 최대, 최소 값을 루트 노드에 놓아서 최대, 최소 값을 바로 꺼내쓰는 용도
# - ★상단의 데이터 삭제 시, 가장 최하단부 왼쪽에 위치한 노드(일반적으로 가장 마지막에 추가한 노드)를 루트노드로 이동
# - ★루트 노드의 값이 child node 보다 작을 경우, 루트 노드의 child node 중 가장 큰 값을 가진 노드와 루트 노드 위치를 
#     바꿔주는 작업을 반복한다.
# - ★트리에서 특정 값이 아닌 삭제 시, 가장 큰 값(루트 노드)을 꺼내 삭제한다.

# 5. 힙 구현
# 힙과 배열
# 일반적으로 Heap 구현시 배열 자료구조를 활용
# 배열은 인덱스가 0번부터 시작하지만, Heap 구현의 편의를 위해, root node 인덱스 번호를 1로 지정하면 구현이 수월
# - 부모 노드 인덱스 번호(Parent node's index) = 자식 노드 인덱스 번호(Child node's index) // 2
# - 왼쪽 자식 노드 인덱스 번호 (left Child node's index) = 부모 인덱스 번호(Parent node's index) * 2
# - 오른쪽 자식 노드 인덱스 번호(right Child node's index) = 부모 노드 인덱스 번호(Parent node's index) * 2 + 1

# 1. Heap에 데이터 삽입 구현(Max Heap)
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None) # 0번 인덱스는 : x
        self.heap_array.append(data) # 1번 인덱스부터 data추가

# append() : list 맨 끝 인덱스 뒤에 추가
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def insert(self, data):
        if len(self.heap_array) == 0 :
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        return True

# 힙 클래스 구현3 - insert2
# 1. 삽입한 노드가 부모 노드의 값보다 클 경우  
# -  부모 노드와 삽입한 노드 위치를 바꾼다.
#    삽입한 노드가 루트 노드가 되거나, 부모 노드보다 값이 작거나 같을 경우까지 반복

# 특정 노드의 관련 노드 위치 알아내기
# - 부모 노드 인덱스 번호 = 자식 노드 인덱스 번호 // 2
# - 왼쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2
# - 오른쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2 + 1

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    # 해당 노드가 상위 노드와의 관계를 판별하기 위해 만든다.
    def move_up(self, inserted_idx):
        if inserted_idx <= 1 : # root node보다 작거나 같으면
            return False       # root node이기 때문에 False 반환
        
        parent_idx = inserted_idx // 2 # 부모 인덱스
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True 
        else :
            return False

    def insert(self, data):
        # root node가 없는 경우
        if len(self.heap_array) == 0 :
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        # root node가 있는 경우
        # 기존 heap_array뒤 append를 통해 인덱스번호를 추가한다.
        self.heap_array.append(data)

        # 1) 마지막에 삽입된 노드 인덱스 알아내기
        # len()을 통해 0부터 추출하기 때문에 len(heap_array) - 1
        # heap_array의 마지막 인덱스를 알아낼 수 있다.
        inserted_idx = len(self.heap_array)-1

        # 삽입된 데이터를 기준으로 부모 노드 데이터와 비교 후 노드 체인지 진행
        # move_up() 에서 return 되는 True, False에 따라 while문 진행
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2 # 부모 인덱스
            # 부모 인덱스와 자식 인덱스를 바꾼다 (swap)
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx # 해당 부모 인덱스 노드와 인덱스 변경
    
    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2    # 왼쪽 자식 노드
        right_child_popped_idx = popped_idx * 2+1 # 오른쪽 자식 노드

        # case1   : parent_idx의 left, right 자식 노드가 없는 경우 비교
        #         - 즉, 왼쪽 자식 노드도 없는 경우(왼쪽부터 데이터가 삽입되기 때문)
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case2   : parent_idx의 left는 있고, right는 없는경우
        #         - 해당 parent_idx와 left_child_popped_idx와 값 비교 후 결과 출력
        elif right_child_popped_idx < len(self.heap_array):
            # 자식이 더 클 경우 체인지
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        
        # case3   : 가장 상단 parent_idx의 left, right 노드가 모두 존재하는 경우
        #         - 1. left, right 노드 중 가장 큰 값을 추출
        else: 
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                # - 2. 추출된 값을 parent_idx와 비교 후 결과 반환
               if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                   return True
               else:
                   return False
            else:
                # - 2. 추출된 값을 parent_idx와 비교 후 결과 반환
               if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                   return True
               else:
                   return False


        return True

    def pop(self):
        if len(self.heap_array) <= 1:
            return None
    
        # 0번 인덱스는 None로 설정되어 있기 때문에
        # 1번 인덱스가 가장 상단이다
        returned_data = self.heap_array[1]
        # 1) 가장 마지막에 삽입된 노드를 가장 상단에 위치 시킨다.
        self.heap_array[1] = self.heap_array[-1]
        # 1-1) 상단에 위치 후 맨끝에 있던 인덱스자리는 없앤다.
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2    # 왼쪽 자식 노드
            right_child_popped_idx = popped_idx * 2+1 # 오른쪽 자식 노드

            # case2   : parent_idx의 left는 있고, right는 없는경우
            #         - 해당 parent_idx와 left_child_popped_idx와 값 비교 후 결과 출력
            
            # heap_array의 len길이가 더 크면
            # 최소 left_child_poppped_idx가 있거나 아니면 root node밖에 존재하지 않는다.
            # right_child_popped_idx가 len(self.heap_array) 보다 큰 값이 있어야 right 인덱스가 존재한다
            if right_child_popped_idx < len(self.heap_array):

                # 자식이 더 클 경우 체인지
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]  
                    popped_idx = left_child_popped_idx
            
            # case3   : 가장 상단 parent_idx의 left, right 노드가 모두 존재하는 경우
            #         - 1. left, right 노드 중 가장 큰 값을 추출
            else: 
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    # - 2. 추출된 값을 parent_idx와 비교 후 결과 반환
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = left_child_popped_idx
                else:
                    # - 2. 추출된 값을 parent_idx와 비교 후 결과 반환
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = right_child_popped_idx
            
        return returned_data

# test
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
# 출력
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
# 2. # Heap에 데이터 삭제 구현(Max Heap)
# - 상단의 데이터 삭제 시, 가장 최하단부 왼쪽에 위치한 노드(일반적으로 가장 마지막에 추가한 노드)를
#   root node로 변경
# - root node의 값이 child node보다 작을 경우, root 노드의 child node 중 
#   가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복(swap)

# 1) 특정 노드의 관련 노드 위치 알아내기
# - 부모 노드 인덱스 번호 = 자식 노드 인덱스 번호 // 2
# - 왼쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2
# - 오른쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2 + 1

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2    # 왼쪽 자식 노드
        right_child_popped_idx = popped_idx * 2+1 # 오른쪽 자식 노드

        # case1   : parent_idx의 left, right 자식 노드가 없는 경우 비교
        #         - 즉, 왼쪽 자식 노드도 없는 경우(왼쪽부터 데이터가 삽입되기 때문)
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case2   : parent_idx의 left는 있고, right는 없는경우
        #         - 해당 parent_idx와 left_child_popped_idx와 값 비교 후 결과 출력
        elif right_child_popped_idx < len(self.heap_array):
            # 자식이 더 클 경우 체인지
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        
        # case3   : 가장 상단 parent_idx의 left, right 노드가 모두 존재하는 경우
        #         - 1. left, right 노드 중 가장 큰 값을 추출
        else: 
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                # - 2. 추출된 값을 parent_idx와 비교 후 결과 반환
               if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                   return True
               else:
                   return False
            else:
                # - 2. 추출된 값을 parent_idx와 비교 후 결과 반환
               if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                   return True
               else:
                   return False
    
    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        
        # 0번 인덱스는 None로 설정되어 있기 때문에
        # 1번 인덱스가 가장 상단이다
        returned_data = self.heap_array[1]
        # 1) 가장 마지막에 삽입된 노드를 가장 상단에 위치 시킨다.
        self.heap_array[1] = self.heap_array[-1]
        # 1-1) 상단에 위치 후 맨끝에 있던 인덱스자리는 없앤다.
        del self.heap_array[len(heap_array)-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2    # 왼쪽 자식 노드
            right_child_popped_idx = popped_idx * 2+1 # 오른쪽 자식 노드

            # case2   : parent_idx의 left는 있고, right는 없는경우
            #         - 해당 parent_idx와 left_child_popped_idx와 값 비교 후 결과 출력
           
            # heap_array의 len길이가 더 크면
            # 최소 left_child_poppped_idx가 있거나 아니면 root node밖에 존재하지 않는다.
            # right_child_popped_idx가 len(self.heap_array) 보다 큰 값이 있어야 right 인덱스가 존재한다
            if right_child_popped_idx < len(self.heap_array):

                # 자식이 더 클 경우 체인지
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                   self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]  
                   popped_idx = left_child_popped_idx
            
            # case3   : 가장 상단 parent_idx의 left, right 노드가 모두 존재하는 경우
            #         - 1. left, right 노드 중 가장 큰 값을 추출
            else: 
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    # - 2. 추출된 값을 parent_idx와 비교 후 결과 반환
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = left_child_popped_idx
                else:
                    # - 2. 추출된 값을 parent_idx와 비교 후 결과 반환
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[poped_idx]
                        poped_idx = right_child_popped_idx

        return returned_data

# 6. 힙(Heap) 시간 복잡도
# depth (트리의 높이)를 h라고 표기한다면
# n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제 시, 최악의 경우 root node에서 leaf 노드까지 비교해야 하므로
# h = log2n에 가까우므로, 시간복잡도는 O(logn)
# - 참고 : Big(O) 표기법에서 logn 에서의 log의 밑은 10이 아니라 2이다.
# - 한번 실행시 마다 50%의 실행할 수도 있는 명령을 제거한다는 의미
#   즉, 50%의 실행시간을 단축시킬 수 있다는 것을 의미한다.




























