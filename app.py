import streamlit as st
import pandas as pd
import pydantic 



st.set_page_config("Member DB","📋")

st.title("Member DB", text_alignment="center")

# inputs

m_full_name = st.text_input(label="Full Name", placeholder="Enter the full name")
m_email = st.text_input(label="Email", placeholder="Enter the Email")
m_gender = st.selectbox(label="Gender", options=["Male", "Female"])
m_age = st.number_input(label="Age", min_value=16, max_value=60, value=18)
m_work_type = st.selectbox(label="Work Type", options=["Game Dev", "Software Dev"])
m_discord_id = st.text_input(label="Discord ID", placeholder="Enter the discord id") 
m_instagram_id = st.text_input(label="Instagram ID", placeholder="Enter the Instagram id") 
m_github_id = st.text_input(label="Github ID", placeholder="Enter the github id") 
m_linkedin_id = st.text_input(label="LinkedIn ID", placeholder="Enter the linkedin id") 
m_description = st.text_area(label="Description", placeholder="Enter the description")

#load db

db = pd.read_csv("member_db.csv")

if st.button(label="Show DB", width="stretch", type="primary"):
    try:
        st.dataframe(db, hide_index=True)
        st.success("Member DB successfully loaded")
    except:
        st.error("Member DB is empty")


# insert data

if st.button(label="Insert Data", width="stretch", type="primary"):
    id = db.shape[0] + 1

    df = pd.DataFrame({
        "ID": [id],
        "FullName": [m_full_name],
        "Email": [m_email],
        "Age": [m_age],
        "WorkType": [m_work_type],
        "DiscordId": [m_discord_id],
        "InstagramID": [m_instagram_id],
        "GithubID": [m_github_id],
        "LinkedInID": [m_linkedin_id],
        "Description": [m_description],
    })

    db = pd.concat([db, df], ignore_index=True)
    st.dataframe(df)
    db.to_csv("member_db.csv", index=False)

# ------------------------------------------------------------------------------------------------------------

index_s = st.radio(label="Select index", options=["ID", "Email", "DiscordId", "InstagramID", "GithubID", "LinkedInID"], horizontal=True)

all_columns = ["ID", "FullName", "Email", "Age", "WorkType", "DiscordId", "InstagramID", "GithubID", "LinkedInID", "Description"]

index_dict = {
    "ID": 0,
    "Email": 2,
    "DiscordId": 5,
    "InstagramID": 6,
    "GithubID": 7,
    "LinkedInID": 8,
}

active_columns = all_columns.copy()
active_columns.pop(index_dict[index_s])

select_ID = st.multiselect(label="Select Columns", options=active_columns)

target_s = st.text_input(label="Enter the target value")

unique_list = list(db[index_s])

out_dict = {}
for i in range(0, len(unique_list)):
    if target_s == str(unique_list[i]):
        for col in all_columns:
            out_dict[col] = db[col].iloc[i]

if st.button(label="Show", width="stretch", type="primary"):
    for j in select_ID:
        if j in out_dict:
            st.success(f"{j} : {out_dict[j]}")

# ---------------------------------------------------------------------------------------------------

unique_list_del = list(db[index_s])

if st.button(label="Delete", width="stretch", type="primary"):
    for i in range(0, len(unique_list_del)):
        if target_s == str(unique_list_del[i]):
            db = db.drop(axis=0, index=i)
            db.reset_index(drop=True, inplace=True)
            st.dataframe(db)
            db.to_csv("member_db.csv", index=False)