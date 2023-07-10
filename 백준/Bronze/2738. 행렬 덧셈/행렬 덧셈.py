A, B = [], []  #행렬선언

N, M = map(int, input().split())  #행렬 크기 입력받기

for row in range(N):   #A, B에 행렬 원소 입력
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):  #행렬 A,B를 더한 행렬 출력
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()