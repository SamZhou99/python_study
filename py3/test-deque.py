from collections import deque

# 堆栈上限
q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print(q)

# 前面添加
q.appendleft(0)
print(q)

# 删除后面
q.pop()
print(q)

# 删除前面
q.popleft()
print(q)
