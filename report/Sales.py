##Importing the necessary packages
import pandas as pd #easy to use open source data analysis and manipulate data
import numpy as np #used for working with arrays.
import plotly.express as px # used for data visualization
import plotly.graph_objects as go
import streamlit as st 

from connection import connect_to_db
import warnings
warnings.filterwarnings('ignore')


pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_columns',None)

st.set_page_config(page_title='AdventureWorks 2025',layout='wide',initial_sidebar_state='expanded')
st.markdown('<style>div.block-container{padding-top:3vh}</style>',unsafe_allow_html=True)


st.title('💰:blue[Sales & Revenue Analysis]')



# col1,col2 = st.columns([5,1],gap='large')
# with col1:
#     st.subheader('Data Professional Survey On Adventure Works')

# with col2:
#     st.text_input(label='')

# st.markdown('')

# total1, total2, total3, total4, total5 = st.columns(5, gap='large')

# # Adding content to each column, effectively placing it in a single row
# with total1:
#     with st.container(border=True):
       
#         st.write("Total Sales")
#         st.markdown(container_style, unsafe_allow_html=True)
#         st.write("This is inside the container")
#         st.markdown("</div>", unsafe_allow_html=True)

# with total2:
#     st.metric(label='country_salary[1][0]',value=400)

# with total3:
#     with st.container(border=True):
#         st.write("Content for total3")

# with total4:
#     with st.container(border=True):
#        st.write("Total Sales")
#        st.markdown(container_style, unsafe_allow_html=True)
#        st.write("This is inside the container")
#        st.markdown("</div>", unsafe_allow_html=True)

# with total5:
#     with st.container(border=True):
#         st.write("Content for total5")