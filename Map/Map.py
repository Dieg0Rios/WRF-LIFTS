import tkinter as tk
import folium
import random
import webbrowser

# --- Function to generate a test balloon path ---
def generate_path(start_lat=40.7128, start_lon=-74.0060, steps=10):
    """Generates a simple random walk path for the balloon"""
    path = [(start_lat, start_lon)]
    for _ in range(steps):
        start_lat += random.uniform(-0.01, 0.01)
        start_lon += random.uniform(-0.01, 0.01)
        path.append((start_lat, start_lon))
    return path

# --- Function to create and save the Folium map ---
def create_map(path):
    m = folium.Map(location=path[0], zoom_start=10, width=600, height=400)
    folium.PolyLine(path, color="blue", weight=3).add_to(m)
    folium.Marker(path[0], popup="Start").add_to(m)
    folium.Marker(path[-1], popup="End").add_to(m)
    m.save("balloon_path.html")

# --- Function triggered by the button ---
def run_simulation():
    path = generate_path()
    create_map(path)
    webbrowser.open("balloon_path.html")

# --- GUI setup ---
root = tk.Tk()
root.title("Weather Balloon Simulation")

# Set fixed window size and position
window_width = 300
window_height = 150
x_position = 100
y_position = 100
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(False, False)

# Title label
tk.Label(root, text="Weather Balloon Simulation", font=("Arial", 14, "bold")).pack(pady=10)

# Run Simulation button
tk.Button(root, text="Run Simulation", command=run_simulation, bg="lightblue", width=20).pack(pady=20)

root.mainloop()
