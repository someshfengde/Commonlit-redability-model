import streamlit as st
from introduction import *
from feedback import *
from run_app import *
from show_source import *


st.title('Commonlit Complexity Detection')

selected_title = st.sidebar(
    "Where would you like to go?",
    ('Introduction', 'Run app >', 'give feedback', 'view source')
)

if selected_title == 'Introduction':
    show_instructions()
    st.sidebar.success('To continue select Run app')

elif selected_title == 'Run app >':
    run_app()

elif selected_title == 'give feedback':
    feedback()

elif selected_title == 'view source':
    show_source()
