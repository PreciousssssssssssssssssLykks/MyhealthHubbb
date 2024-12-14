import tkinter as tk
from tkinter import messagebox
from datetime import date

def save_data():
    user_name = entry_name.get()
    water_intake = entry_water.get()
    exercise_duration = entry_exercise.get()
    sleep_hours = entry_sleep.get()

    if not user_name or not water_intake or not exercise_duration or not sleep_hours:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    try:
        water_intake = int(water_intake)
    except ValueError:
        messagebox.showerror("Input Error", "Water intake must be a valid number.")
        return

    try:
        sleep_hours = float(sleep_hours)
    except ValueError:
        messagebox.showerror("Input Error", "Sleep hours must be a valid number.")
        return

    # Display saved data
    data = (
        f"Name: {user_name}\n"
        f"Water Intake: {water_intake} ml\n"
        f"Exercise Duration: {exercise_duration} minutes\n"
        f"Sleep Hours: {sleep_hours} hours\n"
        f"Date: {date.today()}"
    )

    # Recommendations
    recommendations = []
    if water_intake < 2000:
        recommendations.append("Your water intake is below the recommended 2000 ml. Consider drinking more water.")
    if sleep_hours < 8:
        recommendations.append("You slept less than the recommended 8 hours. Try to get more rest.")
    
    if not recommendations:
        recommendations.append("Great job! You are meeting the health recommendations.")

    messagebox.showinfo("Data Saved", data)
    messagebox.showinfo("Recommendations", "\n".join(recommendations))

# GUI setup
root = tk.Tk()
root.title("MyHealthHub - Health Tracker")
root.geometry("400x400")
root.config(bg="#F7F9F9")  # Light pastel background

# Header
header_label = tk.Label(root, text="MyHealthHub", font=("Helvetica", 24, "bold"), fg="#2C3E50", bg="#F7F9F9")
header_label.pack(pady=20)

# Labels and Entries
label_name = tk.Label(root, text="Enter your name:", font=("Helvetica", 12), fg="#2C3E50", bg="#F7F9F9")
label_name.pack(pady=5)
entry_name = tk.Entry(root, width=40, font=("Helvetica", 12), bd=1, relief="flat", highlightthickness=2, highlightbackground="#DCDCDC")
entry_name.pack(pady=5)

label_water = tk.Label(root, text="Water Intake (ml):", font=("Helvetica", 12), fg="#2C3E50", bg="#F7F9F9")
label_water.pack(pady=5)
entry_water = tk.Entry(root, width=40, font=("Helvetica", 12), bd=1, relief="flat", highlightthickness=2, highlightbackground="#DCDCDC")
entry_water.pack(pady=5)

label_exercise = tk.Label(root, text="Exercise Duration (minutes):", font=("Helvetica", 12), fg="#2C3E50", bg="#F7F9F9")
label_exercise.pack(pady=5)
entry_exercise = tk.Entry(root, width=40, font=("Helvetica", 12), bd=1, relief="flat", highlightthickness=2, highlightbackground="#DCDCDC")
entry_exercise.pack(pady=5)

label_sleep = tk.Label(root, text="Sleep Hours:", font=("Helvetica", 12), fg="#2C3E50", bg="#F7F9F9")
label_sleep.pack(pady=5)
entry_sleep = tk.Entry(root, width=40, font=("Helvetica", 12), bd=1, relief="flat", highlightthickness=2, highlightbackground="#DCDCDC")
entry_sleep.pack(pady=5)

# Save Button
save_button = tk.Button(root, text="Save Data", command=save_data, font=("Helvetica", 14), fg="white", bg="#3498DB", relief="flat", width=20)
save_button.pack(pady=20)

# Run the application
root.mainloop()
