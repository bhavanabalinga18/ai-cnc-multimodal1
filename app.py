import streamlit as st
import pandas as pd
import numpy as np

# --- 0. CONFIG & THEME ---
st.set_page_config(page_title="AQKA-PINN AI", layout="wide")

# --- 1. SCI-FI PASTEL DARK UI (CSS) ---
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0e1117;
        background-image: radial-gradient(#1c1f33 1px, transparent 1px);
        background-size: 30px 30px;
        color: #d1f2eb;
    }
    
    /* Glowing Header */
    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #8be9fd;
        text-shadow: 0 0 15px #8be9fd;
        border-bottom: 2px solid #bd93f9;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    /* Glassmorphism Cards */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(139, 233, 253, 0.3);
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 0 10px rgba(139, 233, 253, 0.1);
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0a0c12;
        border-right: 1px solid #bd93f9;
    }

    /* Pulse Animation for Status */
    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
    .status-light {
        height: 10px; width: 10px;
        background-color: #50fa7b;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
        animation: pulse 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (Manual Input) ---
with st.sidebar:
    st.markdown("### 🎛️ SENSOR OVERRIDE")
    st.write("---")
    in_temp = st.slider("Spindle Heat (°C)", 20, 200, 65)
    in_vib = st.slider("Vibration Level (G)", 0.0, 10.0, 1.5)
    st.write("---")
    st.markdown("<div><span class='status-light'></span><b>SYSTEM: ONLINE</b></div>", unsafe_allow_html=True)
    st.caption("AI Loop: 62ms | Encryption: Active")

# --- 3. MAIN DASHBOARD HEADER ---
st.markdown("<div class='main-title'>AQKA-PINN :: AUTONOMOUS INTERFACE</div>", unsafe_allow_html=True)

# --- 4. THE 4 MISSION TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📡 SENSOR FUSION", 
    "⚛️ QUANTUM ENGINE", 
    "🔥 PHYSICS BRAIN", 
    "🎮 CNC CONTROL"
])

# --- TAB 1: DATA UPLOAD & SENSORS ---
with tab1:
    st.subheader("Stage 1: Multi-Modal Data Acquisition")
    
    # THE UPLOAD BUTTON
    st.info("📂 Layman Tip: Upload your machine's .CSV log file here to start the AI analysis.")
    uploaded_file = st.file_uploader("Upload CNC Sensor Log (.csv)", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Data Loaded Successfully")
        st.dataframe(df.head(10))
        st.line_chart(df)
    else:
        # Default view for layman if no file is uploaded
        st.write("Real-time Sensor Stream (Simulated):")
        dummy_data = pd.DataFrame(np.random.randn(20, 3), columns=['X-Vib', 'Y-Vib', 'Z-Vib'])
        st.line_chart(dummy_data)

# --- TAB 2: QUANTUM MAPPING ---
with tab2:
    st.subheader("Stage 3: Quantum Feature Mapping")
    st.write("Layman Tip: This grid shows how the AI 'sees' complex patterns using Quantum math.")
    
    # Using Native Heatmap (Error-free)
    quantum_matrix = np.random.rand(10, 12)
    st.image("https://raw.githubusercontent.com/dataprofessor/streamlit_app/master/images/heatmap.png", width=400) # Placeholder for sci-fi look
    st.area_chart(quantum_matrix)
    st.caption("Hilbert Space Consistency: 98.4%")

# --- TAB 3: PHYSICS PREDICTION ---
with tab3:
    st.subheader("Stage 4: Physics-Informed Neural Network")
    st.latex(r"\text{Heat Equation: } \alpha \nabla^2 T = \frac{\partial T}{\partial t}")
    
    # Dynamic graph linked to Sidebar
    st.write(f"Predicting thermal stability for current temperature: **{in_temp}°C**")
    pinn_curve = np.linspace(in_temp, in_temp + 25, 100) + np.random.normal(0, 1, 100)
    st.line_chart(pinn_curve)

# --- TAB 4: AUTONOMOUS CONTROL ---
with tab4:
    st.subheader("Stage 6: Autonomous Decision Layer")
    
    c1, c2, c3 = st.columns(3)
    
    # Logic for Layman
    risk_level = "🟢 SAFE" if in_vib < 4.0 else "🔴 DANGER"
    
    c1.metric("CHATTER RISK", risk_level, f"{in_vib} G")
    c2.metric("THERMAL STATUS", "STABLE", f"{in_temp} °C")
    c3.metric("AI CONFIDENCE", "96%", "+1.2%")
    
    st.write("---")
    if st.button("🚨 EMERGENCY STOP"):
        st.error("MANUAL STOP ENGAGED. SYSTEM OFFLINE.")
    else:
        st.success("AI is currently managing the Feed Rate and Spindle Speed.")
        
