import customtkinter as ctk

class Workout:
    def __init__(self, root) -> None:
        """
        Initializer for WORKOUT class and page.

        :param root: the main window where this page can be navigated to.
        :return:     None
        """
        self.root = root

        # Stores workouts in a list
        self.workouts = []

        # Highlights whatever the user is selecting (creates a yellow highlight effect).
        self.highlighted_workout_index = None

        self.workout_list_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.workout_list_frame.pack(pady=20, fill="both", expand=True)

        self.button_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.button_frame.pack(side="bottom", anchor="w", padx=20, pady=30)

        # Create a workout button setting
        self.create_workout_button = ctk.CTkButton(self.button_frame,
                                                   text="Create Workout",
                                                   font=("Helvetica", 20),
                                                   command=self.show_create_workout_form,
                                                   width=250,
                                                   height=70)
        self.create_workout_button.pack(side="left")

        # Delete workout button
        self.delete_workout_button = ctk.CTkButton(self.button_frame,
                                                   text="Delete",
                                                   font=("Helvetica", 20),
                                                   command=self.delete_highlighted_workout,
                                                   width=250,
                                                   height=70,
                                                   state="disabled")
        self.delete_workout_button.pack(side="left", padx=20)

        # Edit workout button
        self.edit_workout_button = ctk.CTkButton(self.button_frame,
                                                 text="Edit",
                                                 font=("Helvetica", 20),
                                                 command=self.edit_highlighted_workout,
                                                 width=250,
                                                 height=70,
                                                 state="disabled")
        self.edit_workout_button.pack(side="left", padx=20)

        # Displays existing workouts
        self.display_workouts()

    def show_create_workout_form(self) -> None:
        """
        Function that creates the small text box to create a workout.

        :return: None
        """
        # Sets DELETE and EDIT options to be off
        self.create_workout_button.configure(state="disabled")

        # Creates the box for the user to enter something
        self.form_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.form_frame.pack(pady=30)

        name_label = ctk.CTkLabel(self.form_frame, text="Workout Name:", font=("Helvetica", 20))
        name_label.pack(pady=10)

        self.name_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Enter workout name...")
        self.name_entry.pack(pady=10)

        description_label = ctk.CTkLabel(self.form_frame, text="Workout Description:", font=("Helvetica", 20))
        description_label.pack(pady=10)

        self.description_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Enter a short description...")
        self.description_entry.pack(pady=10)

        save_button = ctk.CTkButton(self.form_frame, text="Save Workout", command=self.save_workout)
        save_button.pack(pady=15)

    def save_workout(self) -> None:
        """
        Literally saves the workout.

        :returns: None
        """

        # Gets the name and description the user enters.
        workout_name = self.name_entry.get()
        workout_description = self.description_entry.get()

        # Create a workout dictionary.
        new_workout = {
            "name": workout_name,
            "description": workout_description
        }

        self.workouts.append(new_workout)

        # Clear the form after saving (refreshes)
        for widget in self.form_frame.winfo_children():
            widget.destroy()
        self.form_frame.destroy()

        self.create_workout_button.configure(state="normal")

        self.display_workouts()

    def display_workouts(self):
        """
        Function to display the workouts created. It is usually called at the end of every
        other function to update the list of created workouts and display the right ones.

        :return: None
        """
        # Clear any existing widgets in the workout list frame
        for widget in self.workout_list_frame.winfo_children():
            widget.destroy()

        # Loop through each workout in the workouts list
        for index, workout in enumerate(self.workouts):
            # Create a frame for each workout with a light blue background
            workout_frame = ctk.CTkFrame(self.workout_list_frame, fg_color="lightblue", height=120, corner_radius=10)
            workout_frame.pack(fill="x", padx=10, pady=10)

            # Create label for the workout name (larger font, left-aligned)
            workout_name_label = ctk.CTkLabel(workout_frame, text=workout['name'], font=("Helvetica", 24, "bold"), text_color="black", anchor="w")
            workout_name_label.pack(side="top", fill="x", padx=10, pady=5)

            # Create label for the workout description (smaller font, left-aligned)
            workout_description_label = ctk.CTkLabel(workout_frame, text=workout['description'], font=("Helvetica", 16), text_color="black", anchor="w")
            workout_description_label.pack(side="top", fill="x", padx=10, pady=5)

            # Highlight the workout when clicked by properly capturing the `idx` and `workout_frame`
            workout_frame.bind("<Button-1>", lambda event, idx=index, frame=workout_frame: self.highlight_workout(event, idx, frame))

    def highlight_workout(self, event, idx, workout_frame) -> None:
        """
        Highlights the clicked workout by changing its background color to yellow.

        :param idx: the index of the workout being highlighted.
        :param workout_frame: Widget for highlighted workout.
        :return: None
        """
        for widget in self.workout_list_frame.winfo_children():
            widget.configure(fg_color="lightblue")

        # Highlight the clicked workout frame to yellow
        workout_frame.configure(fg_color="yellow") 

        self.highlighted_workout_index = idx

        # Enables the delete and edit buttons after highlighting a workout.
        self.delete_workout_button.configure(state="normal")
        self.edit_workout_button.configure(state="normal")

    def delete_highlighted_workout(self) -> None:
        """
        Function to delete a workout. This is what's called when the delete button is used

        :return: None
        """
        if self.highlighted_workout_index is not None:
            del self.workouts[self.highlighted_workout_index]
            self.highlighted_workout_index = None
            self.delete_workout_button.configure(state="disabled")
            self.edit_workout_button.configure(state="disabled")
            self.display_workouts()

    import customtkinter as ctk

