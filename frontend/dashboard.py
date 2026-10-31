import os

import requests
import streamlit as st

BACKEND = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Job Hunter", layout="wide")
st.title("AI Job Hunter")

page = st.sidebar.radio("Section", [
    "Dashboard", "Resume Profile", "Job Search",
    "Recommended Jobs", "Application Approval", "Application Tracker",
])

if page == "Dashboard":
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Jobs discovered", 0)
    c2.metric("Shortlisted", 0)
    c3.metric("Applied", 0)
    c4.metric("Interviews", 0)
    try:
        st.caption(f"Backend: {requests.get(f'{BACKEND}/health', timeout=3).json()}")
    except Exception:
        st.warning("Backend not reachable")
elif page == "Resume Profile":
    f = st.file_uploader("Upload resume (PDF)", type=["pdf"])
    if f and st.button("Upload"):
        r = requests.post(f"{BACKEND}/resume/upload", files={"file": (f.name, f.getvalue(), "application/pdf")})
        st.write(r.json())
else:
    st.info(f"{page}: coming soon")
