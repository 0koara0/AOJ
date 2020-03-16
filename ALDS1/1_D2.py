def print_list(a):
    out = ''
    for ai in a:
        out += str(ai) + ' '
    else:
        out = out[:-1]
    print(out)

def insertion_sort(a, n):
    for i in range(1, n):
        print_list(a)
        # 比較対象の値
        v = a[i]
        # 比較対象を挿入すべきインデックス
        insertion_idx = i
        while insertion_idx > 0 and a[insertion_idx - 1] > v:
            a[insertion_idx] = a[insertion_idx - 1]
            insertion_idx -= 1
        a[insertion_idx] = v
    return a


n = int(input())
a = list(map(int, input().split(' ')))

a = insertion_sort(a, n)

print_list(a)