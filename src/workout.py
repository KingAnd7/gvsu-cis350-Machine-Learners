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

        button_width = 250
        button_height = 70

       # Create a workout button
        self.create_workout_button = ctk.CTkButton(self.button_frame,
                                                   text="Create Workout",
                                                   font=("Helvetica", 20),
                                                   command=self.show_create_workout_form,
                                                   width=button_width,
                                                   height=button_height)
        self.create_workout_button.pack(side="left")

        # View workout button
        self.view_workout_button = ctk.CTkButton(self.button_frame,
                                                text="View",
                                                font=("Helvetica", 20),
                                                command=self.view_highlighted_workout,
                                                width=button_width,
                                                height=button_height,
                                                state="disabled")
        self.view_workout_button.pack(side="left", padx=20)

        # Edit workout button
        self.edit_workout_button = ctk.CTkButton(self.button_frame,
                                                 text="Edit",
                                                 font=("Helvetica", 20),
                                                 command=self.edit_highlighted_workout,
                                                 width=button_width,
                                                 height=button_height,
                                                 state="disabled")
        self.edit_workout_button.pack(side="left", padx=20)

        # Delete workout button (styled in red with black text)
        self.delete_workout_button = ctk.CTkButton(self.button_frame,
                                                   text="Delete",
                                                   font=("Helvetica", 20, "bold"),
                                                   command=self.delete_highlighted_workout,
                                                   width=button_width,
                                                   height=button_height,
                                                   state="disabled",
                                                   fg_color="red",  # Red background
                                                   text_color="black")  # Black text
        self.delete_workout_button.pack(side="left", padx=20)

        # Display existing workouts
        self.display_workouts()


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
        today = datetime.datetime.today().strftime('%A')  # Day name

        for widget in self.workout_list_frame.winfo_children():
            widget.destroy()

        # Iterate through all workouts and display them
        for index, workout in enumerate(self.workouts):
            # Check if the workout is scheduled for today
            workout_days = workout.get('days', [])
            is_scheduled_for_today = today in workout_days

            # Set the border color to red if the workout is scheduled for today
            border_color = "red" if is_scheduled_for_today else None
            
            # Create a workout frame with the border color conditionally set to red
            workout_frame = ctk.CTkFrame(self.workout_list_frame, 
                                        fg_color="lightblue", 
                                        height=150, 
                                        corner_radius=10, 
                                        border_color=border_color,  
                                        border_width=2 if border_color else 0)
            workout_frame.pack(fill="x", padx=10, pady=10)

            # Add a label if this workout is scheduled for today
            if is_scheduled_for_today:
                scheduled_label = ctk.CTkLabel(workout_frame, 
                                            text="This Workout is scheduled for today!", 
                                            font=("Helvetica", 16, "bold"), 
                                            text_color="black",
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
            if workout_days:
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
        
        if self.highlighted_workout_index is not None:
            prev_workout_frame = self.workout_list_frame.winfo_children()[self.highlighted_workout_index]
            prev_workout_frame.configure(fg_color="lightblue")

        # Highlight the selected workout in yellow
        workout_frame.configure(fg_color="yellow")

        # Set the selected workout index
        self.highlighted_workout_index = idx
        self.delete_workout_button.configure(state="normal")
        self.edit_workout_button.configure(state="normal")
        self.view_workout_button.configure(state="normal")  # Enable the VIEW button



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
        if self.highlighted_workout_index is not None:
            workout_to_edit = self.workouts[self.highlighted_workout_index]

            # Create a new top-level window for editing
            edit_window = ctk.CTkToplevel(self.root)
            edit_window.title("Edit Workout")
            edit_window.geometry("1024x800")

            # Create a scrollable frame inside the window
            scrollable_frame = ctk.CTkScrollableFrame(edit_window)
            scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

            # Create a frame to hold form elements
            form_frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
            form_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Configure form_frame grid (make it stretch to fill window)
            form_frame.grid_rowconfigure(0, weight=0)
            form_frame.grid_rowconfigure(1, weight=1)
            form_frame.grid_rowconfigure(2, weight=0)
            form_frame.grid_rowconfigure(3, weight=1)
            form_frame.grid_rowconfigure(4, weight=0)
            form_frame.grid_rowconfigure(5, weight=1)
            form_frame.grid_columnconfigure(0, weight=1)
            form_frame.grid_columnconfigure(1, weight=1)
            form_frame.grid_columnconfigure(2, weight=1)

            # Workout Details
            title_label = ctk.CTkLabel(form_frame, text="Workout Title:", font=("Helvetica", 20))
            title_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

            name_entry = ctk.CTkEntry(form_frame, placeholder_text="Edit workout name...", width=300)
            name_entry.insert(0, workout_to_edit['name'])
            name_entry.grid(row=1, column=0, padx=20, pady=10, columnspan=3, sticky="ew")

            description_label = ctk.CTkLabel(form_frame, text="Workout Description:", font=("Helvetica", 20))
            description_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

            description_entry = ctk.CTkEntry(form_frame, placeholder_text="Edit workout description...", width=500)
            description_entry.insert(0, workout_to_edit['description'])
            description_entry.grid(row=3, column=0, padx=20, pady=10, columnspan=3, sticky="ew")

            days_header = ctk.CTkLabel(form_frame, text="DAYS", font=("Helvetica", 18, "bold"))
            days_header.grid(row=4, column=0, padx=20, pady=10, sticky="w")

            # Days selection (Checkboxes)
            self.days_var_edit = {day: ctk.BooleanVar() for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
            days_frame_edit = ctk.CTkFrame(form_frame, fg_color="transparent")
            days_frame_edit.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="w")

            for idx, day in enumerate(self.days_var_edit):
                checkbox = ctk.CTkCheckBox(days_frame_edit, text=day, variable=self.days_var_edit[day], font=("Helvetica", 16))
                checkbox.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

            for day in workout_to_edit.get('days', []):
                if day in self.days_var_edit:
                    self.days_var_edit[day].set(True)

            # Exercise Section (Headers)
            headers_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
            headers_frame.grid(row=6, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

            # Configure headers_frame grid (expand horizontally)
            headers_frame.grid_columnconfigure(0, weight=3)
            headers_frame.grid_columnconfigure(1, weight=1)
            headers_frame.grid_columnconfigure(2, weight=1)
            headers_frame.grid_columnconfigure(3, weight=0)  # For the delete button

            exercise_header = ctk.CTkLabel(headers_frame, text="EXERCISES", font=("Helvetica", 16, "bold"), anchor="w")
            exercise_header.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            sets_header = ctk.CTkLabel(headers_frame, text="SETS", font=("Helvetica", 16, "bold"), anchor="center")
            sets_header.grid(row=0, column=1, padx=100, pady=5, sticky="w")

            reps_header = ctk.CTkLabel(headers_frame, text="REPS", font=("Helvetica", 16, "bold"), anchor="center")
            reps_header.grid(row=0, column=2, padx=0, pady=5, sticky="w")

            separator_frame = ctk.CTkFrame(headers_frame, fg_color="white", height=2)
            separator_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

            # Exercise Inputs
            exercises_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
            exercises_frame.grid(row=7, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

            exercises_frame.grid_columnconfigure(0, weight=3)
            exercises_frame.grid_columnconfigure(1, weight=1)
            exercises_frame.grid_columnconfigure(2, weight=1)
            exercises_frame.grid_columnconfigure(3, weight=0)  # For the delete button

            exercise_inputs = []

            if 'exercises' in workout_to_edit:
                for idx, exercise in enumerate(workout_to_edit['exercises']):
                    # Exercise Name
                    exercise_name_label = ctk.CTkLabel(exercises_frame, text=exercise['name'], font=("Helvetica", 16), anchor="w")
                    exercise_name_label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

                    # Sets Entry
                    sets_entry = ctk.CTkEntry(exercises_frame, placeholder_text="Sets", font=("Helvetica", 14))
                    sets_entry.insert(0, exercise.get('sets', ''))
                    sets_entry.grid(row=idx, column=1, padx=10, pady=5, sticky="ew")

                    # Reps Entry
                    reps_entry = ctk.CTkEntry(exercises_frame, placeholder_text="Reps", font=("Helvetica", 14))
                    reps_entry.insert(0, exercise.get('reps', ''))
                    reps_entry.grid(row=idx, column=2, padx=10, pady=5, sticky="ew")

                    # Delete Button
                    delete_button = ctk.CTkButton(exercises_frame, text="Delete", fg_color="red", font=("Helvetica", 12),
                                                command=lambda idx=idx: self.delete_exercise(workout_to_edit, idx))
                    delete_button.grid(row=idx, column=3, padx=10, pady=5)

                    exercise_inputs.append({
                        'exercise': exercise,
                        'sets_entry': sets_entry,
                        'reps_entry': reps_entry
                    })


            def save_edits():
                """"
                Save button for edit window. Saves the changes the user makes.
                User can change the days, sets, and reps amount.
                """
                selected_days = [day for day, var in self.days_var_edit.items() if var.get()]
                workout_to_edit['days'] = selected_days

                for input_data in exercise_inputs:
                    exercise = input_data['exercise']
                    sets_value = input_data['sets_entry'].get()
                    reps_value = input_data['reps_entry'].get()
                    if sets_value:
                        exercise['sets'] = sets_value
                    if reps_value:
                        exercise['reps'] = reps_value

                workout_to_edit['name'] = name_entry.get()
                workout_to_edit['description'] = description_entry.get()
                self.save_workouts()
                edit_window.destroy()
                self.display_workouts()

            save_button = ctk.CTkButton(edit_window, text="Save Changes", command=save_edits, width=250, height=40)
            save_button.pack(pady=20, padx=20, fill="x")

            def discard_changes():
                edit_window.destroy()

            discard_button = ctk.CTkButton(edit_window, text="Discard Changes", command=discard_changes, width=250, height=40,
                                            fg_color="red", text_color="black")
            discard_button.pack(pady=10, padx=20, fill="x")


    def delete_exercise(self, workout_to_edit, idx):
        """
        Deletes an exercise from the workout's exercise list.

        :param workout_to_edit: The workout that is being edited.
        :param idx: The index of the exercise to delete.
        :return: None
        """
        # Remove the exercise from the list
        del workout_to_edit['exercises'][idx]

        # Update the workout data and save it
        self.save_workouts()

        # Refresh the display and UI
        self.display_workouts()

    def view_highlighted_workout(self) -> None:
        """
        Shows a neat chart with the workout details in a popup window.
        Displays the workout name, description, and exercises with their sets and reps.
        """
        if self.highlighted_workout_index is not None:
            workout_to_view = self.workouts[self.highlighted_workout_index]

            # Create a new top-level window for viewing workout details
            view_window = ctk.CTkToplevel(self.root)
            view_window.title("Workout Details")
            view_window.geometry("800x600")

            # Create a scrollable frame for the workout details
            scrollable_frame = ctk.CTkScrollableFrame(view_window)
            scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

            # Display the workout name in bold and large font
            workout_name_label = ctk.CTkLabel(scrollable_frame, 
                                            text=workout_to_view['name'], 
                                            font=("Helvetica", 30, "bold"), 
                                            text_color="black", anchor="w")
            workout_name_label.pack(fill="x", padx=10, pady=10)

            # Display the workout description
            workout_description_label = ctk.CTkLabel(scrollable_frame, 
                                                    text=workout_to_view['description'], 
                                                    font=("Helvetica", 20), 
                                                    text_color="black", anchor="w")
            workout_description_label.pack(fill="x", padx=10, pady=10)

            # Display the exercises section
            exercises_frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
            exercises_frame.pack(fill="both", padx=10, pady=20)

            if 'exercises' in workout_to_view:
                # Create a header for exercises
                exercises_header = ctk.CTkLabel(exercises_frame, 
                                                text="Exercises:", 
                                                font=("Helvetica", 24, "bold"), 
                                                text_color="black", anchor="w")
                exercises_header.pack(fill="x", padx=10, pady=10)

                # Loop through the exercises and display them in a neat chart-like format
                for exercise in workout_to_view['exercises']:
                    exercise_name = exercise.get('name', 'Unnamed Exercise')
                    sets = exercise.get('sets', 'N/A')
                    reps = exercise.get('reps', 'N/A')

                    # Create a row for each exercise
                    exercise_row = ctk.CTkFrame(exercises_frame, fg_color="transparent")
                    exercise_row.pack(fill="x", padx=10, pady=5)

                    # Exercise name
                    exercise_name_label = ctk.CTkLabel(exercise_row, text=exercise_name, font=("Helvetica", 18), anchor="w")
                    exercise_name_label.pack(side="left", padx=10)

                    # Sets and Reps
                    sets_label = ctk.CTkLabel(exercise_row, text=f"Sets: {sets}", font=("Helvetica", 16), anchor="w")
                    sets_label.pack(side="left", padx=10)

                    reps_label = ctk.CTkLabel(exercise_row, text=f"Reps: {reps}", font=("Helvetica", 16), anchor="w")
                    reps_label.pack(side="left", padx=10)

            # Add a 'Close' button to close the view window
            close_button = ctk.CTkButton(view_window, text="Close", command=view_window.destroy, width=250, height=40)
            close_button.pack(pady=20, padx=20, fill="x")
