import customtkinter as ctk
import json
import os

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
        workout is saved when it is created.

        :return:    None
        """
        self.create_workout_button.configure(state="disabled")
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
        Literally saves the workout. It saves it to the JSON file as a dictionary entry.
        It then refreshes the little create workout box upon finish.

        :return:    None
        """
        workout_name = self.name_entry.get()
        workout_description = self.description_entry.get()

        # Create a workout dictionary.
        new_workout = {
            "name": workout_name,
            "description": workout_description
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
        Clicking a workout will highlight it in piss yellow, allowing for the edit and delete options.

        :return:    None
        """
        # Clear any existing widgets
        for widget in self.workout_list_frame.winfo_children():
            widget.destroy()

        # Iterate through all workouts and display them
        for index, workout in enumerate(self.workouts):
            # Create a workout frame (the entire frame area is now clickable)
            workout_frame = ctk.CTkFrame(self.workout_list_frame, fg_color="lightblue", height=120, corner_radius=10)
            workout_frame.pack(fill="x", padx=10, pady=10)

            # Workout name and description
            workout_name_label = ctk.CTkLabel(workout_frame, text=workout['name'], font=("Helvetica", 24, "bold"), text_color="black", anchor="w")
            workout_name_label.pack(side="top", fill="x", padx=10, pady=5)

            workout_description_label = ctk.CTkLabel(workout_frame, text=workout['description'], font=("Helvetica", 16), text_color="black", anchor="w")
            workout_description_label.pack(side="top", fill="x", padx=10, pady=5)

            # Display exercises in this workout
            if 'exercises' in workout:
                exercises_label = ctk.CTkLabel(workout_frame, text="Exercises:", font=("Helvetica", 16, "italic"), text_color="black", anchor="w")
                exercises_label.pack(side="top", padx=10, pady=5, anchor="w")

                for exercise in workout['exercises']:
                    exercise_label = ctk.CTkLabel(workout_frame, 
                                                  text=f"- {exercise['name']}", 
                                                  font=("Helvetica", 14), anchor="w", text_color="black")
                    exercise_label.pack(side="top", padx=20, pady=0, anchor="w")

            #Highlight the box in pee yellow when clicked
            # there is sometimes a little delay in highlighting for some reason...
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
            prev_workout_frame.configure(fg_color="lightblue")

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
        Opens a new window to allow user to edit an already made workout.

        :return:    None
        """
        if self.highlighted_workout_index is not None:
            workout_to_edit = self.workouts[self.highlighted_workout_index]
            edit_window = ctk.CTkToplevel(self.root)
            edit_window.title("Edit Workout")
            edit_window.geometry("600x400")

            # Workout Details
            title_label = ctk.CTkLabel(edit_window, text="Workout Title:", font=("Helvetica", 20))
            title_label.pack(anchor="w", padx=20, pady=10)

            name_entry = ctk.CTkEntry(edit_window, placeholder_text="Edit workout name...")
            name_entry.insert(0, workout_to_edit['name'])
            name_entry.pack(fill="x", padx=20, pady=10)

            description_label = ctk.CTkLabel(edit_window, text="Workout Description:", font=("Helvetica", 20))
            description_label.pack(anchor="w", padx=20, pady=10)

            description_entry = ctk.CTkEntry(edit_window, placeholder_text="Edit workout description...")
            description_entry.insert(0, workout_to_edit['description'])
            description_entry.pack(fill="x", padx=20, pady=10)

            # Display Exercises in Workout
            exercises_label = ctk.CTkLabel(edit_window, text="Exercises:", font=("Helvetica", 20))
            exercises_label.pack(anchor="w", padx=20, pady=10)

            exercises_frame = ctk.CTkFrame(edit_window, fg_color="transparent")
            exercises_frame.pack(fill="both", padx=20, pady=10)

            if 'exercises' in workout_to_edit:
                for exercise in workout_to_edit['exercises']:
                    exercise_label = ctk.CTkLabel(exercises_frame, text=f"- {exercise['name']} ({exercise['primary_muscle']})",
                                                  font=("Helvetica", 16), anchor="w")
                    exercise_label.pack(anchor="w", padx=10, pady=5)

            # Save Changes Button
            def save_edits():
                """
                Saves the changes the user made to their workouts.
                """
                workout_to_edit['name'] = name_entry.get()
                workout_to_edit['description'] = description_entry.get()
                self.save_workouts()
                edit_window.destroy()
                self.display_workouts()

            save_button = ctk.CTkButton(edit_window, text="Save Changes", command=save_edits)
            save_button.pack(side="bottom", anchor="e", padx=20, pady=20)
