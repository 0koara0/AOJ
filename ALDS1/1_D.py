n = int(input())
r = [0] * (n)
for i in range(n):
    r[i] = int(input())
    
num_max = r[1] - r[0]
num_min = r[0]
min_idx = 0
for i in range(1, n):
    if num_max < r[i] - num_min:
        num_max = r[i] - num_min
    if r[i] < num_min:
        num_min = r[i]
print(str(num_max))