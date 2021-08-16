from introduction import *
import streamlit as st


def show_sources():
    app_code = "https://raw.githubusercontent.com/someshfengde/Commonlit-redability-model/master/functionality/app.py"
    running_code = "https://raw.githubusercontent.com/someshfengde/Commonlit-redability-model/master/functionality/run_app.py"

    t0 = st.title("Code:")

    m0 = st.markdown(
        "  # [github link](https://github.com/someshfengde/Commonlit-redability-model)")

    m1 = st.code(get_file_content(app_code))

    st.title('Main_app')

    m2 = st.code(get_file_content(running_code))

    st.write("for more code check our github repo")
    return
