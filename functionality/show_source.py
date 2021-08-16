from introduction import *
import streamlit as st


def show_sources():
    t0 = st.title("Code:")

    m0 = st.markdown(
        "  # [github link](https://github.com/someshfengde/Commonlit-redability-model)")

    m1 = st.code(get_file_content('app.py'))

    st.title('Main_app')

    m2 = st.code(get_file_content('run_app.py'))

    st.write("for more code check our github repo")
    return
