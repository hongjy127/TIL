import pickle
import sys
# python ex02.py data.dat
# sys.argv

# 불러오기
def load(fpath):
    with open(fpath,'rb') as f:
        return pickle.load(f)

# 예외가 load 파일에 있었다면 lines가 None이 되기 때문에
def main():
    if len(sys.argv) !=2:
        print("파일명을 입력하세요")
        print("python ex02.py data.dat")
        sys.exit(0)
    fname = sys.argv[1]

    try:
        # data = load('data.dat')
        data = load(fname)
        print(data)

    except Exception as e:
        print(f"예외발생: {e}")

main()
#\ufeff - ms의 utf-8에 이게 항상 붙음
