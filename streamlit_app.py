import streamlit as st
import base64

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="StreamWave Multimedia Analytics",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------
st.markdown("""
<style>

/* Sidebar width */
[data-testid="stSidebar"] {
    width: 180px;
}

/* Top Banner */
.main-header {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    padding: 18px 0;
    margin: -20px -20px 25px -20px;
    background: linear-gradient(90deg,#c77dff,#d1b3ff,#b388ff);
    color: white;
    box-shadow: 0 0 25px rgba(199,125,255,0.7);
}

.main-header img {
    height: 75px;
}

.main-header h1 {
    font-size: 2rem;
    font-weight: 700;
    margin: 0;
}

</style>
""", unsafe_allow_html=True)




def get_base64_image(image_file):
    with open(image_file, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_base64 = get_base64_image("medialogo.png")

# --------------------------------------------------
# TOP BANNER WITH LOGO
# --------------------------------------------------
st.markdown(f"""
<div class="main-header">
    <img src="data:image/png;base64,{logo_base64}">
    <h1>StreamWave Multimedia Analytics</h1>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
#st.sidebar.image("medialogo.png", use_container_width=True)

#st.sidebar.title("Navigation")
#st.sidebar.write("Dashboard Overview")
#st.sidebar.write("Executive Insights")

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "Multimedia Dashboard",
    "Executive Summary",
    "About Info"
])

# --------------------------------------------------
# TAB 1 – EMBED EXCEL
# --------------------------------------------------
with tab1:
    st.markdown("### Multimedia Performance Dashboard")

    st.components.v1.iframe(
        "https://1drv.ms/x/c/62ed36bcf96b63c6/IQALntCNbXfgS6l-xjpGRmwIAR937NlhVHD-3xxKZUZfdFQ?e=YrzfZO",
        height=780,
        scrolling=True
    )

# --------------------------------------------------
# TAB 2 – EXECUTIVE SUMMARY
# --------------------------------------------------
with tab2:

    st.markdown("## Genre Performance Insights")

    st.markdown("""
- **Drama** – Highest total views and strongest repeat rates  
- **Comedy** – High engagement with strong repeat behaviour  
- **Sci-Fi** – Strong viewership with franchise potential  
- **Action** – High excitement, moderate repeat engagement  
- **Documentary** – Stable engagement with opportunity for retention improvement  
""")

    st.markdown("---")

    st.markdown("##  Strategic Recommendations")

    st.markdown("""
- Increase investment in **Drama and Comedy**  
- Expand niche subgenres within **Comedy, Action, and Sci-Fi**  
- Diversify content offerings across Documentary, Sci-Fi, Action, Kids, and Horror  
- Enhance retention strategies for Biography  
- Refresh Documentary formats for broader appeal  
- Promote cross-genre collaboration initiatives  
- Align marketing spend with high repeat-performance genres  
""")

    st.markdown("---")

    st.markdown("##  Key Takeaways")

    st.markdown("""
- Prioritise high repeat-value genres for long-term ROI  
- Balance portfolio diversification with performance-driven investment  
- Develop serialised and franchise-ready content  
- Align marketing spend with engagement performance metrics  
""")

# --------------------------------------------------
# TAB 3 – ABOUT INFO
# --------------------------------------------------
with tab3:

    st.markdown("## About This Application")

    st.markdown("""
StreamWave Multimedia Analytics is an executive-facing analytics solution designed 
to evaluate multimedia content performance across genres.

The application integrates an interactive Excel dashboard with strategic insights 
to support data-driven decisions on content investment, marketing allocation, and 
portfolio diversification within a streaming platform environment.

It combines KPI design, genre-level performance analysis, and executive reporting 
to translate engagement data into actionable business strategy.
""")