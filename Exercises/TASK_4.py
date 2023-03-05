import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf
from solids import *

def plot_object(points, title: str):
    '''Plots an object, assuming it's convex and not too complex.'''

    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],
                        triangles=tri,
                        shade=True, cmap=cm.RdGy, linewidth=0.2)
    ax.set_xlim3d(-5,5)
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5)
    plt.title(title)

    plt.show()

def rotate_x(points: np.array, angle: float) -> tf.Tensor:
    """Rotates a 3D object around the x-axis by a given angle in degrees.

    Args:
        points (np.array): 3D object represented as a list of points.
        angle (float): Angle in degrees.
    """
    angle =  float(angle) 
    rotation_matrix = tf.transpose(tf.stack([ 
                        [tf.cos(angle), tf.sin(angle), 0],
                        [-tf.sin(angle), tf.cos(angle), 0],
                        [0, 0, 1]
        ]))
    rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
    return rotate_object

def rotate_z(points: np.array, angle: float) -> tf.Tensor:
    """Rotates a 3D object around the z-axis by a given angle in degrees.

    Args:
        points (np.array): 3D object represented as a list of points.
        angle (float): Angle in degrees.
    """
    angle =  float(angle) 
    rotation_matrix = tf.transpose(tf.stack([ 
                        [1, 0, 0],
                        [0, tf.cos(angle), tf.sin(angle)],
                        [0, -tf.sin(angle), tf.cos(angle)]
        ]))
    rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
    return rotate_object

def rotate_y(points: np.array, angle: float) -> tf.Tensor:
    """Rotates a 3D object around the y-axis by a given angle in degrees.

    Args:
        points (np.array): 3D object represented as a list of points.
        angle (float): Angle in degrees.
    """
    angle =  float(angle) 
    rotation_matrix = tf.stack([ 
                        [tf.cos(angle), 0, -tf.sin(angle)],
                        [0, 1, 0],
                        [tf.sin(angle), 0, tf.cos(angle)]
        ])
    rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
    return rotate_object

def rotations(theta_x, theta_y, theta_z):
    init_cube = cube_object(bottom_lower=(0, 0, 0), side_length=3)
    plot_object(init_cube, "Cube in 3D")

    points = tf.constant(init_cube)

    rotated_object = rotate_x(init_cube, theta_x)
    plot_object(rotated_object, "Rotated cube in x by 75 degrees")

    rotated_object = rotate_y(init_cube, theta_y)
    plot_object(rotated_object, "Rotated cube in y by 75 degrees")

    rotated_object = rotate_z(init_cube, theta_z)
    plot_object(rotated_object, "Rotated cube in z by 75 degrees")

def main():
    rotations(75, 75, 75)

if __name__ == "__main__":
    main()
