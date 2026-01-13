import tkinter as tk
import folium
import webbrowser
from pathlib import Path
import time

OUTPUT = Path("balloon_map.html").resolve()

def create_map():
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=10, width=600, height=400)

    # Optional: single marker
    folium.Marker([40.7128, -74.0060], popup="NYC").add_to(m)

    m.save(str(OUTPUT))

def open_map():
    create_map()
    # Cache-bust so you always see the newest file
    webbrowser.open_new_tab(OUTPUT.as_uri() + f"?v={int(time.time())}")

root = tk.Tk()
root.title("Weather Balloon Simulation")
root.geometry("300x150+100+100")
root.resizable(False, False)

tk.Label(root, text="Weather Balloon Simulation", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(root, text="Open Map", command=open_map, bg="lightblue", width=20).pack(pady=20)

root.mainloop()
