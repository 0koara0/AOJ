def insertion_sort(A, N):
    for i in range(1, N):
        print_list(A)
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = v
    print_list(A)

def print_list(a):
    out = ''
    for ai in a:
        out += str(ai) + ' '
    else:
        out = out[:-1]
    print(out)

n = int(input())
a = list(map(int, input().split(' ')))
insertion_sort(a, n)