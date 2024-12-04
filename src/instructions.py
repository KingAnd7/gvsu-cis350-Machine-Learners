import customtkinter as ctk
from tkinter import Text, Tk

class Instructions:
    def __init__(self, root):
        # Create Text widget for rich text formatting
        self.text = Text(root, wrap='word', height=100, width=120, font=("Arial", 16))
        self.text.pack(pady=20)
        
        # Disable user editing (we just want it to display)
        self.text.configure(state="disabled")

        # Create tags for styling (e.g., bold)
        self.text.tag_configure("bold", font=("Arial", 24, "bold"))
        self.text.tag_configure("header", font=("Arial", 18, "bold"))
        
        # Insert formatted content
        self.insert_instructions()

    def insert_instructions(self):
        # Enable the text widget for modification
        self.text.configure(state="normal")
        
        # Clear existing content
        self.text.delete(1.0, "end")

        # Insert content with tags (bold and headers)
        self.text.insert("end", "The purpose of this creation is to help you track workouts. It is technically unfinished, but here are a few rules on how to maximize your use of this program.\n\n", "bold")
        self.text.insert("end", "To begin, make sure you are doing this:\n", "bold")
        self.text.insert("end", "\t- Make sure you are in fullscreen mode.\n")
        self.text.insert("end", "\t- Expect bugs and glitches, and jank.\n")
        self.text.insert("end", "\n")

        # Insert section 1: WORKOUT page
        self.text.insert("end", "1. WORKOUT page.\n\n", "header")
        self.text.insert("end", "1.1 Intro:\n")
        self.text.insert("end", "The WORKOUT page is where you will probably spend most of your time. This is where you create, edit, and delete workout routines that you want to make. Workouts and their associated data are saved until deleted, even after ending the program.\n\n")

        # 1.2 Create Workout
        self.text.insert("end", "1.2 Create Workout:\n", "header")
        self.text.insert("end", "To create a workout, you must select \"Create Workout\". A menu will popup. You can fill in a name and a description for the workout. These can be changed later. Additionally, you will be able to select whatever day you want to schedule these workouts for.\n")
        self.text.insert("end", "For a scheduled workout, a message will appear for that workout if it is scheduled for that day. This can also be changed later.\n\n")

        # 1.3 Highlighting
        self.text.insert("end", "1.3 Highlighting:\n", "header")
        self.text.insert("end", "When a workout is made, a box appears on the workout screen. These boxes can be highlighted by clicking on them. They will be highlighted in yellow. A highlighted box is selected and the edit, view, and delete function can be used.\n\n")
        self.text.insert("end", "- Note:\n", "header")
        self.text.insert("end", "Highlighting can be inconsistent. There can be a delay when highlighting. This is due to tkinter and customtkinter's jankiness.\n\n")

        # 1.4 Edit
        self.text.insert("end", "1.4 Edit:\n", "header")
        self.text.insert("end", "The edit button allows you to make changes to your already created workout. Highlight a workout you made to edit it.\n")
        self.text.insert("end", "While in edit mode, you can edit the workout name, the work description, and the scheduled days.\n")
        self.text.insert("end", "Additionally, any exercise added can be deleted, OR you can change the number of sets or reps you want to perform.\n")
        self.text.insert("end", "Clicking 'Save changes' saves your changes. You may also discard them.\n\n")

        # 1.5 View
        self.text.insert("end", "1.5 View:\n", "header")
        self.text.insert("end", "The View mode is akin to a presentation mode. It will show your settings for a workout in a clean manner.\n\n")

        # 1.6 Delete
        self.text.insert("end", "1.6 Delete:\n", "header")
        self.text.insert("end", "When a workout is highlighted, you may have the option to delete it, removing it permanently. There is no confirmation.\n\n")

        # 2. STOPWATCH page
        self.text.insert("end", "2. STOPWATCH page.\n", "header")
        self.text.insert("end", "2.1 Intro:\n", "header")
        self.text.insert("end", "The Stopwatch page gives you a stopwatch timer and an interval timer to use.\n")
        self.text.insert("end", "\tNOTE: THE TIMER DOES NOT WORK IF YOU SWITCH TO A DIFFERENT PAGE\n\n")

        # 2.2 Stopwatch
        self.text.insert("end", "2.2 Stopwatch:\n", "header")
        self.text.insert("end", "The first thing on the stopwatch page shows you a clock and multiple widgets at the bottom. From left to right:\n")
        self.text.insert("end", "\tStart: Starts the timer.\n")
        self.text.insert("end", "\tStop: Stops the timer.\n")
        self.text.insert("end", "\tReset: Resets the timer back to 0, and clears laps.\n")
        self.text.insert("end", "\tLap Interval: When clicked, the current time and 'lap' is printed. It clears at 54 and starts again.\n")
        self.text.insert("end", "\tTrue Interval: When clicked, opens up a new window to use the 'True Interval'.\n\n")

        # 2.3 True Interval
        self.text.insert("end", "2.3 True Interval:\n", "header")
        self.text.insert("end", "The True Interval is the interval timer. When you click on the button, a new window opens asking you to enter information for work time, rest time, and sets. Entering numbers and pressing start opens up a new window with a timer that counts down to 0, starting from your work time.\n")
        self.text.insert("end", "A message of WORK or REST will display depending on the interval. DONE displays when there are no more sets left.\n\n")

        # 3. EXERCISE page
        self.text.insert("end", "3. EXERCISE page.\n\n", "header")
        self.text.insert("end", "3.1 Intro:\n", "header")
        self.text.insert("end", "The EXERCISE page allows you to search for predetermined exercises. Most are strength exercises.\n\n")

        # 3.2 Search bar
        self.text.insert("end", "3.2 Search bar:\n", "header")
        self.text.insert("end", "At the top of the EXERCISE page lies a search bar. This lets you search for potential exercises. You may search via exercise name or muscle group.\n")
        self.text.insert("end", "It is not case sensitive.\n")
        self.text.insert("end", "Pressing ENTER or clicking search filters your query.\n\n")

        # 3.3 'Add to Workout'
        self.text.insert("end", "3.3 'Add to Workout':\n", "header")
        self.text.insert("end", "When you find an exercise you like, there is an 'add to workout' button. Clicking this will open up a new window with a dropdown menu to add a workout to a created exercise.\n\n")

        # 3.4 'View'
        self.text.insert("end", "3.4 'View':\n", "header")
        self.text.insert("end", "View is another box within each workout. Clicking view shows more information, such as equipment, a summary, or muscle groups.\n\n")

        # 4. INSTRUCTIONS
        self.text.insert("end", "4. INSTRUCTIONS.\n", "header")
        self.text.insert("end", "4.1 Instructions:\n", "header")
        self.text.insert("end", "Shows you the instructions.\n")

        # Disable text widget to make it read-only
        self.text.configure(state="disabled")
