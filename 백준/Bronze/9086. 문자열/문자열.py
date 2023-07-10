case_num = int(input())  #입력 횟수 입력받기

for _ in range(case_num):  #case_num만큼 word를 입력 받고, word인덱스의 0번과 맨끝(-1)번을 출력
    word = input()
    print(word[0], word[-1], sep='')