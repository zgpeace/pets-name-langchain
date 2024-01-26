import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# App title
st.title("Adrien Treuille: The LLM Genius Predictor")

# Introduction text
st.write("Welcome to the Adrien Treuille's Generative AI Predictor! Join Adrien, our LLM genius and developer extraordinaire at Snowflake, as he predicts the rise of generative AI in the next 5 years. Will we reach the singularity? Let's find out!")

# Sidebar title
st.sidebar.title("Controls")

# Slider for the Bar Chart
ai_impact = st.sidebar.slider("Predicted Impact of AI on Different Sectors (1-100)", 1, 100, 50)

# Creating a DataFrame for Bar Chart
sectors = ['Technology', 'Healthcare', 'Finance', 'Education', 'Entertainment']
impact = [ai_impact * np.random.uniform(0.8, 1.2) for _ in sectors]
bar_data = pd.DataFrame({"Sector": sectors, "Impact": impact})

# Altair Bar Chart
bar_chart = alt.Chart(bar_data).mark_bar().encode(
    x='Sector',
    y='Impact',
    color='Sector'
)
st.altair_chart(bar_chart, use_container_width=True)

# Spacer
st.write("---")

# Slider for the Line Chart
ai_growth = st.sidebar.slider("AI Growth Rate Over Next 5 Years (1-20%)", 1, 20, 10)

# Creating a DataFrame for Line Chart
years = np.arange(2024, 2029)
growth = [(1 + ai_growth/100)**i for i in range(5)]
line_data = pd.DataFrame({"Year": years, "Growth": growth})

# Altair Line Chart
line_chart = alt.Chart(line_data).mark_line().encode(
    x='Year:O',
    y='Growth:Q',
    color=alt.value('green')
)
st.altair_chart(line_chart, use_container_width=True)

# Footer
st.write("Disclaimer: This app is for entertainment purposes only and may not accurately predict the future of AI, but with Adrien Treuille on board, who knows what's possible!")

# Run this script using Streamlit