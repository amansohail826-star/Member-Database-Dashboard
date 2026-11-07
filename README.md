# Member DB - Streamlit Dashboard 📋

A secure and lightweight **Streamlit Data Management Dashboard** designed to view, insert, search, and manage member details using a local CSV database. 

This application connects to a central backend verification server. It requires an authorized **API Key** and an active internet connection to launch.

---

## 📋 Features

* **Member Management:** Add, search, and delete records seamlessly.
* **Local Storage:** All your data remains stored locally on your machine in `member_db.csv`.
* **Central Authentication:** Secure remote verification using a unique API Key.
* **Dynamic Querying:** Search records based on unique identifiers like ID, Email, Discord ID, Github ID, etc.

---

## 🛠️ Prerequisites

Before running the application, make sure you have the following installed on your machine:

* **Python 3.12+** ([Download Python](https://www.python.org/downloads/))
* **Git** ([Download Git](https://git-scm.com/))

---

## 🔑 Getting the Required API Key

This app will **NOT** run without an authorized `API_KEY`. The server will deny access and the UI will shut down automatically if the key is missing or invalid.

To get your personal **API Key**:
1. Join our Official **Discord Server** (Contact the administrator/owner).
2. Request an API Key for the Member DB app.
3. Keep your API Key safe and do not share it with anyone.

---

## 🚀 Installation & Setup Guide

Follow these steps to set up and run the application on your local machine:

### 1. Clone the Repository
Open your terminal or command prompt and clone this repository:
```bash
git clone https://github.com/your-alt-username/Member-Database-Dashboard.git
cd Member-Database-Dashboard
```

### 2. Create and Activate a Virtual Environment (Recommended)
```bash
# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS / Linux:
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required Python packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables (`.env`)
Create a new file named `.env` in the root folder of the project and add the following lines:

```env
API_KEY=YOUR_DISCORD_API_KEY_HERE
BACKEND_API_URL=https://your-main-backend-service-url.com/get-app-config
```
> ⚠️ **Note:** Replace `YOUR_DISCORD_API_KEY_HERE` with the actual API Key you received from the Discord server.

---

## 💻 Running the Application

Once everything is set up, run the following command in your terminal:

```bash
streamlit run app.py
```

After executing the command, Streamlit will open the dashboard in your default browser at:
`http://localhost:8501`

---

## 🚨 Troubleshooting & Common Errors

* **"Server Down / Access Denied" Error:**
  * Ensure your internet connection is active.
  * Verify that your `.env` file contains the exact `API_KEY` provided to you.
  * Check if the central server is currently undergoing maintenance.
* **Missing CSV File:**
  * Don't worry! `member_db.csv` will automatically be generated in your project folder when you insert your first record.

---

## 📂 Project Structure

```text
├── .github/workflows/ci.yml # GitHub Actions CI/CD pipeline
├── app.py                   # Main Streamlit UI & Gateway Logic
├── requirements.txt         # Project Dependencies
├── runtime.txt              # Python Version
├── .env.example             # Environment Variable Template
├── .gitignore               # Files ignored by Git
└── README.md                # Project Documentation
```
