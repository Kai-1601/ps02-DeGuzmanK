import time

start = time.time()
result = ""
for i in range(1, 100001):
    result.join(str(i))
    print("join() Time:", time.time() - start)

