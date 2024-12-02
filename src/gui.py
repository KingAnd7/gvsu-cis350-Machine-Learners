from exercise import movements
from workout import Workout
from exercise_display import ExerciseDisplay
import tkinter as tk
import time
import customtkinter as ctk

root = ctk.CTk()
root.title("Rep Nation Workout Program")
ctk.set_default_color_theme("dark-blue")
root.geometry("1200x768")

sidebar = ctk.CTkFrame(root, width=1000)
sidebar.pack(side="left", fill="y")

content_frame = ctk.CTkFrame(root)
content_frame.pack(side="left", fill="both", expand=True)

# add some function that shows stopwatch and shows exercises
ctk.CTkLabel(sidebar, text="Rep Nation", font=("Helvetica", 16)).pack(pady=10)
ctk.CTkButton(sidebar, text="Workout", command=lambda: show_workout(content_frame)).pack(fill="x")
ctk.CTkButton(sidebar, text="Stopwatch", command=lambda: show_stopwatch(content_frame)).pack(fill="x")
ctk.CTkButton(sidebar, text="Exercises", command=lambda: show_exercises(content_frame)).pack(fill="x")
ctk.CTkButton(sidebar, text="Instructions", command=lambda: show_instructions(content_frame)).pack(fill="x")

start_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
start_frame.pack(fill="both", expand=True)


def show_start_screen():
    start_label = ctk.CTkLabel(start_frame, text="Welcome to the Workout Program!", font=("Helvetica", 24), fg_color="transparent")
    start_label.pack(pady=20)

    proceed_button = ctk.CTkButton(start_frame, text="Proceed", command=proceed_to_main)
    proceed_button.pack(pady=10)


def proceed_to_main():
    start_frame.pack_forget()
    show_workout(content_frame)

def show_instructions(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    instructions = Instructions(frame)


def show_workout(frame):
    """
    Calls WORKOUT class from workout.py.
    """
    for widget in frame.winfo_children():
        widget.destroy()
    workout = Workout(frame)


def show_stopwatch(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    stopwatch = Stopwatch(frame)


def show_exercises(frame) -> None:
    """
    Creates the EXERCISES page by initializing the ExerciseDisplay class.
    Clears widgets on start to prevent remnants of other pages.
    :param frame: The parent frame from tkinter to define how the page is to be created.
    :return: None
    """
    # Gets rid of random remnants of other pages.
    for widget in frame.winfo_children():
        widget.destroy()

    # Create an instance of ExerciseDisplay class
    exercise_display = ExerciseDisplay(frame)
    
class Instructions:
    def __init__(self, root):
        self.label = ctk.CTkLabel(root, text = 'Instructions (more coming soon...)', fg_color = 'transparent')
        self.label.pack(pady=20)

class Stopwatch:
    def __init__(self, root) -> None:
        self.running = False
        self.time = 0
        self.root = root
        self.label = ctk.CTkLabel(root, text="00:00:00", font=("Helvetica", 48), fg_color="transparent")
        self.label.pack(pady=20)
        self.x = 0
        self.y = 0

        button_frame = ctk.CTkFrame(root, fg_color="transparent")
        button_frame.pack(pady=10)

        self.start_button = ctk.CTkButton(button_frame, text="Start", command=self.start)
        self.start_button.pack(side=ctk.LEFT, padx=10)

        self.stop_button = ctk.CTkButton(button_frame, text="Stop", command=self.stop)
        self.stop_button.pack(side=ctk.LEFT, padx=10)

        self.reset_button = ctk.CTkButton(button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=ctk.LEFT, padx=10)

        self.interval_button = ctk.CTkButton(button_frame, text="Interval", command=self.interval)
        self.interval_button.pack(side=ctk.LEFT, padx=10)

        self.interval_frame = ctk.CTkFrame(root, fg_color="gray14")
        self.interval_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        self.label1 = ctk.CTkLabel(root, text="interval timer")
        self.label1.pack(pady=20)

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
        self.label1.pack_forget()

    def interval(self):
        minutes, seconds = divmod(self.time, 60)
        hours, minutes = divmod(minutes, 60)
        if self.running:
            if self.y % 2 == 0:
                self.y = self.y % 2
                self.label1 = ctk.CTkLabel(self.interval_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Helvetica", 12), fg_color="transparent")
                self.label1.grid(row=self.x, column=self.y, padx=5, pady=5)
                self.y += 1
            else:
                self.label1 = ctk.CTkLabel(self.interval_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Helvetica", 12), fg_color="transparent")
                self.label1.grid(row=self.x, column=self.y, padx=5, pady=5)
                self.x += 1
                self.y += 1
        else:
            self.running = True
            self.update_timer()
            if self.y % 2 == 0:
                self.y = self.y % 2
                self.label1 = ctk.CTkLabel(self.interval_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Helvetica", 12), fg_color="transparent")
                self.label1.grid(row=self.x, column=self.y, padx=5, pady=5)
                self.y += 1
            else:
                self.label1 = ctk.CTkLabel(self.interval_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Helvetica", 12), fg_color="transparent")
                self.label1.grid(row=self.x, column=self.y, padx=5, pady=5)
                self.x += 1
                self.y += 1

show_start_screen()