import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Random Data Histogram")

# Generate random data
data = np.random.randn(1000)

# User input for number of bins
bins = st.slider("Enter number of bins for histogram:", min_value=1, max_value=100, value=10)

# Plot histogram
fig, ax = plt.subplots()
ax.hist(data, bins=bins)
ax.set_title("Random Data Histogram")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")

# Display the plot
st.pyplot(fig)
