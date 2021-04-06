#최대 곱 구하기 분석 문제 
#여럿이서 카드 게임을 하고 있는데, 각 플레이어는 3장의 카드를 들고 있습니다. 
#위의 경우 첫 번째 플레이어는 11, 22, 33을 들고 있고, 두 번째 플레이어는 44, 66, 11을 들고 있고, 세 번째 플레이어는 88, 22, 44를 들고 있는 거죠.
#함수 max_product는 한 사람당 카드를 하나씩 뽑아서 모두 곱했을 때 가능한 최대 곱을 리턴합니다. 
#max_product를 Greedy Algorithm 방식으로 구현해 보세요.

#Solution
1. 부분 문제의 정답을 이용해서 기존 문제의 정답을 구할 수 있기 때문에, 이 문제에는 최적 부분 구조가 있다.
2. Greedy알고리즘으로 이 문제를 해결하기 위해서는 각 리스트에서 가장 큰 값을 고르는 것.
   각 값을 카드에 적혀있는 숫자이기 때문에 0보다 큰 양수이다.

def max_product(card_lists):
    max_p = 1
   
    for i in range(len(card_lists)):
        precious=0 
        for j in range(len(card_lists[i])):
            if precious < card_lists[i][j]:
                precious = card_lists[i][j]
        max_p = max_p * precious
    return max_p
    
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))
