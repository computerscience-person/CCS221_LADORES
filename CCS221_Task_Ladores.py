import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import Exercises.TASK_1 as task1

def main():
    st.title("Midterm Exam in CCS221")
    st.header("Task 1")
    st.subheader("DDA Line Algorithm")
    st.write("This is a DDA Line Algorithm")
    st.pyplot(task1.DDALine(0, 0, 100, 100, 'ro'))


if  __name__ == "__main__":
    main()
