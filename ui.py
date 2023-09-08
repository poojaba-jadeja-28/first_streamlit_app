import streamlit as st

# Create a multi-select dropdown menu with default values
selected_options = st.multiselect('Select one or more options:', ['Option 1', 'Option 2', 'Option 3'])

# Display the selected options
st.write('You selected:', selected_options)
