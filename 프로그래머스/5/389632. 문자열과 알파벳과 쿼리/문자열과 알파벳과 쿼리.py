import sys
sys.setrecursionlimit(10000)

def solution(s, query):
    N2_MAX = 131072

    seg = [[0] * (N2_MAX * 2) for _ in range(26)]
    seg_str = [0]
    str_uf = [[0] * 26]
    str_idx = [0]

    def find_str(i):
        def find_str_rec(str_n):
            if str_uf[str_n][c] != str_n:
                str_uf[str_n][c] = find_str_rec(str_uf[str_n][c])

            return str_uf[str_n][c]

        c = s[i]

        i |= N2_MAX
        seg_idx = seg[c][i]

        while i > 1:
            i //= 2
            seg_idx = max(seg_idx, seg[c][i])

        return find_str_rec(seg_str[seg_idx])

    def set_seg(node, node_left, node_right):
        if right < node_left or node_right < left:
            return

        if left <= node_left and node_right <= right:
            for c in word:
                seg[c][node] = seg_next
            return

        mid = (node_left + node_right) // 2

        set_seg(node * 2, node_left, mid)
        set_seg(node * 2 + 1, mid + 1, node_right)


    s = [ord(c) - ord('a') for c in s]

    res = []
    for q in query:
        q = q.split()

        if q[0] == '1':
            x, y = int(q[1]) - 1, int(q[2]) - 1
            res.append('YES' if find_str(x) == find_str(y) else 'NO')

        elif q[0] == '2':
            x, word = int(q[1]) - 1, [ord(c) - ord('a') for c in q[2]]

            x_str = find_str(x)

            str_next = len(str_uf)

            for c in word:
                if str_uf[x_str][c] == x_str:
                    str_uf[x_str][c] = str_next

            str_uf.append([str_next] * 26)
            str_idx.append(str_next)

        elif q[0] == '3':
            left, right, word = int(q[1]) - 1, int(q[2]) - 1, [ord(c) - ord('a') for c in q[3]]

            seg_next = len(seg_str)
            str_next = len(str_uf)

            set_seg(1, 0, N2_MAX - 1)

            seg_str.append(str_next)

            str_uf.append([str_next] * 26)
            str_idx.append(str_next)

        elif q[0] == '4':
            x, y = int(q[1]) - 1, int(q[2]) - 1

            x_str, y_str = find_str(x), find_str(y)

            if x_str == y_str:
                continue

            new_idx = min(str_idx[x_str], str_idx[y_str])

            str_next = len(str_uf)

            for str_n in [x_str, y_str]:
                for c in range(26):
                    if str_uf[str_n][c] == str_n:
                        str_uf[str_n][c] = str_next

            str_uf.append([str_next] * 26)
            str_idx.append(new_idx)

        else:
            count = [[0] * 26 for _ in range(len(str_uf))]

            for i, si in enumerate(s):
                count[str_idx[find_str(i)]][si] += 1

            for count_str in count:
                res_str = ''.join([f"{chr(c + ord('a'))} {n} " for c, n in enumerate(count_str) if n > 0])
                if res_str:
                    res.append(res_str[:-1])

    return res