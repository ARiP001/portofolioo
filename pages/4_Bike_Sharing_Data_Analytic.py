import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Analysis", layout="wide")

# --- HEADER & HERO IMAGE ---
st.markdown("""
<div style="text-align: center;">
    <h1 style="margin: 0;">Bike Sharing Data Analysis: Uncovering Usage Patterns</h1>
</div>
""", unsafe_allow_html=True)

st.write("---")

# --- PROBLEM & SOLUTION ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            📊 The Challenge: Understanding Bike Rental Dynamics
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    Bike sharing systems generate a massive amount of data, but raw data alone doesn't provide actionable insights. The challenge of this project was to dive into the Capital Bikeshare historical dataset to answer critical business questions: What are the seasonal trends? How do user types differ? And how do weather conditions impact rental demand?

    **The solution is a comprehensive data analysis project,** using **Python** and its data science libraries to transform raw data into a clear and insightful story. The project culminates in an interactive **Streamlit dashboard** where users can explore these patterns themselves.
    """)

# --- MY ROLE ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            👨‍💻 My Role: Data Analyst
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    This was an **INDIVIDUAL PROJECT**. As the sole **Data Analyst**, I was responsible for the **entire analysis workflow**, from data cleaning and preprocessing to creating visualizations and interpreting the final results.
    """)

st.write("---")

# --- TECHNICAL PROCESS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            ⚙️ My Technical Process: From Raw Data to Actionable Insights
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("My process involved two main stages to ensure the data was clean and the analysis was robust:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                🧼 1. Data Wrangling & Preprocessing
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        The first step was to ensure data quality using **Pandas**. This included:
        - **Renaming columns** for better readability.
        - **Handling outliers** in the 'casual' user data using the IQR method.
        - **Feature Engineering** by creating a custom 'windspeed category' (Calm, Windy, Strong Wind) to better classify wind conditions for analysis.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                📈 2. Exploratory Data Analysis (EDA)
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        With clean data, I used **Matplotlib** and **Seaborn** to create a series of visualizations to answer the business questions. This included:
        - **Stacked bar charts** to compare casual vs. registered users across seasons.
        - **Time-series line plots** to show monthly rental trends.
        - **Scatter plots with regression lines** to analyze the correlation between temperature and rental counts.
        """)

# --- FINAL RESULT & LEARNINGS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            🎯 The Final Result: Key Business Insights
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("The analysis revealed several key insights that could help optimize the bike sharing service:")
    
    # Display bike sharing analysis images
    st.markdown("### 📊 Analysis Results & Visualizations")
    
    # Create tabs for different analysis aspects
    tab1, tab2, tab3, tab4 = st.tabs(["👥 User Types", "📅 Monthly Trends", "🌡️ Temperature Impact", "💨 Wind Effects"])
    
    with tab1:
        st.image("assets/bike-casual-vs-member.png", caption="Casual vs Member Users Analysis - Registered members are the dominant user group, especially in the summer")
    
    with tab2:
        st.image("assets/bike-montly.png", caption="Monthly Rental Trends - Clear seasonal patterns showing peak usage during warmer months")
    
    with tab3:
        st.image("assets/bike-temp-vs-serveice.png", caption="Temperature vs Service Usage - Rental counts show a clear positive correlation with temperature")
    
    with tab4:
        st.image("assets/bike-wind-effect.png", caption="Wind Effects on Bike Sharing - Analysis of how wind conditions impact rental patterns")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            💡 Learnings & Personal Impact
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    1.  **End-to-End Data Storytelling:** This project solidified my ability to manage a complete data analysis lifecycle, from asking the right questions to delivering data-driven stories through clear visualizations.
    2.  **Turning Analysis into a Product:** By developing and deploying an interactive **Streamlit dashboard**, I learned how to present complex data insights in an accessible, user-friendly format, turning a static analysis into a dynamic data product.
    3.  **Real-World Impact:** This experience deepened my understanding of how external factors impact real-world behavior and is why I am eager to apply these skills in the collaborative, product-focused environment of the **Apple Developer Academy**.
    """)

st.write("---")

# --- TECHNOLOGIES & LINKS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            🛠️ Technologies Used & Project Links
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 5])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=50, caption="Python")
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg", width=50, caption="Pandas")
    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg", width=50, caption="Matplotlib")
    with col4:
        st.image("https://seaborn.pydata.org/_images/logo-mark-lightbg.svg", width=50, caption="Seaborn")

    st.markdown("""
    - **[View the Code on GitHub](https://github.com/ARiP001/Bike-Sharing-Data-Analyst)**
    - **[View the Interactive Dashboard](https://bike-sharing-data-analyst-dicoding.streamlit.app/)**
    """)

st.write("---")

# --- NAVIGATION ---
st.markdown("""
<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
    <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
        🚀 Navigate Projects
    </h2>
</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.page_link("pages/3_Crypto_Tracker_-_Crypto_Currency_Simulator.py", label="⬅️ Previous Project: Crypto Tracker", icon="📈")

with col3:
    st.page_link("pages/5_Cashier_Application.py", label="Next Project: Cashier Application ➡️", icon="🛒")

