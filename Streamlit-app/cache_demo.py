import streamlit as st
import time
import pandas as pd
import numpy as np
import requests

# @st.cache_data  # 👈 Add the caching decorator
# def load_data(url):
#     df = pd.read_csv(url)
#     return df

# df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
# st.dataframe(df)

# @st.cache_data
# def transform(df):
#     df = df.filter(items=['Date/Time'])  # 示例 1：筛选特定列
#     # df = df.apply(np.sum, axis=0)
#     return df

# df = transform(df)
# st.dataframe(df)

@st.cache_data
def api_call():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    return response.json()
api_response = api_call()
print("api call", api_response)
st.write("api call", api_response)

st.button("Rerun")