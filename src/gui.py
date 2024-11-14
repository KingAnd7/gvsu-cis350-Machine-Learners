from exercise import movements
import tkinter as tk
import time
import customtkinter as ctk

root = ctk.CTk()
root.title("Workout Program")
ctk.set_default_color_theme("dark-blue")
root.geometry("800x600")

sidebar = ctk.CTkFrame(root, width=200)
sidebar.pack(side="left", fill="y")

content_frame = ctk.CTkFrame(root)
content_frame.pack(side="left", fill="both", expand=True)

# add some function that shows stopwatch and shows exercises
ctk.CTkLabel(sidebar, text="Rep Nation", font=("Helvetica", 16)).pack(pady=10)
ctk.CTkButton(sidebar, text="Workout", command=lambda: show_workout(content_frame)).pack(fill="x")
ctk.CTkButton(sidebar, text="Stopwatch", command=lambda: show_stopwatch(content_frame)).pack(fill="x")
ctk.CTkButton(sidebar, text="Exercises", command=lambda: show_exercises(content_frame)).pack(fill="x")

start_frame = ctk.CTkFrame(content_frame)
start_frame.pack(fill="both", expand=True)


def show_start_screen():
    start_label = ctk.CTkLabel(start_frame, text="Welcome to the Workout Program!", font=("Helvetica", 24))
    start_label.pack(pady=20)

    proceed_button = ctk.CTkButton(start_frame, text="Proceed", command=proceed_to_main)
    proceed_button.pack(pady=10)


def proceed_to_main():
    start_frame.pack_forget()
    show_workout(content_frame)


def show_workout(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    workout = Workout(frame)


def show_stopwatch(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    stopwatch = Stopwatch(frame)


def show_exercises(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    scrollable_frame = ctk.CTkScrollableFrame(frame, width=600, height=600, fg_color="transparent")
    scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

    for exercise in movements:
        exercise_frame = ctk.CTkFrame(scrollable_frame, fg_color="blue")
        exercise_frame.pack(pady=5, fill="x")
        name_label = ctk.CTkLabel(exercise_frame, text=exercise.get_name(), font=("Helvetica", 16))
        name_label.pack(side="left", padx=10)
        summary_label = ctk.CTkLabel(exercise_frame, text=exercise.get_summary(), font=("", 12))
        summary_label.pack(side="left", padx=10)
        musclegroup1_label = ctk.CTkLabel(exercise_frame, text=f"Primary muscle group: {exercise.get_muscle_group1()}",
                                          font=("", 10))
        musclegroup1_label.pack(side="left", padx=10)
        if exercise.get_muscle_group2() != "":
            musclegroup2_label = ctk.CTkLabel(exercise_frame,
                                              text=f"Secondary muscle group: {exercise.get_muscle_group2()}",
                                              font=("", 10))
            musclegroup2_label.pack(side="left", padx=10)


class Workout:
    def __init__(self, root):
        self.label = ctk.CTkLabel(root, text="Technology", fg_color="transparent")
        self.label.pack(pady=20)


class Stopwatch:
    def __init__(self, root) -> None:
        self.running = False
        self.time = 0
        self.root = root
        self.label = ctk.CTkLabel(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        button_frame = ctk.CTkFrame(root)
        button_frame.pack(pady=10)

        self.start_button = ctk.CTkButton(button_frame, text="Start", command=self.start)
        self.start_button.pack(side=ctk.LEFT, padx=10)

        self.stop_button = ctk.CTkButton(button_frame, text="Stop", command=self.stop)
        self.stop_button.pack(side=ctk.LEFT, padx=10)

        self.reset_button = ctk.CTkButton(button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=ctk.LEFT, padx=10)

    def update_timer(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
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
        self.label.configure(text="00:00:00")


show_start_screen()
