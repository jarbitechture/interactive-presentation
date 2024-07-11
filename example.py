import streamlit as st

# Set the page configuration
st.set_page_config(page_title="H1 Review Presentation", page_icon="📊", layout="wide")

# Define the pages
def home():
    st.title("H1 Review Presentation")
    st.write("Welcome to the H1 Review Presentation. Use the sidebar to navigate through the sections.")

def key_strengths():
    st.title("Key Strengths")
    st.write("""
    - Deep technical expertise in marketing technologies and data platforms.
    - Strong analytical and data-driven decision-making.
    - Effective cross-functional collaboration and project management.
    """)

def areas_for_development():
    st.title("Areas for Development")
    st.write("""
    - Leadership and team management skills.
    - Advanced data governance and security knowledge.
    - Enhanced communication and presentation skills for executive stakeholders.
    """)

def action_plan():
    st.title("Action Plan")
    st.write("""
    - Take on leadership roles in larger projects to build management experience.
    - Pursue training or certifications in data governance and security.
    - Develop and deliver presentations to executive teams to refine communication skills.
    - Secure expanded access to key data systems to reduce dependencies.
    - Participate in leadership training programs.
    - Undertake courses in AI and machine learning relevant to marketing.
    """)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Key Strengths", "Areas for Development", "Action Plan"])

# Page content
if page == "Home":
    home()
elif page == "Key Strengths":
    key_strengths()
elif page == "Areas for Development":
    areas_for_development()
elif page == "Action Plan":
    action_plan()
