import streamlit as st


def feedback():
    st.title('Thanks for using our app please share your feedback ')
    form = st.form(key='my_form')
    form.text_input(label='Gmail')
    form.text_input(label='Enter your message')
    submit_button = form.form_submit_button(label='Submit')

    return