class Workout:
    def __init__(self, root) -> None:
        """
        Initializer for WORKOUT class and page.

        :param root: the main window where this page can be navigated to.
        :return:     None
        """
        self.root = root

        # Stores workouts in a list
        self.workouts = []

        # Highlights whatever the user is selecting (creates a yellow highlight effect).
        self.highlighted_workout_index = None

        self.workout_list_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.workout_list_frame.pack(pady=20, fill="both", expand=True)

        self.button_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.button_frame.pack(side="bottom", anchor="w", padx=20, pady=30)

        # Create a workout button setting
        self.create_workout_button = ctk.CTkButton(self.button_frame,
                                                   text="Create Workout",
                                                   font=("Helvetica", 20),
                                                   command=self.show_create_workout_form,
                                                   width=250,
                                                   height=70)
        self.create_workout_button.pack(side="left")

        # Delete workout button
        self.delete_workout_button = ctk.CTkButton(self.button_frame,
                                                   text="Delete",
                                                   font=("Helvetica", 20),
                                                   command=self.delete_highlighted_workout,
                                                   width=250,
                                                   height=70,
                                                   state="disabled")
        self.delete_workout_button.pack(side="left", padx=20)

        # Edit workout button
        self.edit_workout_button = ctk.CTkButton(self.button_frame,
                                                 text="Edit",
                                                 font=("Helvetica", 20),
                                                 command=self.edit_highlighted_workout,
                                                 width=250,
                                                 height=70,
                                                 state="disabled")
        self.edit_workout_button.pack(side="left", padx=20)

        # Displays existing workouts
        self.display_workouts()

    def show_create_workout_form(self) -> None:
        """
        Function that creates the small text box to create a workout.

        :return: None
        """
        # Sets DELETE and EDIT options to be off
        self.create_workout_button.configure(state="disabled")

        # Creates the box for the user to enter something
        self.form_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.form_frame.pack(pady=30)

        name_label = ctk.CTkLabel(self.form_frame, text="Workout Name:", font=("Helvetica", 20))
        name_label.pack(pady=10)

        self.name_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Enter workout name...")
        self.name_entry.pack(pady=10)

        description_label = ctk.CTkLabel(self.form_frame, text="Workout Description:", font=("Helvetica", 20))
        description_label.pack(pady=10)

        self.description_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Enter a short description...")
        self.description_entry.pack(pady=10)

        save_button = ctk.CTkButton(self.form_frame, text="Save Workout", command=self.save_workout)
        save_button.pack(pady=15)

    def save_workout(self) -> None:
        """
        Literally saves the workout.

        :returns: None
        """

        # Gets the name and description the user enters.
        workout_name = self.name_entry.get()
        workout_description = self.description_entry.get()

        # Create a workout dictionary.
        new_workout = {
            "name": workout_name,
            "description": workout_description
        }

        self.workouts.append(new_workout)

        # Clear the form after saving (refreshes)
        for widget in self.form_frame.winfo_children():
            widget.destroy()
        self.form_frame.destroy()

        self.create_workout_button.configure(state="normal")

        self.display_workouts()

    def display_workouts(self):
        """
        Function to display the workouts created. It is usually called at the end of every
        other function to update the list of created workouts and display the right ones.

        :return: None
        """
        # Clear any existing widgets in the workout list frame
        for widget in self.workout_list_frame.winfo_children():
            widget.destroy()

        # Loop through each workout in the workouts list
        for index, workout in enumerate(self.workouts):
            # Create a frame for each workout with a light blue background
            workout_frame = ctk.CTkFrame(self.workout_list_frame, fg_color="lightblue", height=120, corner_radius=10)
            workout_frame.pack(fill="x", padx=10, pady=10)

            # Create label for the workout name (larger font, left-aligned)
            workout_name_label = ctk.CTkLabel(workout_frame, text=workout['name'], font=("Helvetica", 24, "bold"), text_color="black", anchor="w")
            workout_name_label.pack(side="top", fill="x", padx=10, pady=5)

            # Create label for the workout description (smaller font, left-aligned)
            workout_description_label = ctk.CTkLabel(workout_frame, text=workout['description'], font=("Helvetica", 16), text_color="black", anchor="w")
            workout_description_label.pack(side="top", fill="x", padx=10, pady=5)

            # Highlight the workout when clicked by properly capturing the `idx` and `workout_frame`
            workout_frame.bind("<Button-1>", lambda event, idx=index, frame=workout_frame: self.highlight_workout(event, idx, frame))

    def highlight_workout(self, event, idx, workout_frame) -> None:
        """
        Highlights the clicked workout by changing its background color to yellow.

        :param idx: the index of the workout being highlighted.
        :param workout_frame: Widget for highlighted workout.
        :return: None
        """
        for widget in self.workout_list_frame.winfo_children():
            widget.configure(fg_color="lightblue")

        # Highlight the clicked workout frame to yellow
        workout_frame.configure(fg_color="yellow") 

        self.highlighted_workout_index = idx

        # Enables the delete and edit buttons after highlighting a workout.
        self.delete_workout_button.configure(state="normal")
        self.edit_workout_button.configure(state="normal")

    def delete_highlighted_workout(self) -> None:
        """
        Function to delete a workout. This is what's called when the delete button is used

        :return: None
        """
        if self.highlighted_workout_index is not None:
            del self.workouts[self.highlighted_workout_index]
            self.highlighted_workout_index = None
            self.delete_workout_button.configure(state="disabled")
            self.edit_workout_button.configure(state="disabled")
            self.display_workouts()

    def edit_highlighted_workout(self) -> None:
        """
        Function to allow editing of the highlighted workout's name and description.
        This opens a new window with text fields to edit the workout details.
        
        :return: None
        """
        if self.highlighted_workout_index is not None:
            # Get the workout to edit
            workout_to_edit = self.workouts[self.highlighted_workout_index]

            # Create the edit window
            edit_window = ctk.CTkToplevel(self.root)
            edit_window.title("Edit Workout")
            edit_window.geometry("400x300")

            # Title Label for Workout Name
            title_label = ctk.CTkLabel(edit_window, text="Workout Title:", font=("Helvetica", 20))
            title_label.pack(anchor="w", padx=20, pady=10)

            # Entry field for the workout name
            name_entry = ctk.CTkEntry(edit_window, placeholder_text="Edit workout name...")
            name_entry.insert(0, workout_to_edit['name'])  # Insert current workout name
            name_entry.pack(fill="x", padx=20, pady=10)

            # Description Label for Workout Description
            description_label = ctk.CTkLabel(edit_window, text="Workout Description:", font=("Helvetica", 20))
            description_label.pack(anchor="w", padx=20, pady=10)

            # Entry field for the workout description
            description_entry = ctk.CTkEntry(edit_window, placeholder_text="Edit workout description...")
            description_entry.insert(0, workout_to_edit['description'])  # Insert current workout description
            description_entry.pack(fill="x", padx=20, pady=10)

            # Create a frame for the button at the bottom of the window
            button_frame = ctk.CTkFrame(edit_window, fg_color="transparent")
            button_frame.pack(side="bottom", fill="x", padx=20, pady=10)

            # Save button, placed at the right side of the button_frame
            def save_edits():
                workout_to_edit['name'] = name_entry.get()
                workout_to_edit['description'] = description_entry.get()
                edit_window.destroy()
                self.display_workouts()

            save_button = ctk.CTkButton(button_frame, text="Save Changes", command=save_edits)
            save_button.pack(side="right")

