import streamlit as st
import pandas as pd
import numpy as np

left_col, right_col = st.columns(2)
left_col.slider("left", 0, 100)
right_col.slider("right", 0, 100)

number = st.sidebar.slider("pick a number", 0, 100, 40)
st.sidebar.write(number)

st.title("Sample App")

df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [-1, -2, -3, -4],
})

st.dataframe(df.style.highlight_max(axis=0))

st.json({
    "data": {
        "name": "abc",
        "age": 123
    }
})

df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

if st.button("click me"):
    st.write("clicked")

if st.checkbox("click me"):
    st.write("clicked")

options = st.multiselect(
    "what are your favorite colors?",
    ["green", "blue", "red", "yellow"],
    ["blue", "green"]
)

st.write(f"選択肢: {options}")

number = st.slider("pick a number", 0, 100, 40)
st.write(f"number: {number}")


