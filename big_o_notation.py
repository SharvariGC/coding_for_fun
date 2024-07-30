import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to plot Big O notation
def plot_big_o(func, label):
    x = np.linspace(1, 100, 400)
    y = func(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=label)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time Complexity')
    plt.title('Big O Notation')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

st.title('Big O Notation Visualizer')

st.sidebar.title('Choose a Function')

# Define functions representing common Big O notations
functions = {
    'O(1)': lambda x: np.ones_like(x),
    'O(log n)': lambda x: np.log(x),
    'O(n)': lambda x: x,
    'O(n log n)': lambda x: x * np.log(x),
    'O(n^2)': lambda x: x**2,
    'O(2^n)': lambda x: 2**x
}

option = st.sidebar.selectbox('Big O Function', list(functions.keys()))

plot_big_o(functions[option], option)


# run using this
# streamlit run big_o_notation.py