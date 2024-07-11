import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit app
st.title("H1 Review & Career Development")

# Sections
st.header("What am I passionate about?")
st.write("""
- Integrating advanced marketing technologies to drive strategic business outcomes.
- Leveraging data to create personalized customer experiences.
- Fostering cross-functional collaboration.
- Continuous learning and application of the latest trends in MarTech.
""")

st.header("What would I consider as my dream job?")
st.write("""
- A Chief Marketing Technologist role, leading the integration and optimization of marketing technologies at a strategic level.
- A Senior Digital Manager - CDP & Marketing Automations, overseeing CDP implementation and automation to drive innovation and growth.
""")

st.header("What background skills do I already have?")
st.write("""
- Expertise in Segment and Customer.io.
- Deep understanding of data analytics and machine learning.
- Strong project management and cross-functional collaboration skills.
- Vendor evaluation and partnership management.
- Proficiency in data analysis and data-driven decision-making.
""")

st.header("What skills do I need to develop?")
st.write("""
- Advanced data governance and security protocols.
- Leadership and team management.
- Emerging marketing technology trends and tools.
- Enhanced communication strategies for diverse stakeholders.
""")

st.header("What is the one thing holding me back right now?")
st.write("""
- Limited exposure to leadership roles and opportunities to lead large-scale projects independently.
- Limited permissions and access to key data systems (e.g., Snowflake) restricting independent execution.
- Dependency on the development team for project completion, leading to delays and bottlenecks.
- Inability to expand the role due to budget constraints and limitations in investing in new marketing technologies.
""")

st.header("Manager Discussion")
st.write("""
**These are my 3 key strengths today:**
- Deep technical expertise in marketing technologies and data platforms.
- Strong analytical and data-driven decision-making.
- Effective cross-functional collaboration and project management.

**These are 3 areas for development:**
- Leadership and team management skills.
- Advanced data governance and security knowledge.
- Enhanced communication and presentation skills for executive stakeholders.

**These are the 3 things to work on over the next 6-12 months:**
- Take on leadership roles in larger projects to build management experience.
- Pursue training or certifications in data governance and security.
- Develop and deliver presentations to executive teams to refine communication skills.
- Secure expanded access to key data systems to reduce dependencies.
- Participate in leadership training programs.
- Undertake courses in AI and machine learning relevant to marketing.
""")

st.header("Reflection Objective")
st.write("""
**What are you like at your best?**
- Innovative, strategic, and collaborative.
- Thriving in solving complex problems and driving meaningful change.

**How can your manager/team best support you to be at your best?**
- Providing opportunities for leadership, professional development, clear objectives, and regular feedback.
- Reducing dependency on other teams by providing more autonomy and access to necessary tools.
- Maintaining open communication, collaboration, and a collaborative work environment.

**What are you like when you’re not at your best?**
- Overly focused on details and less effective at delegating.
- Becoming frustrated and disengaged when facing bureaucratic hurdles or lack of resources.

**When the situation isn’t set up for you to show up at your best, what are things you want to work on?**
- Maintaining focus on strategic objectives.
- Improving stress management techniques.
- Seeking support when needed.
- Enhancing coding and automation skills to reduce reliance on the development team.

**Where do you want to grow in the coming year?**
- Leadership and team management.
- Expanding expertise in AI and machine learning applications for marketing.

**If you can show up as the leader and employee you aspire to be, what difference will it make?**
- Drive greater innovation and efficiency within the team.
- Create a more collaborative and motivated team environment.
- Lead to highly personalized and effective marketing campaigns, contributing to the company's growth and success.

**Are there specific goals you want to set for yourself for your growth and development?**
- Lead at least one major project from start to finish independently.
- Complete a leadership development program.
- Regularly present strategic initiatives and project outcomes to executive teams.
- Gain advanced certifications in data governance and security.
- Improve data integration and automation processes within the MarTech stack.
- Complete advanced certifications in AI and machine learning.
- Lead a major MarTech integration project demonstrating significant ROI.
- Develop and mentor a team of MarTech specialists.
""")

# Placeholder for environment variables
st.write(f"Secret Key: {os.getenv('SECRET_KEY')}")

