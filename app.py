import streamlit as st
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Env vars (supports both local .env and Streamlit Cloud secrets)
load_dotenv()
API_KEY = os.getenv("API_KEY") or st.secrets.get("API_KEY", "")
BACKEND_API_URL = os.getenv("BACKEND_API_URL") or st.secrets.get("BACKEND_API_URL", "https://your-main-account-backend.onrender.com/get-app-config")

st.set_page_config(page_title="Member DB - Secure Portal", page_icon="🔒")

def fetch_app_from_server(key):
    try:
        headers = {"Authorization": f"Bearer {key}"}
        response = requests.get(BACKEND_API_URL, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

# --- BACKEND GATEKEEPER & KILL SWITCH ---
config = fetch_app_from_server(API_KEY)

if not config or config.get("status") != "success":
    st.error("🚨 **Server Down / Access Denied:** Unable to connect to the central authentication server.")
    st.info("The application has been shut down by the administrator. Please check your internet connection or server status.")
    st.stop()  # UI stops loading if API ping fails or unauthorized

# --- UI LOADED FROM BACKEND CONFIG ---
st.title(config.get("app_title", "Member DB"), anchor=False)

# Render inputs based on backend schema
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

# Safe load local CSV database
if os.path.exists("member_db.csv"):
    db = pd.read_csv("member_db.csv")
else:
    db = pd.DataFrame(columns=[
        "ID", "FullName", "Email", "Age", "WorkType", 
        "DiscordId", "InstagramID", "GithubID", "LinkedInID", "Description"
    ])

if st.button(label="Show DB", type="primary", use_container_width=True):
    try:
        st.dataframe(db, hide_index=True)
        st.success("Member DB successfully loaded")
    except Exception:
        st.error("Member DB is empty")

# Insert Data locally
if st.button(label="Insert Data", type="primary", use_container_width=True):
    new_id = db.shape[0] + 1
    df = pd.DataFrame({
        "ID": [new_id],
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

# Query & Delete Controls
st.divider()
index_s = st.radio(label="Select index", options=["ID", "Email", "DiscordId", "InstagramID", "GithubID", "LinkedInID"], horizontal=True)

all_columns = ["ID", "FullName", "Email", "Age", "WorkType", "DiscordId", "InstagramID", "GithubID", "LinkedInID", "Description"]
index_dict = {"ID": 0, "Email": 2, "DiscordId": 5, "InstagramID": 6, "GithubID": 7, "LinkedInID": 8}

active_columns = all_columns.copy()
active_columns.pop(index_dict[index_s])

select_ID = st.multiselect(label="Select Columns", options=active_columns)
target_s = st.text_input(label="Enter the target value")

if st.button(label="Show", type="primary", use_container_width=True):
    unique_list = list(db[index_s])
    out_dict = {}
    for i in range(len(unique_list)):
        if target_s == str(unique_list[i]):
            for col in all_columns:
                out_dict[col] = db[col].iloc[i]
    for j in select_ID:
        if j in out_dict:
            st.success(f"{j} : {out_dict[j]}")

if st.button(label="Delete", type="primary", use_container_width=True):
    unique_list_del = list(db[index_s])
    for i in range(len(unique_list_del)):
        if target_s == str(unique_list_del[i]):
            db = db.drop(axis=0, index=i)
            db.reset_index(drop=True, inplace=True)
            st.dataframe(db)
            db.to_csv("member_db.csv", index=False)
