import streamlit as st

# Create a slider-style dropdown menu
selected_option = st.select_slider('Select an option:', options=['Option 1', 'Option 2', 'Option 3'])

# Display the selected option
st.write('You selected:', selected_option)
