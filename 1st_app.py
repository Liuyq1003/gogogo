# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 22:06:39 2022

@author: z001r9nr
"""

import pymssql

import pandas as pd

import numpy as np

import streamlit as st



st.title('My 1st app')


conn =  pymssql.connect(server='139.24.237.85', user = 'FS', password = 'Atos2018', database = 'MasterDB')

sql = 'select top (1000) * from CAS_User'

dl_status = st.text('Loading data...')


df = pd.read_sql(sql, conn)

dl_status.text ('Loading data done!')

st.subheader('Raw data')

if st.checkbox('internal'):
    df = df[df['type'] == 'in']
else:
    df = df [df['type'] == 'out']
st.write(df)

st.subheader('Bar chart')

df2 = df.groupby(by = ['type'])['account'].count()

st.write(df2)

st.bar_chart(df2)
