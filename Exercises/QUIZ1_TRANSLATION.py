import cv2
import numpy as np
import matplotlib.pyplot as plt

def translate_img(img: cv2.Mat, x: int, y: int) -> cv2.Mat:
    """
    Translate the image by x and y pixels.
    :param img: The image to translate
    :param x: The number of pixels to translate in the x direction
    :param y: The number of pixels to translate in the y direction
    :return: The translated image
    """

    M = np.float32([[1, 0, x], 
                    [0, 1, y]])
    return cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

def visualize_img(img: cv2.Mat) -> None:
    """
    Visualize the image using matplotlib.
    :param img: The image to visualize
    :return: None
    """
    plt.imshow(img)
    plt.xlim(0, 30)
    plt.ylim(30, 0)
    plt.show()

def main():
    B_old = [[1, 4],
             [2, 6],
             [3, 7],
             [4, 8],
             [5, 9]]
    B_new = [[int(input("Enter x-translation: ")) + coord[0] , int(input("Enter y-translation: ")) + coord[1]] for coord in B_old]
    img = cv2.imread("img4.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.title("Original Image")
    visualize_img(img)
    for j, k in B_new:
        img2 = translate_img(img, j, k)
        visualize_img(img2)

if __name__ == "__main__":
    main()