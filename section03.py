# Section03
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

# 가상환경 실행 activate.bat
# 가상환경 해제 deactivat.bat
# 패키지 설치 pip install
# 패키지 삭제 pip uninstall
# 패키지 리스트 pip list
# 패키지 검색 pip search
# 패키지 내용 pip show

# 외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1': 95, '4': 77, '3': 65, '5': 100, '2': 88}

# simplejson 실행
# indent : 4칸 안으로 들여쓰기 중요!
# sort_keys=True : key를 직렬화해서 정렬한다. 한마디로 키 번호 순서대로 정렬
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))

