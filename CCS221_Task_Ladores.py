import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import Exercises.TASK_1 as task1

def main():
    st.title("Midterm Exam in CCS221")
    st.header("Task 1")
    x0, y0, x1, y1 = st.sidebar.slider('Starting X', 1, 1000), \
                     st.sidebar.slider('Starting Y', 1, 1000), \
                     st.sidebar.slider('Ending X', 1, 1000, 100), \
                     st.sidebar.slider('Ending Y', 1, 1000, 100)
    st.subheader("DDA Line Algorithm")
    st.write("This is a DDA Line Algorithm")
    st.pyplot(task1.DDALine(x0, y0, x1, y1, 'ro'))
    st.subheader("Bresenham's Line Algorithm")
    st.write("This is a Bresenham's Line Algorithm")
    st.pyplot(task1.Bres(x0, y0, x1, y1, 'ro'))
    
    if st.button("Exit"):
        st.stop()

if  __name__ == "__main__":
    main()
