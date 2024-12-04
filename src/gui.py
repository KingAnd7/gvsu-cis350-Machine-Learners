import customtkinter as ctk
import tkinter as tk
from exercise import movements
from workout import Workout
from exercise_display import ExerciseDisplay
from stopwatch import Stopwatch
from instructions import Instructions
import time

root = ctk.CTk()
root.title("Rep Nation Workout Program")
ctk.set_default_color_theme("dark-blue")
root.geometry("1200x768")

sidebar = ctk.CTkFrame(root, width=300)
sidebar.pack(side="left", fill="y")

content_frame = ctk.CTkFrame(root)
content_frame.pack(side="left", fill="both", expand=True)

button_size = 100  # Width and height of buttons to make them more square

# Add some function that shows stopwatch and shows exercises
ctk.CTkLabel(sidebar, text="Rep Nation", font=("Helvetica", 16)).pack(pady=10)

# Adjust button size to make them larger and square
ctk.CTkButton(sidebar, text="Workout", command=lambda: show_workout(content_frame), width=button_size, height=button_size).pack(fill="x", pady=10)
ctk.CTkButton(sidebar, text="Stopwatch", command=lambda: show_stopwatch(content_frame), width=button_size, height=button_size).pack(fill="x", pady=10)
ctk.CTkButton(sidebar, text="Exercises", command=lambda: show_exercises(content_frame), width=button_size, height=button_size).pack(fill="x", pady=10)
ctk.CTkButton(sidebar, text="Instructions", command=lambda: show_instructions(content_frame), width=button_size, height=button_size).pack(fill="x", pady=10)

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
    instructions = Instructions(frame)  # This will use the Instructions class from instructions.py


def show_workout(frame) -> None:
    """
    Creates the WORKOUT page by initializing the Workout class.
    Clears widgets on start to prevent other pages junk from being seen.

    :param frame: The origin frame used to define the window creation.
    :return:      None
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

    :param frame: The frame to define how the page is to be made.
    :return:      None
    """
    for widget in frame.winfo_children():
        widget.destroy()
    exercise_display = ExerciseDisplay(frame)

show_start_screen()
