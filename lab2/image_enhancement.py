import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, exposure


def show(images, titles, cmap_list=None, figsize=(16, 4)):
    """Helper: display multiple images side by side."""
    n = len(images)

    if cmap_list is None:
        cmap_list = ['gray'] * n

    fig, axes = plt.subplots(1, n, figsize=figsize)

    if n == 1:
        axes = [axes]

    for ax, img, title, cmap in zip(axes, images, titles, cmap_list):
        ax.imshow(img, cmap=cmap)
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.axis('off')

    plt.tight_layout()
    plt.show()

# Load a sample grayscale image (use your own: cv2.imread('path'))
img_gray = cv2.cvtColor(
    cv2.resize(
        np.array(data.camera(), dtype=np.uint8),
        (512, 512)
    ),
    cv2.COLOR_GRAY2BGR
)

img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)

print("Setup complete. Image shape:", img_gray.shape)