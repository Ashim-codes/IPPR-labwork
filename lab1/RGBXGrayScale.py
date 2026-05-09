import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('golden-ornamental-fish-isolated-on-white-background-free-photo.jpg',0)
plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
plt.show()