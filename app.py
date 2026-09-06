import tkinter as tk
from tkinter import ttk  # Used to create the sliding graph tabs
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calculate_and_plot_all():
    try:
        # 1. Read single configuration values from input boxes
        base_w = float(entry_weight.get())
        base_l = float(entry_length.get())
        base_d = float(entry_depth.get())

        # Global Physics Constants
        Y = 70 * math.pow(10, 9)
        width_m = 3 * (10 ** -3)

        # ----------------------------------------------------
        # SCENARIO 1: Weight is CONSTANT (Varying Length & Depth)
        # ----------------------------------------------------
        x_lengths_cm = [60, 65, 70, 75, 80, 85, 90, 95, 100]
        y_depths_mm = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        depressions_1 = []

        # Calculate matching pairs loop
        for l_cm, d_mm in zip(x_lengths_cm, y_depths_mm):
            w = base_w * (10 ** -3)
            l = l_cm * (10 ** -2)
            d = d_mm * (10 ** -1)  # Matches your original scaling factor
            y_val = (4 * w * (l ** 3)) / (Y * width_m * (d ** 3))
            depressions_1.append(y_val)

        # ----------------------------------------------------
        # SCENARIO 2: Length is CONSTANT (Varying Weight & Depth)
        # ----------------------------------------------------
        x_weights_g = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        y_depths_mm2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]  # Pad list to match lengths
        depressions_2 = []

        for w_g, d_mm in zip(x_weights_g, y_depths_mm2):
            w = w_g * (10 ** -3)
            l = base_l * (10 ** -2)
            d = d_mm * (10 ** -1)
            y_val = (4 * w * (l ** 3)) / (Y * width_m * (d ** 3))
            depressions_2.append(y_val)

        # ----------------------------------------------------
        # SCENARIO 3: Depth is CONSTANT (Varying Length & Weight)
        # ----------------------------------------------------
        x_lengths_cm3 = [60, 65, 70, 75, 80, 85, 90, 95, 100, 100, 100]  # Pad list to match lengths
        y_weights_g3 = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        depressions_3 = []

        for l_cm, w_g in zip(x_lengths_cm3, y_weights_g3):
            w = w_g * (10 ** -3)
            l = l_cm * (10 ** -2)
            d = base_d * (10 ** -1)
            y_val = (4 * w * (l ** 3)) / (Y * width_m * (d ** 3))
            depressions_3.append(y_val)

        # ----------------------------------------------------
        # DRAWING & REDRAWING THE PLOTS
        # ----------------------------------------------------
        # Graph 1 Update
        ax1.clear()
        ax1.plot(x_lengths_cm, depressions_1, marker='o', color='royalblue', linewidth=2)
        ax1.set_title("Scenario 1: Weight Constant\n(Varying Length & Depth)", fontsize=10, fontweight='bold')
        ax1.set_xlabel("Length Step (cm)")
        ax1.set_ylabel("Depression (y)")
        ax1.grid(True, linestyle=':')

        # Graph 2 Update
        ax2.clear()
        ax2.plot(x_weights_g, depressions_2, marker='s', color='crimson', linewidth=2)
        ax2.set_title("Scenario 2: Length Constant\n(Varying Weight & Depth)", fontsize=10, fontweight='bold')
        ax2.set_xlabel("Weight Step (g)")
        ax2.set_ylabel("Depression (y)")
        ax2.grid(True, linestyle=':')

        # Graph 3 Update
        ax3.clear()
        ax3.plot(y_weights_g3, depressions_3, marker='^', color='forestgreen', linewidth=2)
        ax3.set_title("Scenario 3: Depth Constant\n(Varying Length & Weight)", fontsize=10, fontweight='bold')
        ax3.set_xlabel("Weight Step (g)")
        ax3.set_ylabel("Depression (y)")
        ax3.grid(True, linestyle=':')

        # Refresh all three screen displays
        canvas1.draw()
        canvas2.draw()
        canvas3.draw()
        label_status.config(text="Status: All 3 graphs updated successfully!", fg="green")

    except ValueError:
        label_status.config(text="Error: Enter valid numeric metrics!", fg="red")


# --- GUI WINDOW INITIALIZATION ---
root = tk.Tk()
root.title("Cantilever Multivariable Deflection Lab")
root.geometry("800x700")  # Sized larger for easy visibility
root.geometry("800x700")

# Input Control Dashboard Frame Panel
frame_controls = tk.Frame(root, padx=10, pady=10)
frame_controls.pack(side=tk.TOP, fill=tk.X)

# Grid Layout Setup for input fields
tk.Label(frame_controls, text="Base Weight (g):").grid(row=0, column=0, padx=5, sticky='w')
entry_weight = tk.Entry(frame_controls, width=8)
entry_weight.insert(0, "75")
entry_weight.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame_controls, text="Base Length (cm):").grid(row=0, column=2, padx=5, sticky='w')
entry_length = tk.Entry(frame_controls, width=8)
entry_length.insert(0, "80")
entry_length.grid(row=0, column=3, padx=5, pady=2)

tk.Label(frame_controls, text="Base Depth (mm):").grid(row=0, column=4, padx=5, sticky='w')
entry_depth = tk.Entry(frame_controls, width=8)
entry_depth.insert(0, "5")
entry_depth.grid(row=0, column=5, padx=5, pady=2)

btn_run = tk.Button(frame_controls, text="Update Graphs", command=calculate_and_plot_all, bg="#2196F3", fg="white",
                    font=('Arial', 9, 'bold'))
btn_run.grid(row=0, column=6, padx=15, ipadx=10)

label_status = tk.Label(frame_controls, text="Status: Ready", fg="gray")
label_status.grid(row=1, column=0, columnspan=7, pady=5)

# --- TAB CONTROL SECTION (THE NOTEBOOK) ---
notebook = ttk.Notebook(root)
notebook.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)

# Create 3 independent panel frames to hold our graphics containers
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)

notebook.add(tab1, text="1. Weight Constant")
notebook.add(tab2, text="2. Length Constant")
notebook.add(tab3, text="3. Depth Constant")

# --- INITIALIZE MATPLOTLIB SPACES FOR EACH TAB ---
fig1, ax1 = plt.subplots(figsize=(6, 4))
canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True)

fig2, ax2 = plt.subplots(figsize=(6, 4))
canvas2 = FigureCanvasTkAgg(fig2, master=tab2)
canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)

fig3, ax3 = plt.subplots(figsize=(6, 4))
canvas3 = FigureCanvasTkAgg(fig3, master=tab3)
canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Run calculation engine on boot up sequence to show lines immediately
calculate_and_plot_all()

root.mainloop()
