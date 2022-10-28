# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 10:01:42 2022

@author: z001r9nr
"""
import streamlit as st
import pandas as pd
from PIL import Image




# st.sidebar.header("Quick Links:")
multipage = st.sidebar.radio("Quick Links:",
('Search','DashBoard', 'SPR下单','订单查询', '库存查询', '订单加急追踪', '关于'), index=0)

if multipage == 'Search':
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html= True)

        h1, h2, h3, h4 = st.columns(4)
    with h1:
        image = Image.open('siemens.JPG')
        st.image(image)
    with h4:
        st.caption('Welcome XXX')
    st.title('Search:')
    S_Ipt = st.text_input('','请输入： SO, PO, DN, Invoice, SPR, Material_No, etc.')
    if S_Ipt[:3] == '300':
        st.image(Image.open('SO_Search.png'))
    elif S_Ipt[:3] == '400':
        st.image(Image.open('DN_Search.png'))
    elif S_Ipt[:3] == '450':
        st.image(Image.open('PO_Search.png'))
    elif S_Ipt[:3] == '522':
        st.image(Image.open('Invoice_Search.png'))
    elif S_Ipt[:3] == 'SPR':
        st.image(Image.open('Spr_Search.png'))
    elif S_Ipt[:3] == '3va' or S_Ipt[:3] == '3VA' :
        st.image(Image.open('Material_Search.png'))
    
elif multipage == 'DashBoard':
# st.set_page_config(layout = 'wide')
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html= True)

        h1, h2, h3, h4 = st.columns(4)
    with h1:
        image = Image.open('siemens.JPG')
        st.image(image)
    with h4:
        st.caption('Welcome XXX')
        
    st.title('Dashboard:')

# Data for Billing/AR/OOH

    col1, col2, col3 = st.columns(3)
    col1.metric('Billing:', '500,000 CNY' )
    col2.metric('AR:', '10,000 CNY' )
    col3.metric('OOH:', '300,000 CNY' )

    Credit_blk_s = DWPY_blk_s = AWV_blk_s = ZBOC_blk_s = BSTOP_s = MAD_Abnormal_s = SO_imcomplete_s= True 
    SO_number = Cust_number = ''

    df = pd.read_excel('SO.xlsx')  
    df['cust_number'] = df['cust_number'].astype('str')


    if SO_number:
        df = df[df['SO_No']== int(SO_number)]
    elif Cust_number:
        df = df[df['cust_number'] == Cust_number]
     

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['SO', 'PO', 'DN', 'Billing', 'AR', 'OOH'])


    with tab1:
        d_c1, d_c2 = st.columns([4,1])
        
        Credit_blk_s = DWPY_blk_s = AWV_blk_s = ZBOC_blk_s = BSTOP_s = MAD_Abnormal_s = SO_imcomplete_s = SO_number =  Cust_number = ''
        with d_c2:
            st.text('SO Categories:')
            Credit_blk_s = st.checkbox('Credit_blk', value = True)
            DWPY_blk_s = st.checkbox('DWPY_blk', value = True)
            AWV_blk_s = st.checkbox('AWV_blk', value = True)
            ZBOC_blk_s = st.checkbox('ZBOC_blk', value = True)
            BSTOP_s = st.checkbox('BSTOP', value = True)
            MAD_Abnormal_s = st.checkbox('MAD_Abnormal', value = True)
            SO_imcomplete_s = st.checkbox('SO_imcomplete', value = True)
            SO_number = st.text_input('SO number:')
            Cust_number = st.text_input('Customer number: ')
  
        
        with d_c1:
            if (not SO_number) and (not Cust_number):
                df2 = df.groupby(by = ['Credit_blk'])['SO_No'].count()
                SO_cr_bl = df2[1]
    
                df2 = df.groupby(by = ['DWPY_blk'])['SO_No'].count()
                SO_DWPY_blk = df2[1]
            
                df2 = df.groupby(by = ['AWV_blk'])['SO_No'].count()
                SO_AWV_blk = df2[1]
    
                df2 = df.groupby(by = ['ZBOC_blk'])['SO_No'].count()
                SO_ZBOC_blk = df2[1]
    
                df2 = df.groupby(by = ['BSTOP'])['SO_No'].count()
                SO_BSTOP = df2[1]
    
                df2 = df.groupby(by = ['MAD_Abnormal'])['SO_No'].count()
                SO_MAD_Abnormal = df2[1]
    
                df2 = df.groupby(by = ['SO_imcomplete'])['SO_No'].count()
                SO_imcomplete = df2[1]
       
            elif (not SO_number):
                df2 = df[df['cust_number']== Cust_number].groupby(by = ['Credit_blk'])['SO_No'].count()
                if 1 in df2.index:
                    SO_cr_bl = df2[1]
                else: 
                    SO_cr_bl = 0
    
                df2 = df[df['cust_number']== Cust_number].groupby(by = ['DWPY_blk'])['SO_No'].count()
                if 1 in df2.index:
                    SO_DWPY_blk = df2[1]
                else:
                    SO_DWPY_blk = 0
     
    
                df2 = df[df['cust_number']== Cust_number].groupby(by = ['AWV_blk'])['SO_No'].count()
                if 1 in df2.index:
                    SO_AWV_blk = df2[1]
                else:
                    SO_AWV_blk = 0
        
    
                df2 = df[df['cust_number']== Cust_number].groupby(by = ['ZBOC_blk'])['SO_No'].count()
                if 1 in df2.index:
                    SO_ZBOC_blk = df2[1]
                else:
                    SO_ZBOC_blk = 0    
        
    
                df2 = df[df['cust_number']== Cust_number].groupby(by = ['BSTOP'])['SO_No'].count()
                if 1 in df2.index:
                    SO_BSTOP = df2[1]
                else:
                    SO_BSTOP = 0   
        
    
                df2 = df[df['cust_number']== Cust_number].groupby(by = ['MAD_Abnormal'])['SO_No'].count()
                if 1 in df2.index:
                    SO_MAD_Abnormal = df2[1]
                else:
                    SO_MAD_Abnormal = 0   
    
                df2 = df[df['cust_number']== Cust_number].groupby(by = ['SO_imcomplete'])['SO_No'].count()
                if 1 in df2.index:
                    SO_imcomplete = df2[1]
                else:
                    SO_imcomplete = 0   
     
            else:
                df2 = df[df['SO_No']== int(SO_number)].groupby(by = ['Credit_blk'])['SO_No'].count()
                if 1 in df2.index:
                    SO_cr_bl = df2[1]
                else: 
                    SO_cr_bl = 0
    
                df2 = df[df['SO_No']== int(SO_number)].groupby(by = ['DWPY_blk'])['SO_No'].count()
                if 1 in df2.index:
                    SO_DWPY_blk = df2[1]
                else:
                    SO_DWPY_blk = 0
     
                df2 = df[df['SO_No']== int(SO_number)].groupby(by = ['AWV_blk'])['SO_No'].count()
                if 1 in df2.index:
                    SO_AWV_blk = df2[1]
                else:
                    SO_AWV_blk = 0
    
                df2 = df[df['SO_No']== int(SO_number)].groupby(by = ['ZBOC_blk'])['SO_No'].count()
                if 1 in df2.index:
                    SO_ZBOC_blk = df2[1]
                else:
                    SO_ZBOC_blk = 0    
        
                df2 = df[df['SO_No']== int(SO_number)].groupby(by = ['BSTOP'])['SO_No'].count()
                if 1 in df2.index:
                    SO_BSTOP = df2[1]
                else:
                    SO_BSTOP = 0   
        
                df2 = df[df['SO_No']== int(SO_number)].groupby(by = ['MAD_Abnormal'])['SO_No'].count()
                if 1 in df2.index:
                    SO_MAD_Abnormal = df2[1]
                else:
                    SO_MAD_Abnormal = 0   
            
                df2 = df[df['SO_No']== int(SO_number)].groupby(by = ['SO_imcomplete'])['SO_No'].count()
                if 1 in df2.index:
                    SO_imcomplete = df2[1]
                else:
                    SO_imcomplete = 0   
            
            df3 = pd.DataFrame([SO_cr_bl, SO_DWPY_blk, SO_AWV_blk, SO_ZBOC_blk, SO_BSTOP,
                            SO_MAD_Abnormal,SO_imcomplete], index=['SO_cr_bl', 'SO_DWPY_blk', 'SO_AWV_blk', 'SO_ZBOC_blk', 'SO_BSTOP',
                            'SO_MAD_Abnormal','SO_imcomplete'], columns=['SO_Qty'])
            df4 = df3.copy()
        
            df5 = pd.DataFrame()
        
            df6 = pd.DataFrame()
    
            if Credit_blk_s:
                df4['SO_Qty']['SO_cr_bl'] = df3['SO_Qty']['SO_cr_bl']
            else:
                df4.drop(['SO_cr_bl'], inplace = True)
     
            if DWPY_blk_s:
                df4['SO_Qty']['SO_DWPY_blk'] = df3['SO_Qty']['SO_DWPY_blk']
            else:
                df4.drop(['SO_DWPY_blk'], inplace = True)
                
            if ZBOC_blk_s:
                df4['SO_Qty']['SO_ZBOC_blk'] = df3['SO_Qty']['SO_ZBOC_blk']
            else:
                df4.drop(['SO_ZBOC_blk'], inplace = True)
                    
            if AWV_blk_s:
                df4['SO_Qty']['SO_AWV_blk'] = df3['SO_Qty']['SO_AWV_blk']
            else:
                df4.drop(['SO_AWV_blk'], inplace = True)
                
            if  BSTOP_s:
                df4['SO_Qty']['SO_BSTOP'] = df3['SO_Qty']['SO_BSTOP']
            else:
                df4.drop(['SO_BSTOP'], inplace = True)
                
            if MAD_Abnormal_s:
                df4['SO_Qty']['SO_MAD_Abnormal'] = df3['SO_Qty']['SO_MAD_Abnormal']
            else:
                df4.drop(['SO_MAD_Abnormal'], inplace = True)
                
            if SO_imcomplete_s:
                df4['SO_Qty']['SO_imcomplete'] = df3['SO_Qty']['SO_imcomplete']
            else:
                df4.drop(['SO_imcomplete'], inplace = True)
    
            if not df4.empty:
                st.bar_chart(df4, height=500)
    
                
        if (not SO_number) and (not Cust_number):      
            if Credit_blk_s:
                    df5 = df5.append(df[(df['Credit_blk'] == Credit_blk_s)])
            
            if DWPY_blk_s:
                    df5 = df5.append(df[(df['DWPY_blk'] == DWPY_blk_s)])
            
            if ZBOC_blk_s:
                    df5 = df5.append(df[(df['ZBOC_blk'] == ZBOC_blk_s)])
            
            if AWV_blk_s:
                    df5 = df5.append(df[(df['AWV_blk'] == AWV_blk_s)])
            
            if BSTOP_s:
                    df5 = df5.append(df[(df['BSTOP'] == BSTOP_s)])
            
            if MAD_Abnormal_s:
                    df5 = df5.append(df[(df['MAD_Abnormal'] == MAD_Abnormal_s)])
            
            if SO_imcomplete_s:
                    df5 = df5.append(df[(df['SO_imcomplete'] == SO_imcomplete_s)])
        
        elif (not SO_number):
            if Credit_blk_s:
                    df5 = df5.append(df[(df['Credit_blk'] == Credit_blk_s) & (df['cust_number']== Cust_number)])
            if DWPY_blk_s:
                    df5 = df5.append(df[(df['DWPY_blk'] == DWPY_blk_s) & (df['cust_number']== Cust_number)])
            
            if ZBOC_blk_s:
                    df5 = df5.append(df[(df['ZBOC_blk'] == ZBOC_blk_s) & (df['cust_number']== Cust_number)])
            
            if AWV_blk_s:
                    df5 = df5.append(df[(df['AWV_blk'] == AWV_blk_s) & (df['cust_number']== Cust_number)])
            
            if BSTOP_s:
                    df5 = df5.append(df[(df['BSTOP'] == BSTOP_s) & (df['cust_number']== Cust_number)])
            
            if MAD_Abnormal_s:
                    df5 = df5.append(df[(df['MAD_Abnormal'] == MAD_Abnormal_s) & (df['cust_number']== Cust_number)])
            
            if SO_imcomplete_s:
                    df5 = df5.append(df[(df['SO_imcomplete'] == SO_imcomplete_s) & (df['cust_number']== Cust_number)])
        else:
            if Credit_blk_s:
                    df5 = df5.append(df[(df['Credit_blk'] == Credit_blk_s) & (df['SO_No']== int(SO_number))])
            if DWPY_blk_s:
                    df5 = df5.append(df[(df['DWPY_blk'] == DWPY_blk_s) & (df['SO_No']== int(SO_number))])
            
            if ZBOC_blk_s:
                    df5 = df5.append(df[(df['ZBOC_blk'] == ZBOC_blk_s) & (df['SO_No']== int(SO_number))])
            
            if AWV_blk_s:
                    df5 = df5.append(df[(df['AWV_blk'] == AWV_blk_s) & (df['SO_No']== int(SO_number))])
            
            if BSTOP_s:
                    df5 = df5.append(df[(df['BSTOP'] == BSTOP_s) & (df['SO_No']== int(SO_number))])
            
            if MAD_Abnormal_s:
                    df5 = df5.append(df[(df['MAD_Abnormal'] == MAD_Abnormal_s) & (df['SO_No']== int(SO_number))])
            
            if SO_imcomplete_s:
                    df5 = df5.append(df[(df['SO_imcomplete'] == SO_imcomplete_s) & (df['SO_No']== int(SO_number))])
            
    
        df5 = df5.drop_duplicates(subset=['SO_No'])
    
    
        st.caption('SO Details:')    
        if not df5.empty:
            st.write(df5)

           
    with tab2:
        st.header('PO...')

    with tab3:
        st.header('DN...')

    with tab4:
        st.header('Billing...')

    with tab5:
        st.header('AR...')

    with tab6:
        st.header('OOH...')
