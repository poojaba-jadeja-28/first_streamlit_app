import streamlit as st

# Create a dropdown menu with a list of countries
selected_country = st.selectbox('Select a country:', ['USA', 'Canada', 'UK', 'Australia'])

# Display the selected country
st.write('You selected:', selected_country)


