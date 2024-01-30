import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import pandas as pd

# Sample data for the table
data = {
    "Date": ["16 Mar, 2019", "16 Mar, 2019", "16 Mar, 2019", "16 Mar, 2019", "15 Mar, 2019"],
    "Name": ["Elvis Presley", "Paul McCartney", "Tom Scholz", "Michael Jackson", "Bruce Springsteen"],
    "Ship To": ["Tupelo, MS", "London, UK", "Boston, MA", "Gary, IN", "Long Branch, NJ"],
    "Payment Method": ["VISA **** 3719", "VISA **** 2574", "MC **** 1253", "AMEX **** 2000", "VISA **** 5919"],
    "Sale Amount": [312.44, 866.99, 100.81, 654.39, 212.79]
}
df = pd.DataFrame(data)

# Ag-Grid options
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_grid_options(enableRangeSelection=True)
grid_options = gb.build()

# Enable various features like adding, deleting, and editing rows.
gb.configure_default_column(editable=True, groupable=True)

# Create Ag-Grid component
response = AgGrid(
    df,
    gridOptions=grid_options,
    height=200,
    width='100%',
    data_return_mode=DataReturnMode.AS_INPUT,  # Return data as input (for edits)
    update_mode=GridUpdateMode.MODEL_CHANGED,  # Update mode for cell edits
    editable=True,  # Enable editing
)

# The response['data'] will hold the dataframe with the edited values.
updated_df = response['data']

# Display the updated DataFrame
st.write('Updated Dataframe:')
st.dataframe(updated_df)

# Button to see more orders
if st.button('See more orders'):
    # Here you can add logic to load or display more orders.
    st.write("More orders to be implemented...")
