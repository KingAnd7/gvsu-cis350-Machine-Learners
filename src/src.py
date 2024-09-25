import tkinter as tk

root = tk.Tk()
root.title("Workout Program")
label = tk.Label(root, text="This is a workout program")
label.pack()
root.mainloop()

class Exercise:
    def __init__(self, name="None", sets=0, reps=0, muscle_group1="None", muscle_group2="None", summary='') -> None:
        self.name = name
        self.sets = sets
        self.reps = reps
        self.muscle_group1 = muscle_group1
        self.muscle_group2 = muscle_group2
        self.summary = summary

# TO DO: Need to implement getters, setters for each instance variable

bench_press = Exercise("Barbell Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "")
inc_bench_press = Exercise("Incline Barbell Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "")
chest_press = Exercise("Chest Press", 0, 0, "Chest", "Triceps, Front Deltoids", "")
dumbbell_fly = Exercise("Dumbell Fly", 0, 0, "Chest", "Front Deltoids", "")
cable_fly = Exercise("Cable Fly", 0, 0, "Chest", "Front Deltoids", "")
dips = Exercise("Dips", 0, 0, "Chest", "Triceps, Deltoids", "")
tricep_pushdown = Exercise("Tricep Pushdown", muscle_group1="Triceps", summary='')
