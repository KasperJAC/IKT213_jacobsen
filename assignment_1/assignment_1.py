import numpy as np
import cv2 


def print_image_information(image):
    
    dimensions = image.shape

    print(f"height: {dimensions[0]}")
    print(f"width: {dimensions[1]}")
    print(f"channels: {dimensions[2]}")
    print(f"size: {image.size}")
    print(f"data type: {image.dtype}")




if __name__ == "__main__":
    
    image = "assignment_1/lena-1.png"
    print_image_information(cv2.imread(image))
    