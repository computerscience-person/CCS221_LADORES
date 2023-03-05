import numpy as np

def cube_object(bottom_lower: list=([0, 0, 0]), side_length=5) -> np.ndarray :
    '''Create cube, starting from the bottom lower point.'''
    bottom_lower = np.array(bottom_lower, dtype=np.float32)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower,
    ])
    
    return points

def tetra_object(bottom_lower: list = ([0, 0, 0]), side_length = 5) -> np.ndarray :
    '''Create tetrahedron, starting from the bottom lower point.'''
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower,
    ])

    return points

def pyramid_object(bottom_lower: list = ([0, 0, 0]), base_length = 5) -> np.ndarray:
    '''Create square pyramid, starting from the bottom lower point.'''
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [base_length, 0, 0],
        bottom_lower + [base_length, base_length, 0],
        bottom_lower + [0, base_length, 0],
        bottom_lower + [base_length/2, base_length/2, base_length]
    ])

    return points

def octa_object(bottom_lower: list = ([0, 0, 0]), side_length = 5) -> np.ndarray:
    '''Create octahedron, starting from the bottom lower point.'''
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
    ])

    return points

def prism_object(bottom_lower: list = ([0, 0, 0]), base_width= 1, height = 1, length = 5 ) -> np.ndarray:
    '''Create triangular prism, starting from the bottom lower point.'''
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [length, 0, 0],
        bottom_lower + [0, base_width, 0],
        bottom_lower + [0, 0, height],
        bottom_lower + [length, base_width, 0],
        bottom_lower + [length, 0, height]
    ])

    return points