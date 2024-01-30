import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np

# Define the data for the chart
categories = [f"rose {i}" for i in range(1, 9)]
values = np.random.randint(10, 100, size=8).tolist()

# Define the initial state of each section (all enabled)
initial_state = {category: True for category in categories}

# Define the color scheme
colors = ["#5470c6", "#91cc75", "#fac858", "#ee6666", 
          "#73c0de", "#3ba272", "#fc8452", "#9a60b4"]

# Use session state to store the toggle states of the sections
if 'toggle_states' not in st.session_state:
    st.session_state.toggle_states = initial_state

# Define the ECharts options for the nightingale/rose chart
options = {
    "tooltip": {
        "trigger": "item",
        "formatter": "{a} <br/>{b} : {c} ({d}%)"
    },
    "legend": {
        "left": "center",
        "top": "bottom",
        "data": categories
    },
    "toolbox": {
        "show": True,
        "feature": {
            "saveAsImage": {"show": True, "title": "Save Image"}
        }
    },
    "series": [
        {
            "name": "Roses",
            "type": "pie",
            "radius": [20, 140],
            "center": ["50%", "50%"],
            "roseType": "radius",
            "itemStyle": {
                "borderRadius": 5
            },
            "label": {
                "show": True
            },
            "emphasis": {
                "label": {
                    "show": True
                }
            },
            "data": [
                {"value": values[i], "name": categories[i], "itemStyle": {"color": colors[i]}}
                for i in range(8) if st.session_state.toggle_states[categories[i]]
            ]
        }
    ]
}

# Checkbox for toggling sections
for i, category in enumerate(categories):
    st.session_state.toggle_states[category] = st.sidebar.checkbox(category, value=st.session_state.toggle_states[category])

# Render the ECharts chart in the Streamlit app
st_echarts(options=options, height="500px")
