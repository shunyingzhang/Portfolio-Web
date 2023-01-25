import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpeg')

with col2:
    st.title('Shunying Zhang')
    content = """
    Hi, I am Shunying. I am currently a python programmer. I graduated in 2014 with a PhD degree in Mechanical Engineering
    from INSA de Rennes in France. I was working on implementation of material models as user subroutines for Finite Element 
    Software. I'm aiming to become a python developer with my transferable mathematical and algorithm skills. 
    """
    st.info(content)
    content_blanc = """
        """
    st.write(content_blanc)
    content2 = """
    Below you can find some of the apps I have built in Python. Feel free to contact me!
    """
    st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for indx, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for indx, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")