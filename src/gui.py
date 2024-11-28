from exercise import movements
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
    for widget in frame.winfo_children():
        widget.destroy()
    workout = Workout(frame)


def show_stopwatch(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    stopwatch = Stopwatch(frame)


def show_exercises(frame) -> None:
    """
    Creates the EXERCISES page. Works in conjunction with the filter_exercises and
    display_exercises functions to provide usability. Clears widgets on start (prevents a shitstorm!!)

    :param frame:  The parent frame from tkinter to define how page is to be created.
    :return:       None
    """
    # Gets rid of random remants of otehr pages.
    for widget in frame.winfo_children():
        widget.destroy()

    # Search bar makings.
    search_frame = ctk.CTkFrame(frame, fg_color="transparent")
    search_frame.pack(pady=10, fill="x")

    search_label = ctk.CTkLabel(search_frame, text="Search Exercises:", font=("Helvetica", 20))
    search_label.pack(side="left", padx=10)

    search_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter exercise keyword or muscle group...")
    search_entry.pack(side="left", padx=15, fill="x", expand=True)

    search_button = ctk.CTkButton(search_frame, text="Search", command=lambda: filter_exercises(search_entry.get(), scrollable_frame))
    search_button.pack(side="left", padx=10)

    # Makes enter key work instead of having to hit SEARCH.
    search_entry.bind("<Return>", lambda event: filter_exercises(search_entry.get(), scrollable_frame))

    # Keeps scroll bar there from go die die.
    global scrollable_frame
    scrollable_frame = ctk.CTkScrollableFrame(frame, width=100, height=600, fg_color="transparent")
    scrollable_frame.pack(fill="both", expand=True, padx=0, pady=10)

    # This is the start up, will show by default before query.
    display_exercises(movements, scrollable_frame)

def filter_exercises(search_term, scrollable_frame) -> None:
    """
    The filter_exercises function performs the filtering when using the SEARCH function/bar
    in the EXERCISES page. It first scans user input in the search bar, and scans the list
    of exercises and stores it in the list filtered_exercises. It then calls display_exercises
    solely with the filtered exercises.

    The search is NOT case sensitive, I hope.

    :param str search_term:  The filter/keyword being used to filter.
    :param scrollable_frame: The scrollable frame to be used to scroll if numerous exercises 
                                take up page.
    :returns:                None
    """
    # 'refreshes' when searching. (prevents the damned bar from disappearing)
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    filtered_exercises = []
    for exercise in movements:
        # Looks for search term and filters results. I think it is not case sensitive.
        if search_term.lower() in exercise.get_name().lower():
            filtered_exercises.append(exercise)
    
    # Displays after search.
    display_exercises(filtered_exercises, scrollable_frame)

def display_exercises(exercises, scrollable_frame) -> None:
    """
    The display_exercises function displays the exercises. It is called when
    user navigates to EXERCISE page for the first time, and every time the search bar is used.

    :param list exercises:      the list of exercises to display. On start, this defaults
                                    to the list of exercises from MOVEMENTS from the EXERCISE 
                                    class. After a query, it uses the list FILTERED_EXERCISES 
                                    from the filtered_exercises function.
    :param scrollable_frame:    Creates the scrollbar to use.
    :returns:                   None
    """
    for exercise in exercises:
        exercise_frame = ctk.CTkFrame(scrollable_frame, fg_color="gray14")
        exercise_frame.pack(pady=30, fill="x")
        
        name_label = ctk.CTkLabel(exercise_frame, text=exercise.get_name(), font=("Helvetica", 25))
        name_label.pack(side="left", padx=15)
        
        musclegroup1_label = ctk.CTkLabel(exercise_frame, text=f"Primary muscle group: {exercise.get_muscle_group1()}", font=("", 15))
        musclegroup1_label.pack(side="left", padx=20)
        
        if exercise.get_muscle_group2():
            musclegroup2_label = ctk.CTkLabel(exercise_frame, text=f"Secondary muscle group: {exercise.get_muscle_group2()}", font=("", 15))
            musclegroup2_label.pack(side="left", padx=5)

class Workout:
    def __init__(self, root):
        self.label = ctk.CTkLabel(root, text="Workout (more coming soon...)", fg_color="transparent")
        self.label.pack(pady=20)

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

    def interval(self):
        minutes, seconds = divmod(self.time, 60)
        hours, minutes = divmod(minutes, 60)
        if self.running:
            if self.y % 2 == 0:
                self.y = self.y % 2
                label1 = ctk.CTkLabel(self.interval_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Helvetica", 12), fg_color="transparent")
                label1.grid(row=self.x, column=self.y, padx=5, pady=5)
                self.y += 1
            else:
                label1 = ctk.CTkLabel(self.interval_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Helvetica", 12), fg_color="transparent")
                label1.grid(row=self.x, column=self.y, padx=5, pady=5)
                self.x += 1
                self.y += 1
        else:
            self.running = True
            self.update_timer()
            if self.y % 2 == 0:
                self.y = self.y % 2
                label1 = ctk.CTkLabel(self.interval_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Helvetica", 12), fg_color="transparent")
                label1.grid(row=self.x, column=self.y, padx=5, pady=5)
                self.y += 1
            else:
                label1 = ctk.CTkLabel(self.interval_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Helvetica", 12), fg_color="transparent")
                label1.grid(row=self.x, column=self.y, padx=5, pady=5)
                self.x += 1
                self.y += 1

show_start_screen()
