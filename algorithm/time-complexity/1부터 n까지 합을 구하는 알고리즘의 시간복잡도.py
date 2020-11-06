def sum_all(n):
    total = 0                              # O(1)
    for num in range(1, n+1):              # O(N)
        total += num
    return total


def sum_all_2(n):
    return int(n * (n+1) / 2)              # O(1)

