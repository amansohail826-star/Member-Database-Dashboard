import streamlit as st
import pandas as pd
import pydantic 



st.set_page_config("Member DB","📋")

st.title("Member DB",text_alignment="center")

# inputs

m_full_name = st.text_input(label="Full Name",placeholder="Enter the full name")
m_email = st.text_input(label="Emali",placeholder="Enter the Email")
m_gender = st.selectbox(label="Gender",options=["Male","Fmale"])
m_age = st.number_input(label="Age",min_value=16,max_value=60,value=18)
m_work_type = st.selectbox(label="Work Type",options=["Game Dev","software Dev"])
m_discord_id = st.text_input(label="Discord ID",placeholder="Enter the discord id") 
m_instagram_id = st.text_input(label="Instagram ID",placeholder="Enter the Instagram id") 
m_github_id = st.text_input(label="Github ID",placeholder="Enter the github id") 
m_linkedin_id = st.text_input(label="LinkedIn ID",placeholder="Enter the linkedin id") 
m_description = st.text_area(label="Description",placeholder="Enter the description")

#load db

db = pd.read_csv("member_db.csv")

if st.button(label="Show DB",width="stretch",type="primary"):
    try:
        st.dataframe(db,hide_index=True)
        st.success("Member DB success load ")
    except:
        st.error("Member DB is empty ")


# inset

if st.button(label="Inset Date",width="stretch",type="primary"):
    id = db.shape[0]+1

    # db = pd.read_csv("member_db.csv")
    df = pd.DataFrame({
        "ID":id,
        "FullName":[m_full_name],
        "Email":[m_email],
        "Age":[m_age],
        "WorkType":[m_work_type],
        "DiscordId":[m_discord_id],
        "InstagramID":[m_instagram_id],
        "GithubID":[m_github_id],
        "LinkedInID":[m_linkedin_id],
        "Description":[m_description],
        # "LinkedInID":
    })
    # new_m = [id,m_full_name,m_email,m_age,m_work_type,m_discord_id,m_instagram_id,m_github_id,m_linkedin_id,m_description]

    db = pd.concat([db,df],ignore_index=True)
    st.dataframe(df)
    db.to_csv("member_db.csv",index=False)

# ------------------------------------------------------------------------------------------------------------

index_s = st.radio(label="Select index",options=["ID","Email","DiscordId","InstagramID","GithubID","LinkedInID"],horizontal=True)

all_columns = ["ID","FullName","Email","Age","WorkType","DiscordId","InstagramID","GithubID","LinkedInID","Description"]

index_dict = {
    "ID":0,
    "Email":2,
    "DiscordId":5,
    "InstagramID":6,
    "GithubID":7,
    "LinkedInID":8,
}

all_columns.pop(index_dict[index_s])

select_ID = st.multiselect(label="Select Columns",options=all_columns)

traget_s = st.text_input(label="Enter the traget valuer")

unique_list = list(db[index_s])

out_dict = {}
for i in range(0,len(unique_list)):
    if traget_s == str(unique_list[i]):
        out_dict[all_columns[0]] = db[all_columns[0]][i]
        out_dict[all_columns[1]] = db[all_columns[1]][i]
        out_dict[all_columns[2]] = db[all_columns[2]][i]
        out_dict[all_columns[3]] = db[all_columns[3]][i]
        out_dict[all_columns[4]] = db[all_columns[4]][i]
        out_dict[all_columns[5]] = db[all_columns[5]][i]
        out_dict[all_columns[6]] = db[all_columns[6]][i]
        out_dict[all_columns[7]] = db[all_columns[7]][i]
        out_dict[all_columns[8]] = db[all_columns[8]][i]

        # print(out_dict)
if st.button(label="Show",width="stretch",type="primary"):
    for j in select_ID:
        st.success(f"{j} : {out_dict[j]}")

