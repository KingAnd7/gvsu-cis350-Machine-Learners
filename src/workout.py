import customtkinter as ctk
import json
import os
import datetime

class Workout:
    """
    The Workout class controls the WORKOUT page in the program, where a user can
    create, edit, delete, and view their workouts they created.
    """
    def __init__(self, root) -> None:
        """
        Initializer for the WORKOUT class. Sets up the page format and
        loads any workouts saved on the workout.json file.

        :param root:    Defines how the window is to be made.
        :return:        None
        """
        self.root = root
        self.workouts = []
        self.highlighted_workout_index = None

        # Load saved workouts from .json file.
        self.load_workouts()

        # Scrollable frame for workouts list
        self.workout_list_frame = ctk.CTkScrollableFrame(self.root, fg_color="transparent")
        self.workout_list_frame.pack(pady=20, fill="both", expand=True)

        self.button_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.button_frame.pack(side="bottom", anchor="w", padx=20, pady=30)

        # Create a workout button
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

        # Display existing workouts
        self.display_workouts()

    def save_workouts(self):
        """
        Saves created workouts to the .json file called workouts.json. It is called
        usually after a user creates, edits, or deletes a workout.

        :return:    None
        """
        with open("workouts.json", "w") as file:
            json.dump(self.workouts, file, indent=4)

    def load_workouts(self) -> None:
        """
        Load the workouts list from a JSON file. If one does not exist, it is created
        instead automatically.

        :return:    None
        """
        if os.path.exists("workouts.json"):
            with open("workouts.json", "r") as file:
                self.workouts = json.load(file)
        else:
            self.workouts = []

    def show_create_workout_form(self) -> None:
        """
        Function that creates the small text box to create a workout. The new
        workout is saved when it is created. It also allows the user to select 
        days of the week for the workout.
        """
        self.create_workout_button.configure(state="disabled")
        
        # Create a new form frame
        self.form_frame = ctk.CTkFrame(self.root, fg_color="transparent", width=1000, height=1000)
        self.form_frame.pack(pady=0, anchor="center", padx=0)

        # Add a scrollable frame inside the form
        scrollable_form_frame = ctk.CTkScrollableFrame(self.form_frame, width=580, height=450)
        scrollable_form_frame.pack(padx=10, pady=10)

        # Workout Name
        name_label = ctk.CTkLabel(scrollable_form_frame, text="Workout Name:", font=("Helvetica", 20))
        name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.name_entry = ctk.CTkEntry(scrollable_form_frame, placeholder_text="Enter workout name...", width=400)
        self.name_entry.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        # Workout Description
        description_label = ctk.CTkLabel(scrollable_form_frame, text="Workout Description:", font=("Helvetica", 20))
        description_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.description_entry = ctk.CTkEntry(scrollable_form_frame, placeholder_text="Enter a short description...", width=400)
        self.description_entry.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        # Days Selection
        days_label = ctk.CTkLabel(scrollable_form_frame, text="Select Days of the Week:", font=("Helvetica", 20))
        days_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        # Create the days checkboxes
        self.days_var_create = {day: ctk.BooleanVar() for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
        days_frame_create = ctk.CTkFrame(scrollable_form_frame, fg_color="transparent")
        days_frame_create.grid(row=5, column=0, sticky="w", padx=10, pady=10)

        for idx, day in enumerate(self.days_var_create):
            checkbox = ctk.CTkCheckBox(days_frame_create, text=day, variable=self.days_var_create[day], font=("Helvetica", 16))
            checkbox.grid(row=idx, column=0, sticky="w", padx=10, pady=5)

        # Save Workout Button
        save_button = ctk.CTkButton(scrollable_form_frame, text="Save Workout", command=self.save_workout, width=250, height=40,
                                    font=("Helvetica", 18)
                                    )
        save_button.grid(row=6, column=0, sticky="w", padx=10, pady=15)

        # Add a 'Discard Changes' button to the form (size matching Save button, red with black text)
        discard_button = ctk.CTkButton(scrollable_form_frame, 
                                        text="Discard Changes", 
                                        command=lambda: self.discard_changes(self.form_frame),
                                        width=250, height=40, 
                                        fg_color="red", text_color="black", font=("Helvetica", 18))
        discard_button.grid(row=6, column=0, sticky="w", padx=300, pady=15)

    def discard_changes(self, edit_window) -> None:
        """
        Function that discards changes made to the workout and closes the edit window.
        Also reactivates the "Create Workout" button.
        
        :param edit_window: The window to be closed.
        :return: None
        """
        # Close the form and reset the UI to its previous state
        edit_window.destroy()

        # Reactivate the Create Workout button
        self.create_workout_button.configure(state="normal")



    def save_workout(self) -> None:
        """
        Literally saves the workout. It saves it to the JSON file as a dictionary entry.
        It then refreshes the little create workout box upon finish.

        :return:    None
        """
        workout_name = self.name_entry.get()
        workout_description = self.description_entry.get()

        # Get selected days
        selected_days = [day for day, var in self.days_var_create.items() if var.get()]

        # Create a workout dictionary.
        new_workout = {
            "name": workout_name,
            "description": workout_description,
            "days": selected_days  # Add selected days to the workout
        }

        # Saving the new workout.
        self.workouts.append(new_workout)
        self.save_workouts()

        # Clear the form after saving (refreshes)
        for widget in self.form_frame.winfo_children():
            widget.destroy()
        self.form_frame.destroy()

        self.create_workout_button.configure(state="normal")
        self.display_workouts()

    def display_workouts(self) -> None:
        """
        Function to display the workouts created. Each workout is created in a little blue box.
        Clicking a workout will highlight it in yellow, allowing for the edit and delete options.
        Additionally, it highlights workouts scheduled for today.
        :return:    None
        """
        # Get today's weekday name
        today = datetime.datetime.today().strftime('%A')  # Day name (e.g., Monday, Tuesday, etc.)

        # Clear any existing widgets
        for widget in self.workout_list_frame.winfo_children():
            widget.destroy()

        # Iterate through all workouts and display them
        for index, workout in enumerate(self.workouts):
            # Check if the workout is scheduled for today
            workout_days = workout.get('days', [])
            is_scheduled_for_today = today in workout_days

            # Set the border color to red if the workout is scheduled for today, otherwise no border color
            border_color = "red" if is_scheduled_for_today else None
            
            # Create a workout frame with the border color conditionally set to red
            workout_frame = ctk.CTkFrame(self.workout_list_frame, 
                                        fg_color="lightblue", 
                                        height=150, 
                                        corner_radius=10, 
                                        border_color=border_color,  # Set border color dynamically
                                        border_width=2 if border_color else 0)  # Apply border only if it's red
            workout_frame.pack(fill="x", padx=10, pady=10)

            # Add a label if this workout is scheduled for today
            if is_scheduled_for_today:
                scheduled_label = ctk.CTkLabel(workout_frame, 
                                            text="This Workout is scheduled for today!", 
                                            font=("Helvetica", 16, "bold"), 
                                            text_color="black",  # Make the text bold and black
                                            anchor="w")
                scheduled_label.pack(side="top", fill="x", padx=10, pady=5)

            # Workout name and description
            workout_name_label = ctk.CTkLabel(workout_frame, 
                                            text=workout['name'], 
                                            font=("Helvetica", 24, "bold"), 
                                            text_color="black", 
                                            anchor="w")
            workout_name_label.pack(side="top", fill="x", padx=10, pady=5)

            workout_description_label = ctk.CTkLabel(workout_frame, 
                                                    text=workout['description'], 
                                                    font=("Helvetica", 16), 
                                                    text_color="black", 
                                                    anchor="w")
            workout_description_label.pack(side="top", fill="x", padx=10, pady=5)

            # Display the days for this workout only if there are any
            if workout_days:  # Only show days if there are any selected
                days_label = ctk.CTkLabel(workout_frame, 
                                        text="Days: " + ", ".join(workout_days), 
                                        font=("Helvetica", 14), 
                                        text_color="black", 
                                        anchor="w")
                days_label.pack(side="top", fill="x", padx=10, pady=5)

            # Display exercises in this workout
            if 'exercises' in workout:
                exercises_label = ctk.CTkLabel(workout_frame, 
                                            text="Exercises:", 
                                            font=("Helvetica", 16, "italic"), 
                                            text_color="black", 
                                            anchor="w")
                exercises_label.pack(side="top", padx=10, pady=5, anchor="w")

                for exercise in workout['exercises']:
                    exercise_label = ctk.CTkLabel(workout_frame, 
                                                text=f"- {exercise['name']}", 
                                                font=("Helvetica", 14), 
                                                anchor="w", 
                                                text_color="black")
                    exercise_label.pack(side="top", padx=20, pady=5, anchor="w")

            # Highlight the box in yellow when clicked
            workout_frame.bind("<Button-1>", lambda event, idx=index, frame=workout_frame: self.highlight_workout(event, idx, frame))

    def highlight_workout(self, event, idx, workout_frame) -> None:
        """
        Highlights a selected workout box in yellow color.
        Enables the edit and delete button as well.

        :param event:           The click event.
        :param idx:             The index of the workout in the workout list.
        :param workout_frame:   The frame box of the workout.
        :return:                None
        """
        # If there was a previously highlighted workout, reset its color
        if self.highlighted_workout_index is not None:
            prev_workout_frame = self.workout_list_frame.winfo_children()[self.highlighted_workout_index]
            prev_workout_frame.configure(fg_color="lightblue")  # Reset to default color

        # Highlight the selected workout in yellow
        workout_frame.configure(fg_color="yellow")

        # Set the selected workout index
        self.highlighted_workout_index = idx
        self.delete_workout_button.configure(state="normal")
        self.edit_workout_button.configure(state="normal")



    def delete_highlighted_workout(self) -> None:
        """
        Enables the option to delete the highlighted workout.
        Updates the .json file and refreshes the display.

        :return:    None
        """
        if self.highlighted_workout_index is not None:
            del self.workouts[self.highlighted_workout_index]
            self.highlighted_workout_index = None
            self.delete_workout_button.configure(state="disabled")
            self.edit_workout_button.configure(state="disabled")
            self.save_workouts()
            self.display_workouts()


    def edit_highlighted_workout(self) -> None:
        """
        Opens a new window to allow the user to edit an already created workout.
        This includes adding sets and reps to each exercise and modifying days.
        """
        if self.highlighted_workout_index is not None:
            workout_to_edit = self.workouts[self.highlighted_workout_index]
            edit_window = ctk.CTkToplevel(self.root)
            edit_window.title("Edit Workout")
            edit_window.geometry("1024x800")
            edit_window.columnconfigure(0, weight=1)  # For dynamic resizing
            edit_window.columnconfigure(1, weight=1)
            edit_window.columnconfigure(2, weight=1)

            # Workout Details
            title_label = ctk.CTkLabel(edit_window, text="Workout Title:", font=("Helvetica", 20))
            title_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

            name_entry = ctk.CTkEntry(edit_window, placeholder_text="Edit workout name...", width=300)
            name_entry.insert(0, workout_to_edit['name'])
            name_entry.grid(row=1, column=0, padx=20, pady=10, columnspan=3, sticky="w")

            description_label = ctk.CTkLabel(edit_window, text="Workout Description:", font=("Helvetica", 20))
            description_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

            description_entry = ctk.CTkEntry(edit_window, placeholder_text="Edit workout description...", width=500)
            description_entry.insert(0, workout_to_edit['description'])
            description_entry.grid(row=3, column=0, padx=20, pady=10, columnspan=3, sticky="w")

            # Add a header for "DAYS"
            days_header = ctk.CTkLabel(edit_window, text="DAYS", font=("Helvetica", 18, "bold"))
            days_header.grid(row=4, column=0, padx=20, pady=10, sticky="w")

            # Days selection (Checkboxes)
            self.days_var_edit = {day: ctk.BooleanVar() for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
            days_frame_edit = ctk.CTkFrame(edit_window, fg_color="transparent")
            days_frame_edit.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="w")

            # Create the checkboxes and left-align them
            for idx, day in enumerate(self.days_var_edit):
                checkbox = ctk.CTkCheckBox(days_frame_edit, text=day, variable=self.days_var_edit[day], font=("Helvetica", 16))
                checkbox.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

            # Pre-select days that were chosen earlier
            for day in workout_to_edit.get('days', []):
                if day in self.days_var_edit:
                    self.days_var_edit[day].set(True)

            # Headers for Sets and Reps
            headers_frame = ctk.CTkFrame(edit_window, fg_color="transparent")
            headers_frame.grid(row=6, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

            # Equalize column weights for header and entry boxes
            headers_frame.columnconfigure(0, weight=3)  # Exercise names
            headers_frame.columnconfigure(1, weight=1)  # Sets
            headers_frame.columnconfigure(2, weight=1)  # Reps

            # Exercise Header
            exercise_header = ctk.CTkLabel(headers_frame, text="EXERCISES", font=("Helvetica", 16, "bold"), anchor="w")
            exercise_header.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            # Sets Header
            sets_header = ctk.CTkLabel(headers_frame, text="SETS", font=("Helvetica", 16, "bold"), anchor="center")
            sets_header.grid(row=0, column=1, padx=0, pady=5, sticky="ew")  # Sticky to make it stretch horizontally

            # Reps Header
            reps_header = ctk.CTkLabel(headers_frame, text="REPS", font=("Helvetica", 16, "bold"), anchor="center")
            reps_header.grid(row=0, column=2, padx=100, pady=5, sticky="ew")
            # Separator Line
            separator_frame = ctk.CTkFrame(headers_frame, fg_color="white", height=2)
            separator_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")


            # Frame for Exercises
            exercises_frame = ctk.CTkFrame(edit_window, fg_color="transparent")
            exercises_frame.grid(row=7, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

            # Matching column weights for exercise entries
            exercises_frame.columnconfigure(0, weight=3)  # Exercise names
            exercises_frame.columnconfigure(1, weight=1)  # Sets
            exercises_frame.columnconfigure(2, weight=1)  # Reps

            # List to store entries
            exercise_inputs = []

            if 'exercises' in workout_to_edit:
                for idx, exercise in enumerate(workout_to_edit['exercises'], start=2):  # Adjust row index to align below headers
                    # Exercise Name
                    exercise_name_label = ctk.CTkLabel(
                        exercises_frame,
                        text=exercise['name'],
                        font=("Helvetica", 16),
                        anchor="w"
                    )
                    exercise_name_label.grid(row=idx * 2, column=0, padx=10, pady=5, sticky="w")

                    # Entry box for sets
                    sets_entry = ctk.CTkEntry(exercises_frame, placeholder_text="Sets", font=("Helvetica", 14))
                    sets_entry.insert(0, exercise.get('sets', ''))  # Default to current sets if available
                    sets_entry.grid(row=idx * 2, column=1, padx=10, pady=5, sticky="ew")  # Sticky ensures full-width alignment

                    # Entry box for reps
                    reps_entry = ctk.CTkEntry(exercises_frame, placeholder_text="Reps", font=("Helvetica", 14))
                    reps_entry.insert(0, exercise.get('reps', ''))  # Default to current reps if available
                    reps_entry.grid(row=idx * 2, column=2, padx=10, pady=5, sticky="ew")  # Sticky ensures full-width alignment

                    # Add a separator line below each exercise
                    line = ctk.CTkFrame(exercises_frame, fg_color="white", height=1)
                    line.grid(row=(idx * 2) + 1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

                    # Store input fields
                    exercise_inputs.append({
                        'exercise': exercise,
                        'sets_entry': sets_entry,
                        'reps_entry': reps_entry
                    })

            # Save Changes Button
            def save_edits():
                """
                Saves the changes the user made to their workouts.
                """
                # Update the selected days
                selected_days = [day for day, var in self.days_var_edit.items() if var.get()]
                workout_to_edit['days'] = selected_days

                # Update each exercise with new sets and reps values
                for input_data in exercise_inputs:
                    exercise = input_data['exercise']
                    sets_value = input_data['sets_entry'].get()
                    reps_value = input_data['reps_entry'].get()

                    # If sets or reps are entered, update them
                    if sets_value:
                        exercise['sets'] = sets_value
                    if reps_value:
                        exercise['reps'] = reps_value

                # Save the updated workout
                workout_to_edit['name'] = name_entry.get()
                workout_to_edit['description'] = description_entry.get()
                self.save_workouts()
                edit_window.destroy()
                self.display_workouts()

            save_button = ctk.CTkButton(edit_window, text="Save Changes", command=save_edits)
            save_button.grid(row=8, column=0, columnspan=3, padx=20, pady=20, sticky="e")
        
