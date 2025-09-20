import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Data Elements")

st.subheader("Dataframe")
df = pd.DataFrame({
    "Name": ['Alice', 'Bob', 'Charlie', 'David'],
    "Age": [25, 32, 37, 45],
    "Profession": ['Engineer', 'Doctor', 'Actor', 'Chef']
})
# st.write(df)
st.dataframe(df)

st.divider()

st.subheader("Editable Dataframe")
editable_df = st.data_editor(df)

st.divider()

st.subheader("Static Tables")
st.table(df)

st.divider()

st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=df['Age'].mean())

st.divider()

st.subheader("JSON and Dictionary")
sample_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ['Python', 'ML', 'Data Science']
}
st.json(sample_dict)
