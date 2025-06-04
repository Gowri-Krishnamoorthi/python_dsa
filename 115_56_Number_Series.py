# from queue import Queue

# def generate_5_6_series(n):
#     q = Queue()
#     q.put("5")
#     q.put("6")

#     result = []

#     while len(result) < n:
#         curr = q.get()
#         result.append(curr)

#         q.put(curr + "5")
#         q.put(curr + "6")

#     return result

# # Example
# n = 12
# output = generate_5_6_series(n)
# print(" ".join(output))

from collections import deque

def generate_5_6_series(n):
    result = []
    q = deque()
    q.append("5")
    q.append("6")

    while len(result) < n:
        curr = q.popleft()
        result.append(curr)
        q.append(curr + "5")
        q.append(curr + "6")

    return result

# Example
n = 12
output = generate_5_6_series(n)
print(" ".join(output))



