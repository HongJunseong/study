#프로그래머스 Lv.2 소수 찾기

import itertools #순열을 사용하기 위함

def permutation(s):
    k = []
    h = []

    for i in range(1,len(s)+1):
        l = list(map(list,itertools.permutations(s,i)))
        for j in range(len(l)):
            k.append(l[j])
            
    for i in k: #각 리스트에 다른 인덱스에 있는 문자열들을 하나의 문자열로 합쳐주기 위함
        a = ''
        for j in range(len(i)):
            a += i[j]
        h.append(int(a))

    return list(sorted(set(h)))
   
def primenum(n): #해당 숫자가 소수인지 판별하기 위한 함수
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False #소수가 아니면 False를 반환한다

def solution(numbers):
    answer = 0
    for i in permutation(numbers):
        if primenum(i) == False: #소수가 아니면
            continue             #continue로 건너뛰고
        answer += 1              #소수이면 카운트해준다
    return answer
