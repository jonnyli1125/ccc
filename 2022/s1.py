def solution(inputs):
    n = int(inputs[0])
    a = {(i, (n - 4*i) // 5) for i in range(1, n//4 + 1) if (n - 4*i) % 5 == 0}
    b = {((n - 5*i) // 4, i) for i in range(1, n//5 + 1) if (n - 5*i) % 4 == 0}
    return len(a | b)
