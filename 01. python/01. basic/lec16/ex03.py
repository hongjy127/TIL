import sys

# 현재 워킹 디렉토리가 제일 먼저 조사됨
for path in sys.path:
    print(path)