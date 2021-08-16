import streamlit as st
import urllib


def get_file_content(path='README.md'):
    url = "https://raw.githubusercontent.com/someshfengde/Commonlit-redability-model/master/" + path

    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')


def show_instructions():
    readme_text = st.markdown(get_file_content())
    return 0
