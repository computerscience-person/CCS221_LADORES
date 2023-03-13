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

    return fig

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

def cube_rotations(theta_x: float, theta_y: float, theta_z: float):
    init_cube = cube_object(bottom_lower=(0, 0, 0), side_length=3)
    plot_object(init_cube, "Cube in 3D")

    points = tf.constant(init_cube)

    rotated_object = rotate_x(init_cube, theta_x)
    plot_object(rotated_object, "Rotated cube in x by 75 degrees")

    rotated_object = rotate_y(init_cube, theta_y)
    plot_object(rotated_object, "Rotated cube in y by 75 degrees")

    rotated_object = rotate_z(init_cube, theta_z)
    plot_object(rotated_object, "Rotated cube in z by 75 degrees")
    
def tetra_rotations(theta_x: float, theta_y: float, theta_z: float):
    init_tetrahedron = tetra_object(bottom_lower=(0, 0, 0), side_length=3)
    plot_object(init_tetrahedron, "Tetrahedron in 3D")

    points = tf.constant(init_tetrahedron)

    rotated_object = rotate_x(init_tetrahedron, theta_x)
    plot_object(rotated_object, "Rotated tetrahedron in x by 75 degrees")

    rotated_object = rotate_y(init_tetrahedron, theta_y)
    plot_object(rotated_object, "Rotated tetrahedron in y by 75 degrees")

    rotated_object = rotate_z(init_tetrahedron, theta_z)
    plot_object(rotated_object, "Rotated tetrahedron in z by 75 degrees")

def pyramid_rotations(theta_x: float, theta_y: float, theta_z: float):
    init_pyramid = pyramid_object(bottom_lower=(0, 0, 0), base_length=5)
    plot_object(init_pyramid, "Pyramid in 3D")

    points = tf.constant(init_pyramid)

    rotated_object = rotate_x(init_pyramid, theta_x)
    plot_object(rotated_object, "Rotated pyramid in x by 75 degrees")

    rotated_object = rotate_y(init_pyramid, theta_y)
    plot_object(rotated_object, "Rotated pyramid in y by 75 degrees")

    rotated_object = rotate_z(init_pyramid, theta_z)
    plot_object(rotated_object, "Rotated pyramid in z by 75 degrees")

def prism_rotations(theta_x: float, theta_y: float, theta_z: float):
    init_prism = prism_object(bottom_lower=(0, 0, 0), base_width = 1, height = 5, length= 5)
    plot_object(init_prism, "Prism in 3D")

    points = tf.constant(init_prism)

    rotated_object = rotate_x(init_prism, theta_x)
    plot_object(rotated_object, "Rotated cube in x by 75 degrees")

    rotated_object = rotate_y(init_prism, theta_y)
    plot_object(rotated_object, "Rotated prism in y by 75 degrees")

    rotated_object = rotate_z(init_prism, theta_z)
    plot_object(rotated_object, "Rotated prism in z by 75 degrees")

def octa_rotations(theta_x: float, theta_y: float, theta_z: float):
    init_octahedron = octa_object(bottom_lower=(0, 0, 0), side_length=5)
    plot_object(init_octahedron, "Octahedron in 3D")

    points = tf.constant(init_octahedron)

    rotated_object = rotate_x(init_octahedron, theta_x)
    plot_object(rotated_object, "Rotated octahedron in x by 75 degrees")

    rotated_object = rotate_y(init_octahedron, theta_y)
    plot_object(rotated_object, "Rotated octahedron in y by 75 degrees")

    rotated_object = rotate_z(init_octahedron, theta_z)
    plot_object(rotated_object, "Rotated octahedron in z by 75 degrees")
    
def main():
    cube_rotations(75, 75, 75)
    tetra_rotations(75, 75, 75)
    pyramid_rotations(75, 75, 75)
    prism_rotations(75, 75, 75)
    octa_rotations(75, 75, 75)


if __name__ == "__main__":
    main()
