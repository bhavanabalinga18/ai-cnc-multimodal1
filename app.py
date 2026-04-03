import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

# --- 0. STRESS CONFIG ---
st.set_page_config(page_title="AQKA-PINN INTERFACE", layout="wide", initial_sidebar_state="collapsed")

# --- 1. THE HIGH-FIDELITY SCI-FI CSS INJECTION ---
# This block handles the colors, glassmorphism, and blinking animations.
st.markdown("""
<style>
    /* Global Background - Deep Pastel Dark */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(18, 20, 31) 0%, rgb(10, 11, 18) 100%);
        color: #d1f2eb; /* Main text pastel cyan */
        font-family: 'Space Mono', 'Courier New', monospace;
    }

    /* --- Define Keyframes for Animations --- */
    /* Blinking for Alerts */
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.1; } 100% { opacity: 1; } }
    /* Pulsing for Active Status */
    @keyframes pulse-glow { 0% { box-shadow: 0 0 5px rgba(189, 147, 249, 0.2); } 50% { box-shadow: 0 0 15px rgba(189, 147, 249, 0.6); } 100% { box-shadow: 0 0 5px rgba(189, 147, 249, 0.2); } }

    /* Glassmorphism Block Cards */
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric) {
        background: rgba(26, 28, 41, 0.6) !important;
        border: 1px solid rgba(139, 233, 253, 0.2) !important; /* Pastel Cyan border */
        border-radius: 12px;
        padding: 20px;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease, border 0.3s ease;
    }
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric):hover {
        border: 1px solid rgba(189, 147, 249, 0.7); /* Pastel Purple border on hover */
        transform: translateY(-2px);
    }

    /* Blinking Status Indicator */
    .status-active {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #8be9fd;
        border-radius: 50%;
        margin-right: 8px;
        animation: blink 1.5s infinite;
        box-shadow: 0 0 8px #8be9fd;
    }

    /* Pulsing Global Border effect */
    .pinn-header-pulse {
        border-bottom: 2px solid rgba(189, 147, 249, 0.1);
        animation: pulse-glow 3s infinite;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    /* Sidebar - Pastel Purple Glow */
    [data-testid="stSidebar"] {
        background-color: rgba(14, 16, 24, 0.98);
        border-right: 2px solid rgba(189, 147, 249, 0.3);
    }

    /* Neon Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: transparent; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(26, 28, 41, 0.7);
        border: 1px solid rgba(139, 233, 253, 0.1);
        border-radius: 8px 8px 0px 0px;
        color: #d1f2eb;
        padding: 10px 18px;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(189, 147, 249, 0.15) !important;
        border: 1px solid #bd93f9 !important; /* Pastel Purple */
        color: #f8f8f2;
        text-shadow: 0 0 8px #bd93f9;
    }

    /* Metric Label Colors */
    [data-testid="stMetricLabel"] { color: #8be9fd !important; text-transform: uppercase; letter-spacing: 1px; }
    [data-testid="stMetricValue"] { color: #f8f8f2 !important; text-shadow: 0 0 10px #f8f8f2; }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR CONTROL CONSOLE ---
with st.sidebar:
    st.markdown("### 🎛️ CORE INJECTORS")
    st.write("---")
    in_temp = st.slider("SPINDLE THERMAL (C°)", 20, 250, 68)
    in_vib = st.slider("VIBRATION AMPLITUDE (G)", 0.0, 10.0, 1.1)
    st.write("---")
    
    # Custom HTML for blinking status
    st.markdown("""
    <div style='background:rgba(26,28,41,0.8); padding:10px; border-radius:8px; border:1px solid rgba(189,147,249,0.3);'>
        <h4><span class='status-active'></span> SYSTEM SYNC: ACTIVE</h4>
        <caption style='color:#bd93f9;'>LOOP CYCLE: 62ms<br>FRAME: PINN-ADAPTIVE</caption>
    </div>
    """, unsafe_allow_html=True)

# --- 3. HEADER SECTION ---
# Add the pulsating header bar effect via class
st.markdown("<div class='pinn-header-pulse'>", unsafe_allow_html=True)
c_t1, c_t2 = st.columns([4, 1])
with c_t1:
    st.title("🤖 AQKA-PINN :: MISSION INTERFACE")
    st.markdown("`INTEGRATED QUANTUM-PHYSICS AUTONOMOUS MACHINING LAYER`")
with c_t2:
    st.metric("LATENCY", "62ms", "-1ms", help="Autonomous control loop frequency")
st.markdown("</div>", unsafe_allow_html=True)

# --- 4. MAIN INTERFACE TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📡 SENSOR FUSION", 
    "⚛️ QUANTUM ENGINE", 
    "🔥 PHYSICS BRAIN", 
    "🎮 CNC ACTUATION"
])

# --- TAB 1: SENSOR FUSION ---
with tab1:
    st.subheader("MULTIMODAL SENSOR STREAM (STAGE 1 & 2)")
    # simulated live vibration oscilliscope
    chart_data = pd.DataFrame(np.random.randn(25, 3), columns=['X', 'Y', 'Z'])
    st.line_chart(chart_data)
    st.caption("RAW VIBRATION SPECTRA (G/Hz)")

# --- TAB 2: QUANTUM ENGINE ---
with tab2:
    st.subheader("ADAPTIVE QUANTUM KERNEL MAP (STAGE 3)")
    # Pastel Dark Heatmap
    z_data = np.random.rand(14, 14)
    fig = go.Figure(data=go.Heatmap(
        z=z_data,
        # Dark Pastel Colorscale (Dark Blue -> Pastel Purple -> Pastel Cyan)
        colorscale=[[0, '#0a0b12'], [0.5, '#bd93f9'], [1, '#8be9fd']],
        showscale=False
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)
    st.info("HILBERT SPACE CONSISTENCY: 98.6%")

# --- TAB 3: PHYSICS BRAIN ---
with tab3:
    st.subheader("PINN PHYSICS CONSTRAINTS (STAGE 4)")
    cp1, cp2 = st.columns([1, 2])
    with cp1:
        st.latex(r"\nabla^2 T + \frac{Q}{k} = \frac{1}{\alpha}\frac{\partial T}{\partial t}")
        st.markdown("`[PINN THERMAL LOSS: 0.00019]`")
    with cp2:
        # Predicted vs Actual
        t_range = np.linspace(in_temp-15, in_temp+20, 100)
        # Use simple line chart, color set by global CSS
        st.line_chart(t_range)
        st.caption("PINN-CORRECTED THERMAL TRAJECTORY")

# --- TAB 4: CNC ACTUATION ---
with tab4:
    st.subheader("MPC DECISION & CONTROL LOOP (STAGE 5 & 6)")
    m1, m2, m3, m4 = st.columns(4)
    
    # Logic: High vibration triggers alert via delta
    chatter_risk = "LOW" if in_vib < 4.5 else "HIGH"
    vib_delta = f"{in_vib}G"
    chatter_color = "Normal" if chatter_risk == "LOW" else "inverse" # Blinking controlled by global CSS metric override for inverse would be needed, but we keep it basic
    
    m1.metric("CHATTER", chatter_risk, vib_delta, delta_color=chatter_color)
    m2.metric("THERMAL", "OPTIMAL", f"{in_temp}°C", delta_color="Normal")
    m3.metric("TOOL WEAR", "0.24mm", "0.01", delta_color="Normal")
    m4.metric("FEED RATE", "115%", "5%")

    st.write("---")
    st.success("🤖 AUTONOMOUS CONTROL LOOP ACTIVE")
    
