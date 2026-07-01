import tkinter as tk

# ---------------- Functions ---------------- #

def calculate():
    start = start_station.get()
    stop = stop_station.get()

    # Error checking
    if start == "" or stop == "":
        farelabel.config(text="Please select both stations!")
        return

    if start == stop:
        farelabel.config(text="Start and Stop cannot be the same!")
        return

    # Determine the metro lines
    if start in stn_sL:
        start_line = stn_sL
    else:
        start_line = stn_pL

    if stop in stn_sL:
        stop_line = stn_sL
    else:
        stop_line = stn_pL

    # Calculate number of stops
    if start_line is stop_line:
        n_stops = abs(start_line.index(start) - start_line.index(stop))
    else:
        n_stops = start_line.index(start) - start_line.index("WiByte")
        n_stops = abs(n_stops) + abs(stop_line.index("WiByte") - stop_line.index(stop))

    fare = n_stops * 20
    travel_time = n_stops * 2

    farelabel.config(
        text=f"Stops: {n_stops}\n"
             f"Time: {travel_time} mins\n"
             f"FARE = INR {fare}"
    )


def reset():
    start_station.set("")
    stop_station.set("")
    farelabel.config(text="FARE = ")


# ---------------- Window ---------------- #

window = tk.Tk()
window.title("Smrithi Metro Map")
window.geometry("600x600+10+0")
window.configure(bg="Darkgreen")

title = tk.Label(
    window,
    text="Welcome to Smrithi's Metro",
    font=("Helvetica",16,"bold"),
    bg="Darkgreen",
    fg="white"
)
title.pack()

# ---------------- Canvas ---------------- #

c = tk.Canvas(window, width=550, height=500)
c.pack()

# ---------------- Sprite Line ---------------- #

stn_sL = [
    "SpriteLand",
    "GoNGlide",
    "Costumes",
    "Broadcast",
    "WiByte",
    "Cloning",
    "MyBlocks"
]

x_s = 50
y_s = 200
d_stn = 70
r_stn = 6

for stn in stn_sL:
    if stn != stn_sL[-1]:
        c.create_line(x_s, y_s, x_s+d_stn, y_s,
                      fill="DarkOrange")

    c.create_oval(
        x_s-r_stn,
        y_s-r_stn,
        x_s+r_stn,
        y_s+r_stn,
        fill="DarkOrange"
    )

    c.create_text(
        x_s,
        y_s+30,
        text=stn,
        fill="DarkOrange",
        font=("Helvetica",6,"bold")
    )

    x_s += d_stn

# ---------------- Python Line ---------------- #

stn_pL = [
    "EscapeChar",
    "WhileLoop",
    "WiByte",
    "IfElifElse",
    "Range",
    "Dictionary",
    "TurtlePark"
]

x_s = 330
y_s = 40
d_stn = 70
r_stn = 6

for stn in stn_pL:
    if stn != stn_pL[-1]:
        c.create_line(
            x_s,
            y_s,
            x_s,
            y_s+d_stn,
            fill="blue"
        )

    c.create_oval(
        x_s-r_stn,
        y_s-r_stn,
        x_s+r_stn,
        y_s+r_stn,
        fill="blue"
    )

    c.create_text(
        x_s+40,
        y_s,
        text=stn,
        fill="blue",
        font=("Helvetica",6,"bold")
    )

    y_s += d_stn
# Get all stations except the interchange (avoid duplicate WiByte)
all_stations = stn_sL + stn_pL
all_stations.remove("WiByte")

c.create_text(30, 250, text="Start")
start_station = tk.StringVar()
drop_start = tk.OptionMenu(window, start_station, *all_stations)
drop_start.place(x=30, y=270)

c.create_text(240, 250, text="Stop")
stop_station = tk.StringVar()
drop_stop = tk.OptionMenu(window, stop_station, *all_stations)
drop_stop.place(x=240, y=270)

# ---------------- Buttons ---------------- #

button = tk.Button(
    window,
    text="Calculate Fare",
    command=calculate
)
button.pack()

reset_button = tk.Button(
    window,
    text="Reset",
    command=reset
)
reset_button.pack()

exit_button = tk.Button(
    window,
    text="Exit",
    command=window.destroy
)
exit_button.pack()

# ---------------- Fare Label ---------------- #

farelabel = tk.Label(
    window,
    text="FARE = ",
    font=("Helvetica", 12, "bold")
)
farelabel.pack()

window.mainloop()