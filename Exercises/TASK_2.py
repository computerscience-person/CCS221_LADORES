import numpy as np
import matplotlib.pyplot as plt

arr_2d = np.array([[1, 0, 1]
                   , [0, 0, 0]
                   , [1, 0, 1]])

def change(x, y, color):
    '''
    Changes a specific coordinate to a hue of preset color

    Parameters
    ----------
    x : int
        x coordinate
    y : int
        y coordinate
    color : int
        hue of color
    '''
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d)):
            arr_2d[x][y] = color

    img = plt.imshow(arr_2d, cmap='rainbow', interpolation='none')
    img.set_clim([0, 100])
    plt.colorbar()
    plt.show()

def main():
    change(2, 1, 85)
    
if __name__=="__main__":
    main()