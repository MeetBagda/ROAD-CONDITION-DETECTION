import cv2
import numpy as np

def resize_image(image, size):
    """Resize the image to the specified size."""
    return cv2.resize(image, size)

def normalize_image(image):
    """Normalize the image to have pixel values between 0 and 1."""
    return image / 255.0

def augment_image(image):
    """Apply data augmentation techniques to the image."""
    # Example augmentation: flipping the image
    if np.random.rand() > 0.5:
        image = cv2.flip(image, 1)  # Horizontal flip
    return image