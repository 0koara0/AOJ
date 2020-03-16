class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __str__(self):
        return str(self.time)


n, q = map(int, input().split(' '))

queue = []
for i in range(n):
    name, time = input().split(' ')
    queue.append(Process(name, int(time)))

idx = 0
total = 0
while len(queue) > idx:
    time = queue[idx].time
    if time > q:
        total += q
        queue[idx].time -= q
        queue.append(queue[idx])
    else:
        total += time
        print(queue[idx].name + ' ' + str(total))

    idx += 1
