import streamlit as st


def feedback():
    st.Title('Thanks for using our app please share your feedback ')
    form = st.form(key='my_form')
    form.text_input(label='gmail')
    form.text_input(label='')
    submit_button = form.form_submit_button(label='Submit')

    return
