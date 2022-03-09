def z(n):
    return sum(range(n+1))

def solution(inputs):
    n, m, k = [int(x) for x in inputs[0].split()]

    if k < n or k > z(n):
        return -1
    
