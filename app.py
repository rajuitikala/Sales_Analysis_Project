import streamlit as st

st.title("Sales Analysis Dashboard")
st.write("Welcome to the Sales Analysis Project!")

# Example visualization
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {"Month": ["Jan", "Feb", "Mar", "Apr"], "Sales": [1000, 1500, 2000, 2500]}
df = pd.DataFrame(data)

# Line chart
st.line_chart(df.set_index("Month"))

