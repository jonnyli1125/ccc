def solution(inputs):
    i = 0

    def read_section():
        nonlocal i
        n = int(inputs[i])
        val = [line.split() for line in inputs[i+1:i+n+1]]
        i += n + 1
        return val

    same_group = read_section()
    diff_group = read_section()
    groups = read_section()
    d = {}
    for a, b, c in groups:
        d[a] = [b, c]
        d[b] = [a, c]
        d[c] = [a, b]
    n = sum(1 for (a, b) in same_group if b in d and a not in d[b])
    n += sum(1 for (a, b) in diff_group if b in d and a in d[b])
    return n
