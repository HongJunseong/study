#가장 큰 수 만들기
#N은 배열의 크기이며, M만큼 숫자를 덧셈 계산함
#같은 숫자는 K번까지만 연속적으로 더할 수 있음(다른 숫자가 나온 이후에는 다시 사용 가능)
#서로 다른 인덱스에 해당하는 수가 가은 경우에도 서로 다른 것으로 간주

N, M, K = map(int,input().split())
S = list(map(int,input().split()))

fmax = max(S)
result = 0

if S.count(fmax) >= 2:
    result = fmax * M
else:
    S.remove(fmax)
    for i in range(1,M+1):
        if i%(K+1) == 0:
            result += max(S)
        else:
            result += fmax
print(result)
#3 10 4
#4 8 9
#입력 시 9+9+9+9+8+9+9+9+9+8 = 88 이라는 결과가 나옴
