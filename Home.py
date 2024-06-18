import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Christa Sara Luke")
    content_self_description = """
                Hi, I am Christa! I am a Python programmer. I graduated in 2017 with a Bachelor of Technology in 
                Computer Science from the University of Kerala in India. I have worked with companies from various 
                countries primarily focusing on Odoo development for ERP solutions.
              """
    st.info(content_self_description)

content_description = """Below you can find some of apps I built in python. Feel free to contact me!"""
st.write(content_description)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

main_content = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in main_content[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in main_content[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")


