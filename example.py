import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(page_title="H1 Review Presentation", page_icon="📊", layout="wide")

# Define the pages
def home():
    st.title("H1 Review Presentation")
    st.write("Welcome to the H1 Review Presentation. Use the sidebar to navigate through the sections.")
    st.image("https://source.unsplash.com/1600x900/?cannabis,technology", caption="Cannabis & Technology")

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

def data_visualization():
    st.title("Data Visualization")
    st.write("Here is an example of a data visualization:")

    # Example DataFrame
    data = {
        'Year': [2020, 2021, 2022, 2023],
        'Revenue': [150000, 200000, 250000, 300000],
        'Profit': [50000, 80000, 120000, 150000]
    }
    df = pd.DataFrame(data)

    # Line chart
    st.line_chart(df.set_index('Year'))

    # Bar chart
    st.bar_chart(df.set_index('Year'))

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Key Strengths", "Areas for Development", "Action Plan", "Data Visualization"])

# Page content
if page == "Home":
    home()
elif page == "Key Strengths":
    key_strengths()
elif page == "Areas for Development":
    areas_for_development()
elif page == "Action Plan":
    action_plan()
elif page == "Data Visualization":
    data_visualization()

