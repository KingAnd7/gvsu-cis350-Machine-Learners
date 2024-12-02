from customtkinter import CTkTextbox
from exercise import movements
import customtkinter as ctk

class ExerciseDisplay:
    """
    The ExerciseDisplay class creates and operates the EXERCISES page.
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

            # Equipment Info (if any)
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

        # Left aligns the text because that looks the neatest.
        name_label = ctk.CTkLabel(exercise_window, text=f"Quick Summary for {exercise.get_name()}", font=("Helvetica", 30), anchor="w")
        name_label.pack(pady=10, padx=15, anchor="w")

        musclegroup1_label = ctk.CTkLabel(exercise_window, text=f"Primary Muscle Group: {exercise.get_muscle_group1()}", font=("", 20), anchor="w")
        musclegroup1_label.pack(pady=5, padx=15, anchor="w")

        if exercise.get_muscle_group2():
            musclegroup2_label = ctk.CTkLabel(exercise_window, text=f"Secondary Muscle Group: {exercise.get_muscle_group2()}", font=("", 20), anchor="w")
            musclegroup2_label.pack(pady=5, padx=15, anchor="w")

        # Add the summary title and summary from exercise.py
        summary_label = ctk.CTkLabel(exercise_window, text="How to:", font=("Helvetica", 25, "bold"), anchor="w")
        summary_label.pack(pady=10, padx=15, anchor="w")

        # Adds the literal summary from exercise.py. A little thing I did was make it wrap if the summary is too long.
        summary_text = exercise.get_summary()
        summary_text_label = ctk.CTkLabel(exercise_window, text=summary_text, font=("", 14), anchor="w", wraplength=750)
        summary_text_label.pack(padx=15, pady=10, anchor="w")

        # Equipment Info (if any)
        equipment = exercise.get_equipment_required()
        if equipment and equipment != "None":
            equipment_label = ctk.CTkLabel(exercise_window, text=f"Required Equipment:\n-{equipment}", font=("", 18, "italic"), anchor="e")
            equipment_label.pack(pady=5, padx=15, anchor="w")
        else:
            equipment_label = ctk.CTkLabel(exercise_window, text="No equipment required", font=("", 18, "italic"), anchor="w")
            equipment_label.pack(pady=5, padx=15, anchor="w")

        # Close button
        close_button = ctk.CTkButton(exercise_window, text="Close", command=exercise_window.destroy)
        close_button.pack(side="bottom", anchor="e", padx=15, pady=20)
