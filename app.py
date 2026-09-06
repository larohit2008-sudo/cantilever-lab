import math
import streamlit as st
import matplotlib.pyplot as plt

# --- 1. WEB PAGE INITIALIZATION ---
st.set_page_config(page_title="Cantilever Multivariable Deflection Lab", layout="wide")
st.title("Cantilever Multivariable Deflection Lab")

# --- 2. INPUT CONTROL DASHBOARD (SIDEBAR) ---
st.sidebar.header("Base Metrics Configuration")

base_w = st.sidebar.number_input("Base Weight (g)", min_value=1.0, value=75.0, step=1.0)
base_l = st.sidebar.number_input("Base Length (cm)", min_value=1.0, value=80.0, step=1.0)
base_d = st.sidebar.number_input("Base Depth (mm)", min_value=0.1, value=5.0, step=0.5)

# --- 3. PHYSICS COMPUTATION ENGINE ---
# Global Physics Constants
Y = 70 * math.pow(10, 9)
width_m = 3 * (10 ** -3)

try:
    # SCENARIO 1: Weight is CONSTANT (Varying Length & Depth)
    x_lengths_cm = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    y_depths_mm = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    depressions_1 = []

    for l_cm, d_mm in zip(x_lengths_cm, y_depths_mm):
        w = base_w * (10 ** -3)
        l = l_cm * (10 ** -2)
        d = d_mm * (10 ** -1)
        y_val = (4 * w * (l ** 3)) / (Y * width_m * (d ** 3))
        depressions_1.append(y_val)

    # SCENARIO 2: Length is CONSTANT (Varying Weight & Depth)
    x_weights_g = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    y_depths_mm2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    depressions_2 = []

    for w_g, d_mm in zip(x_weights_g, y_depths_mm2):
        w = w_g * (10 ** -3)
        l = base_l * (10 ** -2)
        d = d_mm * (10 ** -1)
        y_val = (4 * w * (l ** 3)) / (Y * width_m * (d ** 3))
        depressions_2.append(y_val)

    # SCENARIO 3: Depth is CONSTANT (Varying Length & Weight)
    x_lengths_cm3 = [60, 65, 70, 75, 80, 85, 90, 95, 100, 100, 100]
    y_weights_g3 = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    depressions_3 = []

    for l_cm, w_g in zip(x_lengths_cm3, y_weights_g3):
        w = w_g * (10 ** -3)
        l = l_cm * (10 ** -2)
        d = base_d * (10 ** -1)
        y_val = (4 * w * (l ** 3)) / (Y * width_m * (d ** 3))
        depressions_3.append(y_val)

    # --- 4. TAB CONTROL SECTION (THE WEB NOTEBOOK) ---
    tab1, tab2, tab3 = st.tabs(["1. Weight Constant", "2. Length Constant", "3. Depth Constant"])

    # TAB 1: Graph 1 Display
    with tab1:
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        ax1.plot(x_lengths_cm, depressions_1, marker='o', color='royalblue', linewidth=2)
        ax1.set_title("Scenario 1: Weight Constant\n(Varying Length & Depth)", fontsize=10, fontweight='bold')
        ax1.set_xlabel("Length Step (cm)")
        ax1.set_ylabel("Depression (y)")
        ax1.grid(True, linestyle=':')
        st.pyplot(fig1)

    # TAB 2: Graph 2 Display
    with tab2:
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.plot(x_weights_g, depressions_2, marker='s', color='crimson', linewidth=2)
        ax2.set_title("Scenario 2: Length Constant\n(Varying Weight & Depth)", fontsize=10, fontweight='bold')
        ax2.set_xlabel("Weight Step (g)")
        ax2.set_ylabel("Depression (y)")
        ax2.grid(True, linestyle=':')
        st.pyplot(fig2)

    # TAB 3: Graph 3 Display
    with tab3:
        fig3, ax3 = plt.subplots(figsize=(8, 4))
        ax3.plot(y_weights_g3, depressions_3, marker='^', color='forestgreen', linewidth=2)
        ax3.set_title("Scenario 3: Depth Constant\n(Varying Length & Weight)", fontsize=10, fontweight='bold')
        ax3.set_xlabel("Weight Step (g)")
        ax3.set_ylabel("Depression (y)")
        ax3.grid(True, linestyle=':')
        st.pyplot(fig3)

    st.success("Status: All 3 graphs updated successfully!")

except Exception as e:
    st.error(f"Error processing metrics: {e}")
