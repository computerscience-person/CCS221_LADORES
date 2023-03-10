import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
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
    _task3_filepath = st.sidebar.text_input('Enter file path: ')
    
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
    
    if st.button("Exit"):
        st.stop()

if  __name__ == "__main__":
    main()
