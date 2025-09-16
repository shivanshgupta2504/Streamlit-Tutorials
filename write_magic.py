import streamlit as st
import pandas as pd
import numpy as np

# Basic code to demonstrate the .write magic method
# It automatically detects the type of the object and renders it appropriately

# Normal Text
st.write("Hello World!")

# Numeric value
st.write(123.52)

# Markdown
st.write("# This is a H1 Markdown Header")

# Dictionary
st.write({"key": "value"})

# List
st.write([1, 2, 3, 4])

# Tuple
st.write((1, 2, 3, 4))

# Boolean
st.write(True)

# Numpy array
st.write(np.random.randint(1, 10, 4))

# Pandas Series
st.write(pd.Series(np.random.randint(1, 10, 4)))

# Pandas Dataframe
df = pd.DataFrame({
    "x1": np.random.randint(1, 10, 4),
    "x2": np.random.randint(1, 10, 4)
})
st.write(df)

# Inline Expressions
# 5 + 5
