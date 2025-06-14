# Imports
import streamlit as st  # type: ignore
import sys
import os
# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from main import Frontend_Email_Summarizer

# Main Page Layout
st.set_page_config(page_title="Email Summarizer", page_icon=":email:", layout="wide")
st.title("📧 Email Summarizer 📝")
user_input = st.text_area("Paste your email here:", height=300)

if st.button("Summarize"):
    user_input = Frontend_Email_Summarizer(user_input)
    st.write(user_input)