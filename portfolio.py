import streamlit as st
import pandas as pd
import numpy as np
import json
import time
import datetime
import re

st.set_page_config(
    page_title="Aariz Bin Azmat | Software & Data Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

def inject_custom_css():
    st.markdown("""
    <style>
    /* Global Styles & Dark Theme Glassmorphism */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    code, kbd, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        color: #f8fafc;
    }

    /* Black text inside text fields and text areas when typing */
    div[data-baseweb="input"] input, 
    div[data-baseweb="textarea"] textarea,
    input, textarea {
        color: #000000 !important;
        background-color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.2s ease-in-out, border-color 0.2s ease-in-out;
    }

    .glass-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        transform: translateY(-2px);
    }

    .hero-title {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.2rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.3rem;
        font-weight: 400;
        margin-bottom: 1.5rem;
    }

    .stat-box {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }

    .stat-number {
        font-size: 2.2rem;
        font-weight: 800;
        color: #818cf8;
    }

    .stat-label {
        color: #94a3b8;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .skill-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        color: #a5b4fc;
        border: 1px solid rgba(99, 102, 241, 0.3);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 500;
        margin: 3px;
    }

    .status-active {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(34, 197, 94, 0.15);
        color: #4ade80;
        border: 1px solid rgba(34, 197, 94, 0.3);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
    }

    .terminal-window {
        background: #090d16;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 18px;
        font-family: 'JetBrains Mono', monospace;
        color: #38bdf8;
    }

    /* Streamlit UI Tweaks */
    div[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    div.stButton > button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #4338ca 0%, #6d28d9 100%);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

if 'cli_history' not in st.session_state:
    st.session_state.cli_history = [
        {"cmd": "welcome", "output": "Welcome to Aariz Bin Azmat's Interactive Developer Terminal. Type 'help' to view available commands."}
    ]

WORK_EXPERIENCE = [
    {
        "role": "Lead Data & Backend Engineer",
        "company": "Software Solutions",
        "period": "2026 - Present",
        "location": "Remote / Hybrid",
        "summary": "Architected high-throughput ETL pipelines and microservices processing daily event workflows.",
        "highlights": [
            "Engineered automated data ingestion workflows using Python, FastAPI, and PostgreSQL with high uptime.",
            "Reduced data processing latency by 42% through query optimization and caching layer implementation.",
            "Designed and implemented RESTful microservices with automated Swagger/OpenAPI documentation.",
            "Maintained clean code practices, PEP8 standards, and automated testing suites."
        ]
    },
    {
        "role": "Web & Python Developer",
        "company": "Tech Innovations",
        "period": "2025 - 2026",
        "location": "Remote",
        "summary": "Developed custom web applications and interactive analytics dashboards.",
        "highlights": [
            "Built responsive React & Python Streamlit web portals serving active users.",
            "Constructed database schemas, migration scripts, and ORM models.",
            "Integrated multi-tenant authentication systems using standard authentication protocols.",
            "Streamlined deployment pipelines using Docker containers and GitHub Actions."
        ]
    }
]

PROJECTS_DATA = [
    {
        "title": "AetherData - High-Throughput ETL Engine",
        "category": "Data Engineering & Python",
        "tech": ["Python", "FastAPI", "PostgreSQL", "Redis", "Docker"],
        "summary": "Distributed data pipeline platform capable of ingesting, validating, and transforming JSON telemetry feeds.",
        "architecture_flow": "Source Systems -> Data Ingestion -> Python Worker Nodes -> Validation Cache -> PostgreSQL Warehouse",
        "code_snippet": """def process_telemetry_batch(batch: List[Dict[str, Any]]) -> ProcessingReport:
    # Validate payload structure via Pydantic model
    validated_records = [TelemetryModel(**record) for record in batch]
    
    # Compute analytics aggregation
    df = pd.DataFrame([r.dict() for r in validated_records])
    cleaned_df = df.dropna(subset=['device_id', 'timestamp'])
    
    # Stream to persistent storage
    engine = create_db_engine()
    cleaned_df.to_sql('telemetry_logs', con=engine, if_exists='append', index=False)
    
    return ProcessingReport(processed=len(cleaned_df), status="SUCCESS")""",
        "stats": {"Throughput": "10,000 req/s", "Latency": "<15ms", "Test Coverage": "96%"}
    },
    {
        "title": "OmniStream - Analytics & Monitoring Platform",
        "category": "Web & Software Architecture",
        "tech": ["Python", "Streamlit", "Plotly", "SQLAlchemy"],
        "summary": "Interactive Web Application offering deep-dive analytics, real-time query builders, and automated reporting.",
        "architecture_flow": "Streamlit Frontend -> Web API Middleware -> Analytical SQL Engine -> Dynamic Visualizer",
        "code_snippet": """@st.cache_data(ttl=300)
def fetch_analytics_metrics(start_date: str, end_date: str) -> pd.DataFrame:
    query = f'''
        SELECT date_trunc('hour', timestamp) as time_bucket,
               service_name,
               AVG(latency_ms) as avg_latency,
               COUNT(*) as request_count
        FROM server_metrics
        WHERE timestamp BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY 1, 2 ORDER BY 1 ASC
    '''
    return pd.read_sql(query, con=db_connection)""",
        "stats": {"Query Exec Speed": "0.14s", "Uptime": "99.95%"}
    }
]

with st.sidebar:
    st.image("https://placehold.co/150x150/1e1b4b/818cf8?text=ABA", width=120)
    st.markdown("### **Aariz Bin Azmat**")
    st.markdown("<p style='color: #94a3b8; font-size: 0.85rem;'>Web Developer | Data Specialist</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='status-active'>🟢 Available for Developer Roles</div>", unsafe_allow_html=True)
    st.divider()
    
    navigation_option = st.radio(
        "Navigation",
        [
            "🏠 Profile & Overview",
            "💼 Professional Experience",
            "🛠 Technical Skills Matrix",
            "🚀 Interactive Project Gallery",
            "📊 Data Management & ETL Studio",
            "🌐 REST API & Microservice Explorer",
            "🏗 Architecture & Schema Visualizer",
            "💻 Interactive Terminal Console",
            "📩 Contact & Inquiry"
        ]
    )
    
    st.divider()
    st.markdown("#### Quick Links")
    st.markdown("[👔 LinkedIn Profile](https://www.linkedin.com/in/aariz-bin-azmat-43320242b)")
    # Updated GitHub URL to open your GitHub profile page
    st.markdown("[🐙 GitHub Repositories](https://github.com/aarizdeadshot-droid)")
    
    st.caption("© 2026 Aariz Bin Azmat. Built with Python & Streamlit.")

if navigation_option == "🏠 Profile & Overview":
    st.markdown("<div class='hero-title'>Aariz Bin Azmat</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-subtitle'>Web Developer | Python Engineer | Data Management Specialist | Software Developer</div>", unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>1+</div>
            <div class='stat-label'>Years Experience</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>10+</div>
            <div class='stat-label'>Projects Delivered</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>10K+</div>
            <div class='stat-label'>Daily Data Records</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>99.9%</div>
            <div class='stat-label'>System Uptime SLA</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_bio, col_summary = st.columns([1.5, 1])
    
    with col_bio:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("👨‍💻 Executive Summary")
        st.write("""
        I am a passionate **Web Developer, Python Engineer, and Data Management Specialist** focused on building clean backend web systems, reliable data workflows, and interactive analytics dashboards.
        
        My expertise bridges software development, structured data processing, and modern web interfaces. Whether developing dynamic web tools using Streamlit, crafting automated data extraction frameworks, or writing structured SQL databases, my focus is always on maintainability and performance.
        """)
        
        st.markdown("#### Primary Domains of Expertise")
        skills_tags = [
            "Python Backend", "RESTful APIs", "ETL Data Pipelines",
            "SQL / Relational Databases", "Web Application Architecture",
            "Docker Containerization", "Data Cleaning & Parsing", "Interactive Dashboards"
        ]
        tag_html = "".join([f"<span class='skill-badge'>{tag}</span>" for tag in skills_tags])
        st.markdown(tag_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_summary:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("⚡ Core Focus Areas")
        
        st.markdown("**1. Data Pipelines & Engineering**")
        st.progress(92)
        
        st.markdown("**2. Python Development**")
        st.progress(95)
        
        st.markdown("**3. Web Development & Dashboards**")
        st.progress(90)
        
        st.markdown("**4. Database Design & Optimization**")
        st.progress(88)
        
        st.markdown("**5. Cloud & Deployment (Docker, Git)**")
        st.progress(82)
        st.markdown("</div>", unsafe_allow_html=True)

elif navigation_option == "💼 Professional Experience":
    st.title("💼 Professional Experience & Capability Matrix")
    st.write("A track record of engineering web applications, backend services, and automated data workflows.")
    
    for exp in WORK_EXPERIENCE:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        c1, c2 = st.columns([3, 1])
        with c1:
            st.subheader(f"{exp['role']}")
            st.markdown(f"**{exp['company']}** • *{exp['location']}*")
        with c2:
            st.markdown(f"<p style='text-align: right; color: #818cf8; font-weight: 600;'>{exp['period']}</p>", unsafe_allow_html=True)
            
        st.write(exp['summary'])
        
        st.markdown("**Key Accomplishments:**")
        for hl in exp['highlights']:
            st.markdown(f"• {hl}")
            
        st.markdown("</div>", unsafe_allow_html=True)

elif navigation_option == "🛠 Technical Skills Matrix":
    st.title("🛠 Technical Skills & Competency Matrix")
    st.write("Comprehensive technical stack breakdown across software engineering and data disciplines.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🐍 Python & Software Development")
        st.markdown("""
        - **Languages:** Python 3.x, SQL, JavaScript, HTML5/CSS3
        - **Web Frameworks:** Streamlit, FastAPI, Flask
        - **Database Tooling:** SQLite, PostgreSQL, MySQL
        - **Testing & Quality:** PyTest, Pydantic
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_b:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📊 Data Engineering & Tools")
        st.markdown("""
        - **Data Processing:** Pandas, NumPy
        - **Visualization:** Plotly, Matplotlib
        - **DevOps & Tools:** Git, GitHub, Docker, VS Code
        """)
        st.markdown("</div>", unsafe_allow_html=True)

elif navigation_option == "🚀 Interactive Project Gallery":
    st.title("🚀 Interactive Project Showcase & Engineering Gallery")
    st.write("Explore software solutions engineered by Aariz Bin Azmat.")
    
    for proj in PROJECTS_DATA:
        with st.expander(f"📌 {proj['title']}", expanded=True):
            st.markdown(f"**Category:** {proj['category']}")
            st.write(proj['summary'])
            
            tech_html = " ".join([f"<span class='skill-badge'>{t}</span>" for t in proj['tech']])
            st.markdown(f"**Technologies Used:** {tech_html}", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            col_left, col_right = st.columns([1, 1])
            with col_left:
                st.markdown("#### System Metrics")
                for k, v in proj['stats'].items():
                    st.metric(label=k, value=v)
                st.markdown("**System Architecture Flow:**")
                st.info(proj['architecture_flow'])
                
            with col_right:
                st.markdown("#### Core Implementation Snippet")
                st.code(proj['code_snippet'], language='python')

elif navigation_option == "📊 Data Management & ETL Studio":
    st.title("📊 Data Management & ETL Transformation Studio")
    st.write("Demonstration of real-time dataset ingestion, parsing, cleaning, and metric computation.")
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("1. Live Raw Dataset Generator")
    
    np.random.seed(42)
    n_rows = st.slider("Select Sample Record Count for Pipeline Processing", 10, 200, 30)
    
    raw_data = {
        "record_id": [f"REC-{1000+i}" for i in range(n_rows)],
        "client_name": np.random.choice(["Acme Corp", "Beta Tech", "Gamma Global", None, "Delta Logistics"], n_rows),
        "transaction_amount": np.random.choice([150.5, 2300.0, None, -50.0, 4500.25, 890.0], n_rows),
        "status": np.random.choice(["PENDING", "COMPLETED", "FAILED", "completed", "pending"], n_rows)
    }
    
    df_raw = pd.DataFrame(raw_data)
    st.markdown("**Raw Ingested Data (Contains missing values & raw strings):**")
    st.dataframe(df_raw.head(10), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("2. Execute Automated Data Cleaning Pipeline")
    
    if st.button("⚡ Run Data Pipeline"):
        with st.spinner("Cleaning and normalizing data..."):
            time.sleep(0.5)
            
            df_cleaned = df_raw.copy()
            df_cleaned['client_name'] = df_cleaned['client_name'].fillna("Unknown Client")
            df_cleaned['transaction_amount'] = df_cleaned['transaction_amount'].apply(lambda x: abs(x) if x is not None and x < 0 else x)
            df_cleaned['transaction_amount'] = df_cleaned['transaction_amount'].fillna(df_cleaned['transaction_amount'].median())
            df_cleaned['status'] = df_cleaned['status'].str.upper()
            
            st.success("Pipeline Executed Successfully! Data normalized.")
            st.dataframe(df_cleaned.head(10), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif navigation_option == "🌐 REST API & Microservice Explorer":
    st.title("🌐 REST API Simulator")
    st.write("Test sample API endpoints built in Python.")
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    endpoint = st.selectbox(
        "Select API Endpoint",
        [
            "GET /api/v1/healthcheck",
            "GET /api/v1/developer/profile"
        ]
    )
    
    if st.button("🚀 Send HTTP Request"):
        time.sleep(0.3)
        st.markdown("<span class='status-active'>STATUS: 200 OK</span>", unsafe_allow_html=True)
        if "healthcheck" in endpoint:
            resp = {"status": "HEALTHY", "database": "CONNECTED", "redis_cache": "READY"}
        else:
            resp = {
                "developer": "Aariz Bin Azmat",
                "roles": ["Web Developer", "Python Developer", "Data Management Specialist"]
            }
        st.json(resp)
    st.markdown("</div>", unsafe_allow_html=True)

elif navigation_option == "🏗 Architecture & Schema Visualizer":
    st.title("🏗 Architecture Blueprint")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("System Data Flow Architecture")
    st.markdown("""""")
    st.markdown("</div>", unsafe_allow_html=True)

elif navigation_option == "💻 Interactive Terminal Console":
    st.title("💻 Interactive Developer CLI Console")
    
    st.markdown("<div class='terminal-window'>", unsafe_allow_html=True)
    st.markdown("**Aariz Terminal (v1.0.0)** - Type `help` to list commands.")
    st.markdown("---")
    
    for entry in st.session_state.cli_history:
        st.markdown(f"<span style='color: #4ade80;'>aariz@portfolio:~$</span> {entry['cmd']}", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #cbd5e1; margin-left: 15px;'>{entry['output']}</p>", unsafe_allow_html=True)
        
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    cmd_input = st.text_input("Enter command:", key="cli_input_box")
    
    if st.button("Execute Command"):
        if cmd_input.strip():
            cmd = cmd_input.strip().lower()
            if cmd == "help":
                output = "Commands: bio, skills, projects, clear"
            elif cmd == "bio":
                output = "Aariz Bin Azmat - Web Developer, Python Developer, Data Management Specialist."
            elif cmd == "skills":
                output = "Python, Streamlit, Pandas, PostgreSQL, Docker, REST APIs, HTML/CSS."
            elif cmd == "projects":
                output = "1. AetherData Engine | 2. OmniStream Analytics"
            elif cmd == "clear":
                st.session_state.cli_history = []
                st.rerun()
            else:
                output = f"Command not recognized: '{cmd}'. Type 'help' for available commands."
                
            st.session_state.cli_history.append({"cmd": cmd_input, "output": output})
            st.rerun()

elif navigation_option == "📩 Contact & Inquiry":
    st.title("📩 Contact & Direct Inquiry")
    st.write("Feel free to send a message regarding projects or developer roles!")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        submitted = st.form_submit_button("Send Message")
        if submitted:
            if name and email and message:
                st.success(f"Thank you {name}! Your message has been sent.")
            else:
                st.error("Please fill in all fields before submitting.")
