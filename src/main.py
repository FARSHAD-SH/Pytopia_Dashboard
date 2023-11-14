import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image

login_option = st.sidebar.radio('Login/Signup', ('Login', 'Signup'))

if login_option == 'Login':
    with st.sidebar.form('login'):
        st.write('Login Here.')
        username = st.text_input('Enter User Name:')
        password = st.text_input('Enter Password:', type='password')

        submitted = st.form_submit_button('Login')
        if submitted:
            pass
else:
    with st.sidebar.form('login'):
        st.write('Signup Here.')
        username = st.text_input('Enter User Name:')
        password = st.text_input('Enter Password:', type='password')
        email = st.text_input('Email')

        submitted = st.form_submit_button('Login')
        if submitted:
            pass


banner = Image.open('./Data/python-banner.png')
st.image(banner, use_column_width=True)

col1, col2 = st.columns(2)
col1.metric(label='Unige Members', value='4500', delta='+10')
col2.metric(label='Niazmandiha Member', value='600', delta='-4', delta_color='inverse')

# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO

# st.title(":zap: Pytopia Dashboard")
# st.write(":chicken: Welcome to the Pytopia Dashboard! This is a work in progress, so please be patient with us.") 
# st.text("This is a text widget")

# with st.expander("Upload File"):
    # uploaded_file = st.file_uploader("Choose a file")
    # if uploaded_file is not None:
    #     st.write("filename: ", uploaded_file.name)
    #     st.write("filetype: ", uploaded_file.type)
    #     st.write("file size: ", uploaded_file.size)
    #     st.write("file content: ", uploaded_file.read())
    #     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #     string_data = stringio.read()
    #     st.write(string_data)

    #     data = json.loads(string_data)
    #     st.json(data)

with st.expander('plot'):
    fig, ax = plt.subplots(1, 1, figsize=(6, 4))
    sns.histplot(np.random.randn(1000), ax=ax)
    st.pyplot(fig)

with st.expander('Profile'):
    col1, col2 = st.columns(2)
    col1.text_input('Name')
    col2.text_input('Age')
    st.camera_input('Camera Input', key='camera_input')


