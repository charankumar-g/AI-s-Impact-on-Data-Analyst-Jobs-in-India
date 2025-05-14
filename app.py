import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI's Impact on Data Analyst Jobs in India", layout="wide", page_icon="🤖")

# ---- HEADER ----
st.title("🤖 AI’s Impact on Data Analyst Jobs in India")
st.markdown("""
This interactive portfolio project explores how **Artificial Intelligence (AI)** is reshaping the **Data Analyst job market** in India using a demo dataset and **Tableau dashboards**.
""")

# ---- PROJECT HIGHLIGHTS ----
st.header("🔍 Project Highlights")
st.markdown("""
- 📍 Location-based job demand
- 🧠 Top skills in demand
- 💼 AI vs Non-AI job role insights
- 💰 Salary vs experience comparison
- 😊 Sentiment toward AI in job descriptions
""")

# ---- IMAGE DISPLAY ----
st.header("📸 AI Impact Dashboard")
st.image("assets/ai_impact_dashboard.png", caption="AI Impact on Data Analyst Jobs in India", use_container_width=True)

# ---- DATASET INFO ----
st.header("📚 Dataset Info")
st.markdown("""
**Source**: `LinkedIn_India_DataAnalyst_500_AI_Impact.xlsx`  
- Manually curated & cleaned demo dataset  
- Contains 500+ job records from LinkedIn  
- Fields include: Company, Location, Skills, Salary, Experience, AI Sentiment
""")

# ---- PREVIEW DATA ----
data = pd.read_excel("LinkedIn_India_DataAnalyst_500_AI_Impact.xlsx")
with st.expander("📄 Preview Dataset"):
    st.dataframe(data.head(10), use_container_width=True)

# ---- INSIGHTS ----
st.header("📊 Key Insights")
st.markdown("""
✅ **AI-related roles offer higher salaries** for similar experience levels  
✅ In-demand skills: **Python, Data Modeling, BigQuery, Tableau, Snowflake**  
✅ High job demand in **Kolkata, Ahmedabad, Hyderabad**  
✅ **Positive sentiment** dominates AI’s perceived job market impact  
✅ Job roles are almost **evenly split** between AI and Non-AI listings  
""")

# ---- DASHBOARD EMBED ----
st.header("📈 Interactive Tableau Dashboard")
st.markdown("👉 **[Open in new tab](https://public.tableau.com/views/AIsImpactonDataAnalystJobsinIndia/AIImpact-DataAnalystJobMarketIndia)** for full screen view.")

st.components.v1.iframe(
    "https://public.tableau.com/views/AIsImpactonDataAnalystJobsinIndia/AIImpact-DataAnalystJobMarketIndia?:language=en-GB&:display_count=n&:origin=viz_share_link",
    height=650, scrolling=True
)

# ---- FOOTER ----
st.markdown("---")
st.subheader("📬 Connect with Me")
st.markdown("""
- 🔗 [LinkedIn](https://linkedin.com/in/charankumar-g)  
- 📧 [charankumar.career@gmail.com](mailto:charankumar.career@gmail.com)
""")
