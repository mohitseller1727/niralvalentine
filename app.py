import streamlit as st

st.set_page_config(page_title="My Simple Page")

st.title("My Simple Web Page")
st.write("This is a basic Streamlit app.")

# If you want to show your index.html as raw HTML:
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=600, scrolling=True)
