import time
from timeit import default_timer as timer

start = timer()
print("hello")
time.sleep(10)
end = timer()
print(end - start)
