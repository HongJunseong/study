#1
#숫자 카드 게임
#n은 행의 개수, m은 열의 개수
#선택한 행에서 가장 작은 숫자를 점수로 얻게되는 게임
#각 행의 가장 작은 수를 찾은 뒤, 그 중에서 가장 큰수를 찾아내야 최고 득점이 가능

n, m = map(int,input().split())
array = []
array2 = []
for i in range(n):
    array.append(list(map(int, input().split())))
    rowmin = min(array[i]) #각 행에서 가장 작은 수가 rowmin이 됨
    array2.append(rowmin) #가장 작은 수들을 모으고,
print(max(array2)) #그 중에서 가장 큰 수가 적혀있는 카드가 최고 득점이 되는 카드임
#2 4 <- 행과 열의 개수
#7 3 1 8
#3 3 3 4
#첫번째 행에서는 1이 최소, 두번째 행에서는 3이 최소이다
#따라서 최고 득점했을 때의 점수는 3이다

#2
#임의의 수 N이 1이 될때까지 다음의 두 과정을 반복 선택하여 수행한다
#N에서 1을 뺀다
#N을 K로 나눈다(이 연산은 N이 K로 나누어 떨어질 때만 선택 가능하다)
#총 연산을 몇번 수행하는지 구하는 프로그램

n, k =map(int, input().split())
count = 0
while(n!=1):
    if n%k == 0:
        n = n//k
        count += 1
    elif n%k != 0:
        n -= 1
        count += 1
print(count)
#100 3을 입력시 100-1, 99//3, 33//3, 11-1, 10-1, 9//3, 3//3 과  계산을 총 7번 한다.
