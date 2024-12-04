import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox


class Stopwatch:
    def __init__(self, root) -> None:
        
        self.running = False
        self.time = 0
        self.root = root
        
        # Increase font size and adjust the label to take more space
        self.label = ctk.CTkLabel(root, text="00:00:00", font=("Helvetica", 200), fg_color="transparent")  # Increased font size
        self.label.pack(pady=50, expand=True)  # Use expand=True to allow the label to take more space

        self.x = 0
        self.y = 0
        self.lap_count = 1  # Initialize lap counter

        # Frame for the buttons at the bottom
        button_frame = ctk.CTkFrame(root, fg_color="transparent")
        button_frame.pack(side=tk.BOTTOM, pady=30, fill=tk.X)

        # Create bigger buttons with same size and spacing
        self.start_button = ctk.CTkButton(button_frame, text="Start", command=self.start, width=220, height=80)
        self.start_button.pack(side=ctk.LEFT, padx=15)

        self.stop_button = ctk.CTkButton(button_frame, text="Stop", command=self.stop, width=220, height=80)
        self.stop_button.pack(side=ctk.LEFT, padx=15)

        self.reset_button = ctk.CTkButton(button_frame, text="Reset", command=self.reset, width=220, height=80)
        self.reset_button.pack(side=ctk.LEFT, padx=15)

        self.lap_interval_button = ctk.CTkButton(button_frame, text="Lap Interval", command=self.interval, width=220, height=80)
        self.lap_interval_button.pack(side=ctk.LEFT, padx=15)

        self.true_interval_button = ctk.CTkButton(button_frame, text="True Interval", command=self.open_interval_window, width=220, height=80)
        self.true_interval_button.pack(side=ctk.LEFT, padx=15)

        # Interval frame for showing lap times (if necessary)
        self.interval_frame = ctk.CTkFrame(root, fg_color="gray14")
        self.interval_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Configure the column to expand with content
        self.interval_frame.grid_columnconfigure(0, weight=1)
        self.interval_frame.grid_columnconfigure(1, weight=1)
        self.interval_frame.grid_columnconfigure(2, weight=1)
        self.interval_frame.grid_columnconfigure(3, weight=1)
        self.interval_frame.grid_columnconfigure(4, weight=1)

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
        self.lap_count = 1  # Reset lap count
        self.label.configure(text="00:00:00")
        self.clear_laps()  # Clear displayed laps

    def interval(self):
        minutes, seconds = divmod(self.time, 60)
        hours, minutes = divmod(minutes, 60)

        # Set the text color to black for all laps
        text_color = "black"

        # Alternate background color (box color) between white and light blue
        if self.lap_count % 2 == 0:
            bg_color = "lightblue"
        else:
            bg_color = "white"

        # Set the font style to bold for even laps
        if self.lap_count % 2 == 0:
            font_style = ("Helvetica", 14, "bold")
        else:
            font_style = ("Helvetica", 14)

        # Create the lap label with alternating background colors and black text
        label = ctk.CTkLabel(self.interval_frame, 
                            text=f"Lap {self.lap_count}: {hours:02}:{minutes:02}:{seconds:02}",
                            font=font_style, 
                            text_color=text_color,  # Set text color to black
                            fg_color=bg_color)  # Set background color to white or light blue

        # Grid placement without unwanted gaps, starting from column=0 and row by row
        label.grid(row=self.x, column=self.y, padx=5, pady=5, sticky='ew', columnspan=1)

        # Before incrementing the lap count, check if we've hit a multiple of 55
        if self.lap_count % 55 == 0 and self.lap_count != 0:
            self.clear_laps()  # Clear all the lap labels
            self.lap_count += 1  # Start at the next lap after the multiple of 55
        else:
            # Increment lap count normally if not clearing
            self.lap_count += 1

        # Update positions: when we hit 5 laps in a row, start a new row
        self.y += 1
        if self.y == 5:  # You can change '5' to any number to control the number of laps per row
            self.x += 1
            self.y = 0  # Reset y when starting a new row




    def clear_laps(self):
        # Remove all lap labels
        for widget in self.interval_frame.winfo_children():
            widget.destroy()

        # Reset position for lap display
        self.x = 0
        self.y = 0

    def open_interval_window(self):
        # Create the window for user input (Work time, Rest time, Sets)
        self.interval_window = ctk.CTkToplevel(self.root)
        self.interval_window.title("True Interval Timer")
        
        # Set window size to 600x600 and center it
        width, height = 600, 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the center of the screen
        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)

        # Set the window geometry
        self.interval_window.geometry(f"{width}x{height}+{center_x}+{center_y}")
        
        # Set minimum size for the window
        self.interval_window.minsize(width, height)

        # Labels for input fields with larger font
        ctk.CTkLabel(self.interval_window, text="Work Time (seconds):", font=("Helvetica", 16)).pack(padx=20, pady=20)
        self.work_time_entry = ctk.CTkEntry(self.interval_window, font=("Helvetica", 16))
        self.work_time_entry.pack(padx=20, pady=20)

        ctk.CTkLabel(self.interval_window, text="Rest Time (seconds):", font=("Helvetica", 16)).pack(padx=20, pady=20)
        self.rest_time_entry = ctk.CTkEntry(self.interval_window, font=("Helvetica", 16))
        self.rest_time_entry.pack(padx=20, pady=20)

        ctk.CTkLabel(self.interval_window, text="Sets:", font=("Helvetica", 16)).pack(padx=20, pady=20)
        self.sets_entry = ctk.CTkEntry(self.interval_window, font=("Helvetica", 16))
        self.sets_entry.pack(padx=20, pady=20)

        # Buttons for controlling the timer
        self.start_interval_button = ctk.CTkButton(self.interval_window, text="Start", command=self.start_true_interval, width=180, height=60)
        self.start_interval_button.pack(padx=20, pady=20)

        self.close_interval_button = ctk.CTkButton(self.interval_window, text="Close", command=self.interval_window.destroy, width=180, height=60)
        self.close_interval_button.pack(padx=20, pady=20)

    def start_true_interval(self):
        # Get inputs for work time, rest time, and sets
        try:
            self.work_time = int(self.work_time_entry.get())
            self.rest_time = int(self.rest_time_entry.get())
            self.sets = int(self.sets_entry.get())
        except ValueError:
            # Show an error popup if the inputs are invalid
            self.show_error_popup()
            return  # Exit the method if invalid input is detected

        if self.sets > 0 and self.work_time > 0 and self.rest_time > 0:
            # Create a new window with the countdown timer and the current status
            self.timer_window = ctk.CTkToplevel(self.interval_window)
            self.timer_window.title("Interval Countdown")

            self.timer_label = ctk.CTkLabel(self.timer_window, text="00:00", font=("Helvetica", 150), fg_color="transparent")
            self.timer_label.pack(pady=100)

            self.status_label = ctk.CTkLabel(self.timer_window, text="WORK", font=("Helvetica", 90), fg_color="transparent")
            self.status_label.pack(pady=20)

            # Initialize interval variables
            self.interval_running = True
            self.current_set = 1  # Start from the first set
            self.is_work_phase = True  # Start with the work phase
            self.interval_time = self.work_time  # Start with the work phase
            self.update_interval_timer()

    def update_interval_timer(self):
        if self.interval_running:
            if self.interval_time > 0:
                self.interval_time -= 1
                minutes, seconds = divmod(self.interval_time, 60)
                self.timer_label.configure(text=f"{minutes:02}:{seconds:02}")
            else:
                # Switch between work and rest phases
                if self.is_work_phase:
                    self.status_label.configure(text="REST")
                    self.interval_time = self.rest_time
                else:
                    self.status_label.configure(text="WORK")
                    self.interval_time = self.work_time

                # Switch phase
                self.is_work_phase = not self.is_work_phase

                # If all sets are completed, show DONE and stop the timer
                if self.current_set >= self.sets:
                    self.status_label.configure(text="DONE")
                    self.interval_running = False
                    return

                # If one cycle of work-rest is completed, increment the set count
                if self.interval_time == 0:
                    self.current_set += 1

            # Call the update function again in 1 second
            self.timer_window.after(1000, self.update_interval_timer)

    def show_error_popup(self):
        # Create a system popup using messagebox
        messagebox.showerror("Input Error", "Please enter valid numbers for work time, rest time, and sets.")
