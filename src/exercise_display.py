from customtkinter import *
from exercise import movements
from tkinter import messagebox
from tkinter import Text
import customtkinter as ctk
import tkinter as tk
import os
import json

class ExerciseDisplay:
    """
    The ExerciseDisplay class creates and operates the EXERCISES page. This is where
    the user can search for exercises and add them to their workouts.
    """
    def __init__(self, parent_frame):
        """
        Initializer for the ExerciseDisplay Class.
        """
        self.parent_frame = parent_frame
        self.scrollable_frame = None
        self.create_search_bar()
        self.create_scrollable_frame()
        self.display_exercises(movements)

    def create_search_bar(self) -> None:
        """
        Creates the search bar for filtering exercises.

        :return:    None
        """
        search_frame = ctk.CTkFrame(self.parent_frame, fg_color="transparent")
        search_frame.pack(pady=10, fill="x")

        search_label = ctk.CTkLabel(search_frame, text="Search Exercises:", font=("Helvetica", 20))
        search_label.pack(side="left", padx=10)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter exercise keyword or muscle group...")
        self.search_entry.pack(side="left", padx=15, fill="x", expand=True)

        search_button = ctk.CTkButton(search_frame, text="Search", command=self.filter_exercises)
        search_button.pack(side="left", padx=10)

        # Makes enter key work instead of having to hit SEARCH.
        self.search_entry.bind("<Return>", lambda event: self.filter_exercises())

    def create_scrollable_frame(self) -> None:
        """
        Creates a scrollable frame to display filtered exercises.
        This is called multiple times in different functions to preserve the search
        bar.

        :return:    None
        """
        self.scrollable_frame = ctk.CTkScrollableFrame(self.parent_frame, width=100, height=600, fg_color="transparent")
        self.scrollable_frame.pack(fill="both", expand=True, padx=0, pady=10)

    def filter_exercises(self) -> None:
        """
        Filters the exercises based on the search term (name or muscle group).
        It is not case sensitive.

        :return:    None
        """
        search_term = self.search_entry.get()

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        filtered_exercises = []
        for exercise in movements:
            exercise_name = exercise.get_name().lower()
            muscle_group1 = exercise.get_muscle_group1().lower() if exercise.get_muscle_group1() else ""
            muscle_group2 = exercise.get_muscle_group2().lower() if exercise.get_muscle_group2() else ""

            if search_term.lower() in exercise_name or search_term.lower() in muscle_group1 or search_term.lower() in muscle_group2:
                filtered_exercises.append(exercise)

        self.display_exercises(filtered_exercises)

    def display_exercises(self, exercises) -> None:
        """
        Displays the exercises in the window. This is usually called at the end of most of the
        other functions in the ExerciseDisplay class.

        This also includes the 'add to workout' button, which the user clicks to add their
        chosen exercise to a workout.

        :param exercises:   List of exercises to display.
        :return:            None
        """
        # This loop creates the window.
        # It also adds a border color around the exercises to help differentiate them from each other.
        for exercise in exercises:
            exercise_frame = ctk.CTkFrame(self.scrollable_frame, 
                                          fg_color="gray14", 
                                          border_width=2,
                                          border_color="gray")
            exercise_frame.pack(pady=15, fill="x", anchor="w")

            # Name of the exercise (this will be at the top to make it more neat IMO).
            name_label = ctk.CTkLabel(exercise_frame, text=exercise.get_name(), font=("Helvetica", 25), anchor="w")
            name_label.pack(side="top", padx=15, pady=5, anchor="w")

            # This prints the primary muscle group below the name in a smaller font.
            musclegroup1_label = ctk.CTkLabel(exercise_frame, text=f"Primary muscle group: {exercise.get_muscle_group1()}", font=("", 15), anchor="w")
            musclegroup1_label.pack(side="top", padx=15, pady=3, anchor="w") 

            # Secondary muscle group (if any)
            if exercise.get_muscle_group2():
                musclegroup2_label = ctk.CTkLabel(exercise_frame, text=f"Secondary muscle group: {exercise.get_muscle_group2()}", font=("", 15), anchor="w")
                musclegroup2_label.pack(side="top", padx=15, pady=3, anchor="w")

            # Equipment Info (if any) It is displayed in tiny italicized font.
            equipment = exercise.get_equipment_required()
            if equipment and equipment != "None": 
                equipment_label = ctk.CTkLabel(exercise_frame, text=f"Equipment: {equipment}", font=("", 12, "italic"), anchor="w")
                equipment_label.pack(side="top", padx=15, pady=3, anchor="w")
            else:
                equipment_label = ctk.CTkLabel(exercise_frame, text="No equipment required", font=("", 12, "italic"), anchor="w")
                equipment_label.pack(side="top", padx=15, pady=3, anchor="w")

            # Adds view button for the open_exercise_window function.
            button_frame = ctk.CTkFrame(exercise_frame, fg_color="transparent")
            button_frame.pack(side="bottom", fill="x", padx=15, pady=10)

            # Moves the button to be near the bottom left of each exercise box.
            view_button = ctk.CTkButton(button_frame, text="View", command=lambda ex=exercise: self.open_exercise_window(ex))
            view_button.pack(side="right", padx=10)


            # Add a new button for adding to a workout
            add_to_workout_button = ctk.CTkButton(button_frame, text="Add to Workout", 
                                                  command=lambda ex=exercise: self.add_to_workout(ex))
            add_to_workout_button.pack(side="right", padx=10)

    def open_exercise_window(self, exercise) -> None:
        """
        Opens a window with more information when the 'view' button is clicked.
        This is where the user can see more information for each exercise.

        :param exercise:    The exercise to be viewed more.
        :return:            None
        """

        # Create a new window. The window name defaults to the name of the exercise.
        exercise_window = ctk.CTkToplevel(self.parent_frame)
        exercise_window.title(f"{exercise.get_name()}")
        exercise_window.geometry("850x600")

        # Create Text widget for rich text formatting
        text_widget = Text(exercise_window, wrap='word', font=("Arial", 16), height=30, width=100)
        text_widget.pack(pady=20, padx=20)

        # Disable user editing
        text_widget.configure(state="normal")

        # Create tags for styling (e.g., bold, italic, headers)
        text_widget.tag_configure("header", font=("Arial", 20, "bold"))
        text_widget.tag_configure("subheader", font=("Arial", 18, "bold"))
        text_widget.tag_configure("normal", font=("Arial", 16))
        text_widget.tag_configure("italic", font=("Arial", 16, "italic"))

        # Insert content with formatting
        text_widget.insert("end", f"{exercise.get_name()}\n\n", "header")
        text_widget.insert("end", f"Primary Muscle Group: {exercise.get_muscle_group1()}\n", "normal")
        if exercise.get_muscle_group2():
            text_widget.insert("end", f"Secondary Muscle Group: {exercise.get_muscle_group2()}\n", "normal")
        text_widget.insert("end", "\n")

        text_widget.insert("end", "How to:\n", "subheader")
        text_widget.insert("end", f"{exercise.get_summary()}\n\n", "normal")

        equipment = exercise.get_equipment_required()
        if equipment and equipment != "None":
            text_widget.insert("end", "Required Equipment:\n", "subheader")
            text_widget.insert("end", f"- {equipment}\n", "italic")
        else:
            text_widget.insert("end", "No equipment required\n", "italic")

        # Disable the text widget to make it read-only
        text_widget.configure(state="disabled")

        # Add a close button at the bottom
        close_button = ctk.CTkButton(exercise_window, text="Close", command=exercise_window.destroy)
        close_button.pack(side="bottom", padx=15, pady=20)

    def add_to_workout(self, exercise) -> None:
        """
        Prompts the user to choose a workout and adds the selected exercise to it.
        A new window popup opens up upon the interaction.

        :param exercise:    The exercise to add to a workout.
        :return:            None
        """

        if os.path.exists("workouts.json"):
            with open("workouts.json", "r") as file:
                workouts = json.load(file)
        else:
            workouts = []

        if not workouts:
            messagebox.showinfo("No Workouts Found", "No workouts found. Please create a workout first. I bet you did not read the instructions. Idiot.")
            return

        # Create a popup window for selecting a workout
        popup = CTkToplevel()
        popup.title("Select Workout")
        popup.geometry("600x400")

        # Configure grid layout to stretch and adapt
        popup.grid_columnconfigure(0, weight=1)
        popup.grid_rowconfigure(0, weight=0)
        popup.grid_rowconfigure(1, weight=1)
        popup.grid_rowconfigure(2, weight=0)

        label = ctk.CTkLabel(popup, text="Choose a workout:", font=("Helvetica", 16))
        label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        workout_names = [workout['name'] for workout in workouts]
        selected_workout = ctk.StringVar(popup)
        selected_workout.set(workout_names[0])  # Default selection

        dropdown = tk.OptionMenu(
            popup, 
            selected_workout, 
            *workout_names
        )
        dropdown.config(
            font=("Helvetica", 24),  
            width=100                 
        )
        dropdown.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        def save_to_workout():
            """
            This function updates the .json file to also include the exercises the user added to their workout.
            """
            workout_name = selected_workout.get()
            for workout in workouts:
                if workout['name'] == workout_name:
                    if 'exercises' not in workout:
                        workout['exercises'] = []
                    workout['exercises'].append({
                        "name": exercise.get_name(),
                        "primary_muscle": exercise.get_muscle_group1(),
                        "secondary_muscle": exercise.get_muscle_group2(),
                        "equipment": exercise.get_equipment_required(),
                    })
                    break
            with open("workouts.json", "w") as file:
                json.dump(workouts, file, indent=4)
            popup.destroy()
            messagebox.showinfo("Success", f"{exercise.get_name()} added to {workout_name}.")

        save_button = ctk.CTkButton(popup, text="Add", command=save_to_workout)
        save_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        close_button = ctk.CTkButton(popup, text="Cancel", command=popup.destroy)
        close_button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
