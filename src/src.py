import tkinter as tk
import time
import customtkinter as ctk
root = ctk.CTk()
root.title("Workout Program")

sidebar = ctk.CTkFrame(root, width=200)
sidebar.pack(side="left", fill="y")

# add some function that shows stopwatch and shows exercises
ctk.CTkLabel(sidebar, text="RepNation", font=("Helvetica", 16)).pack(pady=10)
ctk.CTkButton(sidebar, text="Stopwatch", command=lambda: show_stopwatch(content_frame)).pack(fill="x")
ctk.CTkButton(sidebar, text="Exercises", command=lambda: show_exercises(content_frame)).pack(fill="x")

def show_exercises(frame):
    pass

def show_stopwatch(frame):
    pass

class Stopwatch:
    def __init__(self, root) -> None:
        self.running = False
        self.time = 0
        self.root = root
        self.label = ctk.CTkLabel(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = ctk.CTkButton(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = ctk.CTkButton(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = ctk.CTkButton(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def update_timer(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_timer)

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")

root.title("Stopwatch")

stopwatch = Stopwatch(root)

root.mainloop()

class Exercise:
    def __init__(self, name="None", sets=0, reps=0, muscle_group1="None", muscle_group2="None", summary='') -> None:
        self.name = name
        self.sets = sets
        self.reps = reps
        self.muscle_group1 = muscle_group1
        self.muscle_group2 = muscle_group2
        self.summary = summary

    # Getters for each instance variable
    def get_name(self):
        return self.name

    def get_sets(self):
        return self.sets

    def get_reps(self):
        return self.reps

    def get_muscle_group1(self):
        return self.muscle_group1

    def get_muscle_group2(self):
        return self.muscle_group2

    def get_summary(self):
        return self.summary

    # Setters for each instance variable
    def set_name(self, name):
        self.name = name

    def set_sets(self, sets):
        self.sets = sets

    def set_reps(self, reps):
        self.reps = reps

    def set_muscle_group1(self, muscle_group1):
        self.muscle_group1 = muscle_group1

    def set_muscle_group2(self, muscle_group2):
        self.muscle_group2 = muscle_group2

    def set_summary(self, summary):
        self.summary = summary


# Example of exercises, maybe we want to add a way to make your own..?
movements = []

bench_press = Exercise("Barbell Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Lie on a flat bench, grip the barbell, and press it from your chest to arms fully extended.")
movements.append(bench_press)

inc_bench_press = Exercise("Incline Barbell Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Lie on an incline bench, grip the barbell, and press it from your chest to arms fully extended.")
movements.append(inc_bench_press)

chest_press = Exercise("Chest Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Sit on a chest press machine and press the handles forward until arms are fully extended.")
movements.append(chest_press)

dumbbell_fly = Exercise("Dumbbell Fly", 0, 0, "Chest", "Front Deltoids", "Lie on a flat bench with dumbbells in hand, lower arms out to sides, then bring them together above your chest.")
movements.append(dumbbell_fly)

cable_fly = Exercise("Cable Fly", 0, 0, "Chest", "Front Deltoids", "Stand between cable machines, grab the handles, and pull them together in front of you while maintaining slightly bent arms.")
movements.append(cable_fly)

dips = Exercise("Dips", 0, 0, "Chest", "Triceps, Deltoids", "Grip parallel bars and lower your body until your arms are at 90 degrees, then push back up.")
movements.append(dips)

tricep_pushdown = Exercise("Tricep Pushdown", 0, 0, "Triceps", "", "Using a cable machine, grip the bar and push it down until your arms are fully extended.")
movements.append(tricep_pushdown)

skull_crusher = Exercise("Skull Crusher", 0, 0, "Triceps", "", "Lie on a bench with an EZ bar and lower it toward your forehead, then extend your arms to press the bar back up.")
movements.append(skull_crusher)

squat = Exercise("Barbell Squat", 0, 0, "Quads", "Glutes, Hamstrings", "Stand with feet shoulder-width apart, barbell on upper back, and lower yourself into a squat before standing back up.")
movements.append(squat)

deadlift = Exercise("Deadlift", 0, 0, "Back", "Hamstrings, Glutes", "Grip the barbell on the floor, hinge at the hips, and lift the bar while keeping your back straight.")
movements.append(deadlift)

romanian_deadlift = Exercise("Romanian Deadlift", 0, 0, "Hamstrings", "Glutes", "With a barbell, lower it by hinging at the hips while keeping your legs straight, then return to standing.")
movements.append(romanian_deadlift)

leg_press = Exercise("Leg Press", 0, 0, "Quads", "Glutes", "Sit on the leg press machine, place feet on the platform, and push it away by extending your legs.")
movements.append(leg_press)

lunges = Exercise("Lunges", 0, 0, "Quads", "Glutes, Hamstrings", "Step forward with one leg, lower your hips until both knees are at 90-degree angles, and push back up.")
movements.append(lunges)

calf_raise = Exercise("Calf Raise", 0, 0, "Calves", "", "Stand on a raised surface, lift your heels off the ground by contracting your calves, then lower them back down.")
movements.append(calf_raise)

lat_pull_down = Exercise("Lat Pull Down", 0, 0, "Back", "Biceps", "Sit at a lat pull-down machine, grip the bar, and pull it down to your chest while keeping your back straight.")
movements.append(lat_pull_down)

pull_up = Exercise("Pull Up", 0, 0, "Back", "Biceps", "Grip a pull-up bar with palms facing away and pull your body up until your chin is over the bar.")
movements.append(pull_up)

barbell_row = Exercise("Barbell Row", 0, 0, "Back", "Biceps", "Bend over with a barbell and row it to your lower chest, keeping your back straight.")
movements.append(barbell_row)

dumbbell_row = Exercise("Dumbbell Row", 0, 0, "Back", "Biceps", "Place one knee on a bench, grip a dumbbell with the other hand, and row it to your side while keeping your back straight.")
movements.append(dumbbell_row)

shoulder_press = Exercise("Shoulder Press", 0, 0, "Shoulders", "Triceps", "Grip a barbell or dumbbells at shoulder height and press them overhead until your arms are fully extended.")
movements.append(shoulder_press)

lateral_raise = Exercise("Lateral Raise", 0, 0, "Shoulders", "", "Stand with dumbbells at your sides and lift them out to the sides until your arms are parallel to the floor.")
movements.append(lateral_raise)

front_raise = Exercise("Front Raise", 0, 0, "Shoulders", "Front Deltoids", "Hold dumbbells in front of your thighs and raise them in front of you until your arms are parallel to the floor.")
movements.append(front_raise)

face_pull = Exercise("Face Pull", 0, 0, "Shoulders", "Rear Deltoids", "Using a cable machine with a rope attachment, pull the rope toward your face, keeping your elbows high.")
movements.append(face_pull)

bicep_curl = Exercise("Bicep Curl", 0, 0, "Biceps", "", "Stand with dumbbells or a barbell and curl the weights up to your shoulders while keeping your elbows stationary.")
movements.append(bicep_curl)

hammer_curl = Exercise("Hammer Curl", 0, 0, "Biceps", "Forearms", "Hold dumbbells with palms facing each other and curl them toward your shoulders.")
movements.append(hammer_curl)

preacher_curl = Exercise("Preacher Curl", 0, 0, "Biceps", "", "Sit at a preacher bench with an EZ bar and curl the bar toward your shoulders while keeping your upper arms on the pad.")
movements.append(preacher_curl)

plank = Exercise("Plank", 0, 0, "Core", "", "Hold a position with your forearms and toes on the ground, keeping your body straight and core engaged.")
movements.append(plank)

sit_up = Exercise("Sit-Up", 0, 0, "Core", "", "Lie on your back with knees bent, then sit up toward your knees and lower back down.")
movements.append(sit_up)

russian_twist = Exercise("Russian Twist", 0, 0, "Core", "Obliques", "Sit on the floor, lean back slightly, and twist your torso side to side while holding a weight or medicine ball.")
movements.append(russian_twist)

