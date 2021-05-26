# 1 .. 4 ~ 100
# 2 .. 8 ~ 200
import numpy as np

B = []
for i in range(1, 11):
    B.append([i * j * 4 for j in range(0, 26)])

for j in range(0, 10):
    B[j][0] = j + 1

# 이게 그냥 출력한건데 array로 바꿔야 밑에 문제 계산이 될거같은데
# B 안에 그냥 들어가있는거야
# print('\n'.join(map(str, B)))
C = np.dot(B, np.array(B).reshape(10, 26).T)
print(C.shape)

# 이게 대각합이야
print(np.trace(C))
