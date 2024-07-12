import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(page_title="H1 Review Presentation", page_icon="🌿", layout="wide")

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    body {
        background-color: #f0f4f7;
        font-family: 'Arial', sans-serif;
    }
    .main-header {
        background-color: #2c3e50;
        padding: 20px;
        text-align: center;
        color: white;
        border-radius: 10px;
    }
    .section {
        background-color: #ffffff;
        padding: 20px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .section h2, .section h3 {
        color: #2c3e50;
    }
    .sidebar .sidebar-content {
        background-color: #16a085;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Data and Content
sections = {
    "Professional Development Objectives": {
        "What am I passionate about?": [
            "Integrating advanced marketing technologies to drive strategic business outcomes.",
            "Leveraging data to create personalized customer experiences.",
            "Fostering cross-functional collaboration.",
            "Exploring the potential of AI and machine learning to revolutionize marketing strategies.",
            "Utilizing Customer Data Platforms (CDPs) to enhance customer insights and engagement."
        ],
        "What would I consider as my dream job?": [
            "Chief Marketing Technologist or Senior Digital Manager focused on CDP and Marketing Automations.",
            "Leading the integration and optimization of marketing technologies at a strategic level.",
            "Overseeing the deployment of Segment and other CDP platforms.",
            "Ensuring seamless data integration and developing automated marketing workflows."
        ],
        "What background skills do I already have?": [
            "Proficient in Segment, Customer.io, and Snowflake for data warehousing.",
            "Experience with Python and Cloud Computing.",
            "Strong understanding of data analytics and the application of machine learning models to predict customer behavior.",
            "Experience in leading cross-functional teams and managing projects from start to finish.",
            "Skilled in evaluating vendors and managing strategic partnerships."
        ],
        "What skills do I need to develop?": [
            "Advanced Data Governance and Security: To ensure compliance and data integrity.",
            "Leadership and Team Management: To effectively oversee larger projects and mentor team members.",
            "Emerging Marketing Technology Trends: Staying updated with the latest tools and trends in the MarTech landscape.",
            "Enhanced Communication Strategies: For presenting complex technical concepts to executive stakeholders and non-technical team members."
        ],
        "What is the one thing holding me back right now?": [
            "Limited exposure to leadership roles and opportunities to lead large-scale projects independently.",
            "Dependency on the development team for project completion.",
            "Increasing access to Snowflake and developing more in-house coding and automation skills would mitigate these issues."
        ]
    },
    "Role Reflection": {
        "These are my 3 key strengths today:": [
            "Deep knowledge of marketing technologies and data platforms, including Segment, Customer.io, and Snowflake. Additionally, experience with Python, cloud computing, CRM systems, SEO, content marketing, and marketing automation.",
            "Strong ability to analyze data and make data-driven decisions to optimize marketing strategies.",
            "Proven track record of managing cross-functional projects and delivering results on time and within budget."
        ],
        "These are 3 areas for development:": [
            "Leadership and Team Management: Need to develop skills to lead larger projects and mentor team members.",
            "Data Governance and Security: Advanced knowledge of data governance and security protocols is essential.",
            "Communication Skills: Improved ability to present complex technical concepts to executive stakeholders and non-technical team members."
        ],
        "These are the 3 things to work on over the next 6-12 months:": [
            "Lead a Major Project Independently: Take ownership of a significant project from start to finish to build leadership experience.",
            "Pursue Training in Data Governance and Security: Enroll in courses or certifications to enhance knowledge in this area.",
            "Develop and Deliver Presentations to Executive Teams: Regularly present strategic initiatives and project updates to executive stakeholders to refine communication skills."
        ]
    },
    "Reflection Objectives": {
        "What are you like at your best? What do you want to continue doing to maximize when you feel this way?": [
            "At my best, I am innovative, strategic, and collaborative. I excel in solving complex problems and driving meaningful change. To maximize this, continue to seek challenging projects and foster strong relationships with the team."
        ],
        "How can your manager/team best support you to be at your best? What do you need from each of them?": [
            "My manager can support me by providing opportunities for leadership and professional development. Additionally, reducing dependency on the development team by providing more autonomy and access to necessary tools will be beneficial."
        ],
        "What are you like when you’re not at your best? What are the signs or triggers you need to watch for to avoid showing up this way?": [
            "When not at my best, I can be overly focused on details and less effective at delegating. Signs include feeling overwhelmed and micro-managing. To avoid this, watch for these triggers and delegate more effectively."
        ],
        "When the situation isn’t set up for you to show up at your best, what are things you want to work on?": [
            "Maintain focus on strategic objectives, improve stress management techniques, and seek support when needed. Enhancing my coding and automation skills will also help reduce reliance on the development team."
        ],
        "Where do you want to grow in the coming year? Where do you hope to see this growth take you over the next 3 years?": [
            "I want to grow in leadership and team management. Over the next 3 years, I hope to transition into a senior leadership role where I can influence broader strategic decisions and lead significant MarTech initiatives independently."
        ],
        "If you can show up as the leader and employee you aspire to be, what difference will it make? What will be possible?": [
            "It will drive greater innovation and efficiency within the team, leading to more successful projects and strategic growth. This will create a more collaborative and motivated team environment and enable me to tackle larger, more complex projects with greater autonomy."
        ],
        "Are there specific goals you want to set for yourself for your growth and development? What would truly elevate you to the next level?": [
            "Lead a Major Project Independently: Demonstrate my ability to manage large-scale projects from start to finish.",
            "Complete a Leadership Development Program: Build my leadership skills and prepare for a senior leadership role.",
            "Regularly Present to Executive Teams: Improve my ability to communicate strategic initiatives and project outcomes effectively.",
            "Gain Advanced Certifications in Data Governance and Security: Ensure compliance and data integrity across all marketing initiatives.",
            "Improve Data Integration and Automation Processes: Develop a comprehensive plan to enhance data integration and automation within our MarTech stack."
        ]
    }
}

# Define the pages
def home():
    st.markdown("""
        <div class="main-header">
            <h1>Welcome to the H1 Review Presentation</h1>
        </div>
        <div class="section">
            <p>Use the sidebar to navigate through the sections.</p>
        </div>
    """, unsafe_allow_html=True)

def display_section(section_name, content):
    st.markdown(f"<div class='section'><h2>{section_name}</h2>", unsafe_allow_html=True)
    for key, value in content.items():
        st.markdown(f"<h3>{key}</h3>", unsafe_allow_html=True)
        if isinstance(value, list):
            for item in value:
                st.markdown(f"<p>- {item}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p>{value}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def create_chart():
    st.subheader("Skills Development Progress")
    data = {
        "Skill": ["Data Governance", "Team Management", "MarTech Trends", "Communication", "Coding"],
        "Proficiency": [60, 70, 80, 90, 50]
    }
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Skill"))

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Professional Development Objectives", "Role Reflection", "Reflection Objectives", "Skills Development Chart"])

# Page content
if page == "Home":
    home()
elif page in sections:
    display_section(page, sections[page])
elif page == "Skills Development Chart":
    create_chart()

