import streamlit as st
from streamlit_agenda_view import st_agenda_view

st.title('Calendar View in Streamlit')

# Create a list of events (you can fetch these from your data)
events = [
    {
        'title': 'Meeting 1',
        'date': '2023-08-15',
        'description': 'Discuss project updates',
    },
    {
        'title': 'Meeting 2',
        'date': '2023-08-20',
        'description': 'Planning session',
    },
    {
        'title': 'Conference',
        'date': '2023-08-25',
        'description': 'Tech conference',
    },
]

# Display the calendar view
st_agenda_view(events)
