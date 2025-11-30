from dotenv import load_dotenv
load_dotenv() # load all the evviroment

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## configure our API

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

# Function to load google Gemini Model and provide sql query as responce

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content([prompt[0],question])
    return response.text


# Fuction to retrive query from the sql database

def read_sql_query (sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows


# Define Your Promt

prompt=[
    """
    your are an expert in converting English question to Sql Query!
    The SQL database has the name rdm_exposure_detailed_fct and has TWO table 1.rdm_exposure_detailed_fct with the following columns - fic_mis_date ,v_cust_id,
    v_cust_name ,f_fb_nfb_nslr_deriv,n_outstanding_amount   and n_total_exposure   and 2nd table customer_info  with the following columns - v_cust_id  ,v_cust_industry ,
    v_cust_name , v_cust_nationality , passport ,DOB 

    joining condition will be v_cust_id
    
    \n\n For Example 1 - How many entries of records are present?
    the SQL command will be somthing like this select count(*) from rdm_exposure_detailed_fct;

    Example 1 - display total FB exposure for customers in IRON AND STEEL industry?
    the SQL command will be somthing like this select f_fb_nfb_nslr_deriv,sum(a.n_total_exposure) from rdm_exposure_detailed_fct a inner join customer_info b on ( a.v_cust_id = b.v_cust_id) 
     where a.f_fb_nfb_nslr_deriv = 'FB'
     AND B.v_cust_industry LIKE '%IRON AND STEEL%'
     GROUP BY a.f_fb_nfb_nslr_deriv   ;
    also the sql code should not have ``` in beginning or end of sql word in output 


"""
 

]

# stramlite App

st.set_page_config(page_title="I can Retrieve any sql query")
st.header("Axis Bank RISK chat boat foR SQL Data")

question = st.text_input("input: ",key = "input")

submit=st.button("Ask the question")

# if submit is clicked

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"rdm_exposure_detailed_fct.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)
