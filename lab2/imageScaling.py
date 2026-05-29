import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('panda.jpg')

# res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

height, width = img.shape[:2]

res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

plt.subplot(121), plt.imshow(img), plt.title('Original')

# plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(res), plt.title('Scaling')

# plt.xticks([]), plt.yticks([])

plt.show()