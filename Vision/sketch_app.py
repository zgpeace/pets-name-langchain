import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np

# Set up the page layout
st.set_page_config(layout="wide")

# Assuming logo.png is the logo file in the same directory as the script
logo = './logo.png'

# Sidebar with logo and navigation
# st.sidebar.image(logo, use_column_width=True)
st.sidebar.button('Page 1')
st.sidebar.button('Page 2')
st.sidebar.button('Page 3')
st.sidebar.checkbox('Checkbox 01')
st.sidebar.checkbox('Checkbox 02')
st.sidebar.selectbox('ComboBox', ['Option 1', 'Option 2', 'Option 3'])

# Main page layout
col1, col2 = st.columns([1, 3])

# Dummy data for the chart
data = pd.DataFrame({
    'Series 1': np.random.rand(10),
    'Series 2': np.random.rand(10)
})

# Echart line chart
options = {
    "xAxis": {
        "type": 'category',
        "data": list(data.index)
    },
    "yAxis": {
        "type": 'value'
    },
    "series": [{
        "data": list(data['Series 1']),
        "type": 'line',
        "smooth": True
    },{
        "data": list(data['Series 2']),
        "type": 'line',
        "smooth": True
    }]
}

# Render the Echarts line chart in the main column
with col2:
    st.markdown("### Chart_name")
    st_echarts(options=options, height="400px")

    # Button to download data
    if st.button('Download Chart Data'):
        # This will download the data as a CSV file
        st.download_button(
            label="Download data as CSV",
            data=data.to_csv().encode('utf-8'),
            file_name='chart_data.csv',
            mime='text/csv',
        )

# Text and other elements would go here
with col1:
    st.markdown("## My_app_name")
    st.markdown("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Quisque varius eros ac purus dignissim.
    """)
