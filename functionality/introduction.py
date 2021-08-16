import streamlit as st
import urllib


def get_file_content(url='https://raw.githubusercontent.com/someshfengde/Commonlit-redability-model/master/README.md'):

    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')


def show_instructions():
    readme_text = st.markdown(get_file_content())
    return 0
