import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(page_title="H1 Review Presentation", page_icon="🌿", layout="wide")

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    body {
        background-color: #e0f7fa;
        font-family: 'Arial', sans-serif;
    }
    .main-header {
        background-color: #00695c;
        padding: 10px;
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
    .sidebar .sidebar-content {
        background-color: #004d40;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Data and Content
sections = {
    "Personal Brainstorm": {
        "What am I passionate about?": [
            "Integrating advanced marketing technologies to drive strategic business outcomes.",
            "Leveraging data to create personalized customer experiences.",
            "Fostering cross-functional collaboration.",
            "Continuous learning and application of the latest trends in MarTech."
        ],
        "What would I consider as my dream job?": [
            "A Chief Marketing Technologist role, leading the integration and optimization of marketing technologies at a strategic level.",
            "A Senior Digital Manager - CDP & Marketing Automations, overseeing CDP implementation and automation to drive innovation and growth."
        ],
        "What background skills do I already have?": [
            "Expertise in Segment and Customer.io.",
            "Deep understanding of data analytics and machine learning.",
            "Strong project management and cross-functional collaboration skills.",
            "Vendor evaluation and partnership management.",
            "Proficiency in data analysis and data-driven decision-making."
        ],
        "What skills do I need to develop?": [
            "Advanced data governance and security protocols.",
            "Leadership and team management.",
            "Emerging marketing technology trends and tools.",
            "Enhanced communication strategies for diverse stakeholders."
        ],
        "What is the one thing holding me back right now?": [
            "Limited exposure to leadership roles and opportunities to lead large-scale projects independently.",
            "Limited permissions and access to key data systems (e.g., Snowflake) restricting independent execution.",
            "Dependency on the development team for project completion, leading to delays and bottlenecks.",
            "Inability to expand the role due to budget constraints and limitations in investing in new marketing technologies."
        ]
    },
    "Manager Discussion": {
        "These are my 3 key strengths today:": [
            "Deep technical expertise in marketing technologies and data platforms.",
            "Strong analytical and data-driven decision-making.",
            "Effective cross-functional collaboration and project management."
        ],
        "These are 3 areas for development:": [
            "Leadership and team management skills.",
            "Advanced data governance and security knowledge.",
            "Enhanced communication and presentation skills for executive stakeholders."
        ],
        "These are the 3 things to work on over the next 6-12 months:": [
            "Take on leadership roles in larger projects to build management experience.",
            "Pursue training or certifications in data governance and security.",
            "Develop and deliver presentations to executive teams to refine communication skills.",
            "Secure expanded access to key data systems to reduce dependencies.",
            "Participate in leadership training programs.",
            "Undertake courses in AI and machine learning relevant to marketing."
        ]
    },
    "Reflection Objective": {
        "What are you like at your best? What do you want to continue doing to maximize when you feel this way?": [
            "At my best, I am innovative, strategic, and collaborative, thriving in solving complex problems and driving meaningful change.",
            "To maximize this, I will continue to seek out challenging projects and foster strong relationships with my team, embracing opportunities for collaboration across departments."
        ],
        "How can your manager/team best support you to be at your best? What do you need from each of them?": [
            "My manager can support me by providing opportunities for leadership, professional development, clear objectives, and regular feedback.",
            "Reducing dependency on other teams by providing more autonomy and access to necessary tools will be beneficial.",
            "The team can support by maintaining open communication, collaboration, and a collaborative work environment."
        ],
        "What are you like when you’re not at your best? What are the signs or triggers you need to watch for to avoid showing up this way?": [
            "When not at my best, I can be overly focused on details and less effective at delegating, becoming frustrated and disengaged when facing bureaucratic hurdles or lack of resources.",
            "Signs include feeling overwhelmed, micro-managing, procrastination, and decreased motivation.",
            "To avoid this, I need to watch for these triggers, delegate more effectively, proactively seek solutions, and maintain open communication with my manager about obstacles."
        ],
        "When the situation isn’t set up for you to show up at your best, what are things you want to work on?": [
            "I want to work on maintaining focus on strategic objectives, improving stress management techniques, and seeking support when needed.",
            "Enhancing my coding and automation skills will also help reduce reliance on the development team.",
            "Improving resilience, adaptability, and skills in navigating organizational barriers and securing necessary resources are key areas of focus."
        ],
        "Where do you want to grow in the coming year? Where do you hope to see this growth take you over the next 3 years?": [
            "I want to grow in leadership and team management, expanding my expertise in AI and machine learning applications for marketing.",
            "Over the next 3 years, I hope to transition into a senior leadership role where I can influence broader strategic decisions and lead significant MarTech initiatives independently."
        ],
        "If you can show up as the leader and employee you aspire to be, what difference will it make? What will be possible?": [
            "It will drive greater innovation and efficiency within the team, leading to more successful projects and strategic growth.",
            "It will also create a more collaborative and motivated team environment, enabling us to tackle larger, more complex projects with greater autonomy.",
            "This will lead to highly personalized and effective marketing campaigns, ultimately contributing to the company's growth and success."
        ],
        "Are there specific goals you want to set for yourself for your growth and development? What would truly elevate you to the next level?": [
            "Lead at least one major project from start to finish independently, demonstrating my ability to manage large-scale projects.",
            "Complete a leadership development program, building my leadership skills and preparing for a senior leadership role.",
            "Regularly present strategic initiatives and project outcomes to executive teams, improving my communication skills.",
            "Gain advanced certifications in data governance and security to ensure compliance and data integrity across all marketing initiatives.",
            "Improve data integration and automation processes within our MarTech stack.",
            "Completing advanced certifications in AI and machine learning.",
            "Leading a major MarTech integration project that demonstrates significant ROI.",
            "Developing and mentoring a team of MarTech specialists."
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
page = st.sidebar.radio("Go to", ["Home", "Personal Brainstorm", "Manager Discussion", "Reflection Objective", "Skills Development Chart"])

# Page content
if page == "Home":
    home()
elif page in sections:
    display_section(page, sections[page])
elif page == "Skills Development Chart":
    create_chart()

