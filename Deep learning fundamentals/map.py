from datetime import datetime
import timeit
import numpy as np

a = list(np.arange(1000))
b = []

start = timeit.default_timer()
for i in a:
    b.append(i * 2)

stop = timeit.default_timer()
print((stop - start)*1000, 'ms')

start = timeit.default_timer()

c = map(lambda x: x * 2, a)
#o(nlogn)
c = list(c)
stop = timeit.default_timer()
print((stop - start)*1000, 'ms')

print(b == list(c))


print(next(iter(b)))

# map function is faster a bit than for loop
# but if not change the map object to list, it will be way more faster!
# tensorflow map will compute parallel across the files, and make it efficient
