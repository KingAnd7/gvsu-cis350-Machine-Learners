import tkinter as tk

root = tk.Tk()
root.title("Workout Program")
label = tk.Label(root, text="This is a workout program")
label.pack()
root.mainloop()

class Exercise:
    def __init__(self, name, sets, reps, muscle_group1, muscle_group2, summary) -> None:
        self.name
        self.sets
        self.reps
        self.muscle_group1
        self.muscle_group2
        self.summary

bench_press = Exercise("Bench Press", 0, 0, "Chest", "N/A", "Bench Press a bar")