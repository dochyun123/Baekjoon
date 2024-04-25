N = int(input())
candy = [list(input()) for _ in range(N)]

def count_candy(N,candy):
    x_cnt = 1  # total_max_cnt
    for i in range(0,N):
        # 가로 확인
        cnt = 1
        for j in range(0, N-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            x_cnt = max(cnt, x_cnt)
    y_cnt = 1
    for i in range(0,N):
        # 세로 확인 
        cnt = 1
        for j in range(0, N-1):
            if candy[j][i] == candy[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            y_cnt = max(cnt, y_cnt)
            
        max_cnt = max(x_cnt, y_cnt)
    
    return max_cnt


def switch_x(candy,i,j):
    switched_candy = candy # copy 사용 안하면 candy도 수정됨, 같은 메모리 issue : 자세히 알아보자
    if switched_candy[i][j]!=switched_candy[i][j+1]: # 오른쪽에 있는 것과 바꾸기
        switched_candy[i][j], switched_candy[i][j+1] = switched_candy[i][j+1], switched_candy[i][j]
    else:
        pass
    return switched_candy   


def switch_y(candy,i,j): # 아래에 있는 것과 바꾸기
    switched_candy = candy
    if switched_candy[i][j]!=switched_candy[i+1][j]:
        switched_candy[i][j], switched_candy[i+1][j] = switched_candy[i+1][j], switched_candy[i][j]
    else:
        pass
    return switched_candy

# candy[0][0]~candy[N][N]에 대해여 
# 1. 오른쪽과 바꿔보고 최대수 check 
# 2. 아래쪽과 바꿔보고 최대수 check
count_list = []
count = 1
for i in range(0,N):
    for j in range(0,N-1):
        # 오른쪽 바꾸기
        count1 = count_candy(N,switch_x(candy,i,j))
        count_list.append(count1)
        switch_x(candy,i,j) # 원위치


for i in range(0,N-1):
    for j in range(0,N):
        # 아래쪽 바꾸기
        count2 = count_candy(N,switch_y(candy,i,j))
        count_list.append(count2)
        switch_y(candy,i,j) # 원위치
print(max(count_list))
    