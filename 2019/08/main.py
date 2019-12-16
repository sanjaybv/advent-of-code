from fileinput import input as f_input
import numpy as np

image = np.array(list(int(x) for x in f_input()[0].strip()))
image = image.reshape(-1, 6, 25)

i_0 = np.argmin(np.sum(image == 0, (1, 2)))
print(np.sum(image[i_0] == 1) * np.sum(image[i_0] == 2))

final = np.full(image.shape[1:], 2)
for x in range(final.shape[0]):
    for y in range(final.shape[1]):
        for i in image[:, x, y]:
            if i != 2:
                final[x][y] = i
                break

print(final)
