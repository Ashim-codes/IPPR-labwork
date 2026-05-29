import cv2
import numpy as np
import matplotlib.pyplot as plt

img_gray = cv2.imread('panda.jpg', 0)

def show(images, titles, figsize=(20, 4)):
    import matplotlib.pyplot as plt

    n = len(images)
    fig, axes = plt.subplots(1, n, figsize=figsize)

    if n == 1:
        axes = [axes]

    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap='gray')
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()


def intensity_transformations(img):
    img = img.astype(np.float64)
    L = 256  # gray levels

    # 1. Image Negative
    negative = L - 1 - img

    # 2. Log Transformation: s = c * log(1 + r)
    c = (L - 1) / np.log(1 + np.max(img))
    log_img = c * np.log(1 + img)

    # 3. Power-Law (Gamma) Transformation
    gamma = 0.5  # <1 brightens, >1 darkens
    c = 1.0
    gamma_img = c * np.power(img / 255.0, gamma) * 255

    # 4. Contrast Stretching
    r_min, r_max = img.min(), img.max()
    contrast = (img - r_min) / (r_max - r_min) * 255

    images = [
        img.astype(np.uint8),
        negative.astype(np.uint8),
        log_img.astype(np.uint8),
        gamma_img.astype(np.uint8),
        contrast.astype(np.uint8)
    ]

    titles = [
        'Original',
        'Negative',
        'Log Transform',
        f'Gamma (γ={gamma})',
        'Contrast Stretch'
    ]

    show(images, titles, figsize=(20, 4))


print("Intensity Transformations complete.")
intensity_transformations(img_gray)