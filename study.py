#거슬러줘야 할 돈이 N일 때 거슬러주는 동전의 개수를 최소가 되게 구함
#거슬러 주는 돈은 500원, 100원, 50원, 10원만 존재한다고 가정
def gmoney(rmoney):
    coin500 = rmoney//500
    rmoney -= coin500*500
    coin100 = rmoney//100
    rmoney -= coin100*100
    coin50 = rmoney//50
    rmoney -= coin50*50
    coin10 = rmoney//10
    print("500원 동전 : {}개, 100원 동전 : {}개, 50원 동전 : {}개, 10원 동전 : {}개"
    .format(coin500,coin100,coin50,coin10))