# 1228. S/W 문제해결 기본 8일차 - 암호문1

for t in range(1, 11):
    raw_data_len = int(input())
    raw_data = list(input().split())
    order_len = int(input())
    order_data = list(input().split())

    while order_data:
        order = order_data.pop(0)
        x = int(order_data.pop(0))
        y = int(order_data.pop(0))
        for _ in range(y):
            raw_data.insert(x, order_data.pop(0))
            x += 1
    print(f'#{t}', end=' ')
    print(*raw_data[0:10])