print(*[m**2 for m in map(int, input().split()) if m % 2 == 0 and m**2 % 10 != 4])
