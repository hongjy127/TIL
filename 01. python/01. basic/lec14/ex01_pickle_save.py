# 되도록 함수로 만들어서 사용
# 전역변수는 최대한 피하기
# 단일책임의 원칙

def load(fpath):
    with open(fpath, "rt", encoding="utf-8") as f:
        return f.readlines()

def convert(lines):  # list -> dict (학생이름: key, 성적 리스트: value)
    data = {}
    for line in lines[1:]:  # 헤더 제외
        items = line.split(',')
        name = items[0]  # 학생이름
        scores = items[1:]  # 성적 리스트
        data[name] = list(map(int,scores))  # 사전에 추가(int를 사용하면 white 문자도 삭제)
    return data

import pickle
# 저장하기
def save(fpath, data):
    with open(fpath,'wb') as f:
        pickle.dump(data, f)

# 예외가 load 파일에 있었다면 lines가 None이 되기 때문에
def main():
    try:
        lines = load('ex01_data.csv')  # hard coding - 안좋아! -> input, sys.argv, config.ini
        # fpath = input("파일명: ")
        # lines = load(fpath)
        # print(lines)
        data = convert(lines)  # 이런 작업들을 맨날 하지 않으려면 data(dict)를 저장 -> pickle
        print(data)
        save('ex01_data.dat', data)

    except Exception as e:
        print(f"예외발생: {e}")

main()
#\ufeff - ms의 utf-8에 이게 항상 붙음
