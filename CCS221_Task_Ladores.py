import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import Exercises.TASK_1 as task1
import Exercises.TASK_2 as task2
import Exercises.TASK_3 as task3

def main():
    st.title("Midterm Exam in CCS221")
    
    st.sidebar.header("Line Algorithm Parameters")
    _task1_x0, _task1_y0, _task1_x1, _task1_y1 = st.sidebar.slider('Starting X', 1, 1000), \
                     st.sidebar.slider('Starting Y', 1, 1000), \
                     st.sidebar.slider('Ending X', 1, 1000, 100), \
                     st.sidebar.slider('Ending Y', 1, 1000, 100)

    st.sidebar.header("Change Pixel Hue Parameters")
    _task2_x, _task2_y, _task2_hue = st.sidebar.slider('X coordinate', 0, 2, 0, 1), \
                                     st.sidebar.slider('Y coordinate', 0, 2, 0, 1), \
                                     st.sidebar.slider('Hue', 0, 100, 50)
                                    
    st.sidebar.header("Image transformations")
    # _task3_filepath = st.sidebar.text_input('Enter file path: ', 'Exercises/images/img1.webp')
    _task3_images = st.sidebar.file_uploader('Upload your files here', ['png', 'jpg', 'webp'], True)
    _task3_transformations = st.sidebar.multiselect('Select tranformations to apply: ', \
                            ['translate', 'rotate', 'reflect', 'scale', 'shear'])

    if 'translate' in _task3_transformations:
        _task3_translationx = st.sidebar.slider('X Translation', 0, 1000)
        _task3_translationy = st.sidebar.slider('Y Translation', 0, 1000)
        
    if 'reflect' in _task3_transformations:
        _task3_reflectionx = st.sidebar.checkbox('Reflect along x axis', True)
        _task3_reflectiony = st.sidebar.checkbox('Reflect along y axis')
        _task3_reflection = ''
        if _task3_reflectionx and _task3_reflectiony:
            _task3_reflection = 'x y'
        elif _task3_reflectionx:
            _task3_reflection = 'x'
        elif _task3_reflectiony:
            _task3_reflection = 'y'
        
    if 'rotate' in _task3_transformations:
        _task3_rotation = st.sidebar.slider('Rotation', -360, 360, 0)
        
    if 'scale' in _task3_transformations:
        _task3_scale = st.sidebar.slider('Scale', 0.0, 5.0, 1.0, 0.000001)
        
    if 'shear' in _task3_transformations:
        _task3_shearx = st.sidebar.slider('X Shear', 0.0, 5.0, 0.0, 0.000001)
        _task3_sheary = st.sidebar.slider('Y Shear', 0.0, 5.0, 0.0, 0.000001)
                
    st.header("Task 1")
    st.subheader("DDA Line Algorithm")
    st.pyplot(task1.DDALine(_task1_x0, _task1_y0, _task1_x1, _task1_y1, 'ro'))
    st.subheader("Bresenham's Line Algorithm")
    st.pyplot(task1.Bres(_task1_x0, _task1_y0, _task1_x1, _task1_y1, 'ro'))
    st.subheader("Midpoint Line Algorithm")
    st.pyplot(task1.midpoint(_task1_x0, _task1_y0, _task1_x1, _task1_y1, 'ro'))
    
    st.header("Task 2")
    st.subheader("Change a pixel's color")
    st.pyplot(task2.change(_task2_x, _task2_y, _task2_hue))
    
    st.header("Task 3")
    st.subheader("Image Transformations")
    # st.write('File Path: ', _task3_filepath)
    for task3_image in _task3_images:
        task3_image = Image.open(task3_image)
        # task3_image = cv2.cvtColor(np.asarray(task3_image), cv2.COLOR_BGR2RGB)
        task3_image = np.asarray(task3_image)
        st.write('Original Image:')
        st.pyplot(task3.visualize(task3_image))
        st.write('Image Transformations: ', *_task3_transformations)
        for transformation in _task3_transformations:
            match transformation:
                case 'translate':
                    st.write("Translation")
                    st.pyplot(task3.visualize(task3.translate(task3_image, _task3_translationx, _task3_translationy)))
                case 'rotate':
                    st.write("Rotation")
                    st.pyplot(task3.visualize(task3.rotate(task3_image, _task3_rotation)))
                case 'reflect':
                    st.write("Reflect")
                    st.pyplot(task3.visualize(task3.reflect(task3_image, _task3_reflection)))
                case 'scale':
                    st.write("Scale")
                    st.pyplot(task3.visualize(task3.scale(task3_image, _task3_scale)))
                case 'shear':
                    st.write("Shear")
                    st.pyplot(task3.visualize(task3.shear(task3_image, _task3_shearx, _task3_sheary)))
    
    if st.button("Exit"):
        st.stop()

if  __name__ == "__main__":
    main()
