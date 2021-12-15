import numpy as np

np.random.seed(500)

arr = np.random.rand(3, 3, 3)

print(arr)
print('a의 원소들 중 최소값 : ' + str(np.min(arr)))
