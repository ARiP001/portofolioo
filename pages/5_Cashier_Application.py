import streamlit as st

st.set_page_config(page_title="Cashier Application", layout="wide")

# --- HEADER & HERO IMAGE ---
st.markdown("""
<div style="text-align: center;">
    <h1 style="margin: 0;">Java OOP Cashier Application: A Point of Sale System</h1>
</div>
""", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1556740738-b6a63e27c4df?w=1200", caption="A real-world POS solution built from user interviews.")

st.write("---")

# --- PROBLEM & SOLUTION ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            🛒 The Challenge: Solving a Real Minimarket's Problem
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    This project originated from a **real-world problem**. The challenge was to design and build a functional desktop Point of Sale (POS) application after **interviewing a local minimarket owner** to understand their daily operational pain points, such as inefficient transaction processes and manual sales tracking.

    **The solution is a desktop POS application built with Java**, grounded in strong **Object-Oriented Programming (OOP)** principles. The application provides a user-friendly interface to handle sales, manage products, and generate reports, directly addressing the needs identified in the user interview.
    """)

# --- MY ROLE ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            👨‍💻 My Role: Java Developer
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    This was a **GROUP PROJECT** developed by a two-person team. My role was **Java Developer**, where my core responsibilities involved architecting the backend logic and **implementing the code from the Figma design**.
    """)

st.write("---")

# --- TECHNICAL PROCESS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: white; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            ⚙️ My Technical Process: From Design to Functional Code
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("My process focused on building a robust and maintainable application by separating design and logic:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                🧱 1. Object-Oriented Architecture
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        The application's backbone is its **OOP structure**. I designed a robust class hierarchy to model key real-world entities like `Products`, `Transactions`, and `Receipts`.
        
        This approach utilized key OOP principles:
        - **Encapsulation:** Bundling data and methods within classes.
        - **Inheritance & Polymorphism:** Creating a maintainable and scalable code structure.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 12px; border-radius: 6px; margin: 8px 0;">
            <h3 style="color: #333; margin: 0; text-align: center; font-size: 1.2em;">
                🎨 2. Figma to GUI Implementation
            </h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        I translated the high-fidelity UI/UX designs from **Figma** into a fully interactive graphical user interface (GUI) using **Java Swing/JavaFX**.
        
        This involved coding all the visual components for key features, such as:
        - Processing sales and adding items to a cart.
        - A feature to **download sales reports in PDF format**, providing a tangible business tool.
        """)

# --- FINAL RESULT & LEARNINGS ---
with st.container():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            🎯 The Final Result: A User-Centric POS Application
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("The final product is a functional desktop application that directly solves the problems identified during our initial user interview, demonstrating a complete product development cycle.")
    
    # Display cashier application images
    st.markdown("### 📱 Application Screenshots")
    
    # Create tabs for different features
    tab1, tab2, tab3, tab4 = st.tabs(["🔐 Login", "🛒 Transaction", "📦 Item Management", "📄 PDF Report"])
    
    with tab1:
        st.image("assets/kasir-login.png", caption="Login Interface - Secure authentication system for cashier access")
    
    with tab2:
        st.image("assets/kasir-transaksi.png", caption="Transaction Interface - Point of sale system for processing customer purchases")
    
    with tab3:
        st.image("assets/kasir-item.png", caption="Item Management - Product catalog and inventory management system")
    
    with tab4:
        st.image("assets/kasir-pdf-report.png", caption="PDF Report Generation - Automated sales report generation in PDF format")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%); padding: 15px; border-radius: 8px; margin: 15px 0;">
        <h2 style="color: #333; text-align: center; margin: 0; font-size: 1.6em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
            💡 Learnings & Personal Impact
        </h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    1.  **User-Driven Development:** This project taught me the immense value of starting with a real user problem. Translating direct feedback from an interview into technical requirements was a crucial learning experience.
    2.  **Practical OOP Application:** It solidified my ability to apply theoretical **OOP** concepts to solve a practical business need and architect a maintainable code structure.
    3.  **Design to Product Pipeline:** This project honed my skills in translating a visual design from **Figma** into a functional product, reinforcing my drive to build complete, user-centric solutions at the **Apple Developer Academy**.
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
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 6])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/1200px-Java_programming_language_logo.svg.png", width=50, caption="Java")
    

    st.markdown("""
    - **[View the Code on GitHub](your-github-link-here)**
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
    st.page_link("pages/4_Bike_Sharing_Data_Analytic.py", label="⬅️ Previous Project: Bike Sharing", icon="🚲")

with col3:
    st.page_link("Dashboard.py", label="Back to Dashboard 🏠", icon="🏠")

