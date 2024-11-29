import customtkinter as ctk
from exercise import movements

class ExerciseDisplay:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.scrollable_frame = None
        self.create_search_bar()
        self.create_scrollable_frame()
        self.display_exercises(movements)

    def create_search_bar(self):
        """
        Creates the search bar for filtering exercises.
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

    def create_scrollable_frame(self):
        """
        Creates a scrollable frame to display filtered exercises.
        """
        self.scrollable_frame = ctk.CTkScrollableFrame(self.parent_frame, width=100, height=600, fg_color="transparent")
        self.scrollable_frame.pack(fill="both", expand=True, padx=0, pady=10)

    def filter_exercises(self):
        """
        Filters the exercises based on the search term (name or muscle group).
        """
        search_term = self.search_entry.get()

        # Clear the previous displayed exercises
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        filtered_exercises = []
        for exercise in movements:
            # Looks for search term and filters results. It is case-insensitive.
            exercise_name = exercise.get_name().lower()
            muscle_group1 = exercise.get_muscle_group1().lower() if exercise.get_muscle_group1() else ""
            muscle_group2 = exercise.get_muscle_group2().lower() if exercise.get_muscle_group2() else ""

            # Check if the search term is in the exercise name or either muscle group
            if search_term.lower() in exercise_name or search_term.lower() in muscle_group1 or search_term.lower() in muscle_group2:
                filtered_exercises.append(exercise)

        self.display_exercises(filtered_exercises)

    def display_exercises(self, exercises):
        """
        Displays the exercises in the scrollable frame.
        :param exercises: List of exercises to display.
        """
        for exercise in exercises:
            exercise_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="gray14")
            exercise_frame.pack(pady=15, fill="x", anchor="w")  # anchor="w" aligns the frame to the left

            # Name of the exercise (this will be at the top)
            name_label = ctk.CTkLabel(exercise_frame, text=exercise.get_name(), font=("Helvetica", 25), anchor="w")
            name_label.pack(side="top", padx=15, pady=5, anchor="w")  # anchor="w" left-aligns the text

            # Primary muscle group
            musclegroup1_label = ctk.CTkLabel(exercise_frame, text=f"Primary muscle group: {exercise.get_muscle_group1()}", font=("", 15), anchor="w")
            musclegroup1_label.pack(side="top", padx=15, pady=3, anchor="w")  # anchor="w" left-aligns the text

            # Secondary muscle group (if any)
            if exercise.get_muscle_group2():
                musclegroup2_label = ctk.CTkLabel(exercise_frame, text=f"Secondary muscle group: {exercise.get_muscle_group2()}", font=("", 15), anchor="w")
                musclegroup2_label.pack(side="top", padx=15, pady=3, anchor="w")  # anchor="w" left-aligns the text
