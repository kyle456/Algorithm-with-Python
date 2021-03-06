# 2887. 행성 터널 (골드1)

import sys
input = sys.stdin.readline


def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def make_edges(planets, tunnels):
    for i in range(1, n):
        xa, ya, za, ai = planets[i-1]
        xb, yb, zb, bi = planets[i]
        tunnels.append((min(abs(xa-xb), abs(ya-yb), abs(za-zb)), ai, bi))


n = int(input())
planets = [list(map(int, input().split())) + [i] for i in range(n)]
planets_x = sorted(planets)
planets_y = sorted(planets, key=lambda x: x[1])
planets_z = sorted(planets, key=lambda x: x[2])

tunnels = []
make_edges(planets_x, tunnels)
make_edges(planets_y, tunnels)
make_edges(planets_z, tunnels)
tunnels.sort()

parent = list(range(n))
total, count = 0, 0
for cost, a, b in tunnels:
    a_root, b_root = find_set(a), find_set(b)
    if a_root != b_root:
        parent[b_root] = a_root
        total += cost
        count += 1
        if count >= n-1:
            break
print(total)