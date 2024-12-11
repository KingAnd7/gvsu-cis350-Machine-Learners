# The Machine Learners

A cool, very on fleek, dapper exercise desktop program. The exercise program will assist any potential users in maximizing their workout routine. They will be able to utilize the program in order to create the best and most efficient workout routine. They will have access to use a timer to keep track of their time spent working out. Users will also be able to find exercises that they can perform in order to achieve their ideal body physique. If they do not know how to perform an exercise, a tutorial will be provided for them. If multiple users ever wanted to use the program with multiple 'profiles', where settings will be saved for separate profiles. Using our program, the most skinniest person can turn themselves into the most jacked human being ever, making someone like Sam Sulek and Chris Bumstead jealous of your new body.

## Team Members and Roles

* [Andrew Hills](https://github.com/KingAnd7/CIS350-HW2-Hills) (Leader, coder, project developer, amateur weightlifter)
* [Preston Thomas](https://github.com/preston-thomas/CIS350-HW2-Thomas) (Project manager, coder, project developer, professional weightlifter, documenter proof-reader)
* [Chai Callow](https://github.com/callchai/CIS350-HW2-Callow) (Documenter, coder, project developer)

## Run Instructions

#### 1. Install the latest version of Python.
   - Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Download the appropriate installer for your operating system (Windows, MacOS).
   - Run the installer and ensure that the "Add Python to PATH" option is selected during installation.
   - Verify the installation by opening a terminal and typing `python3 --version` or `python --version`.

#### 2. Make sure you have `tkinter` and `customtkinter` installed.
   - `tkinter`:
     - For most systems, `tkinter` comes pre-installed with Python. Verify by running `python3 -m tkinter` in the terminal. If a window appears, `tkinter` is installed.
     - If not installed, follow the appropriate steps for your system:
       - **MacOS**: Ensure you have the latest version of Python from python.org.
         - For newer MacBooks, you can use [Homebrew](https://brew.sh/) to install Python by running:
         ```bash
         brew install python
         ```
       - **Windows**: Reinstall Python and ensure `tkinter` is included.
   - `customtkinter`:
     - Install via pip by running `pip install customtkinter`.
       - If on Mac, try `brew install customtkinter`.
   - **Note for installation:**
     - If you are getting messages saying something called `pip` is not installed on a Mac system, try installing it in the terminal using:
      ```bash
      brew install pip
      ```
      - Or try:
        ```bash
        python -m ensurepip --upgrade
        ```

#### 3. Clone this repository.
   - Navigate to your terminal and type:
     ```bash
     git clone https://github.com/KingAnd7/gvsu-cis350-Machine-Learners/tree/main
     ```

#### 4. In your terminal, navigate to the `src` directory for the repository.
   - Use the `cd` command to navigate to the `src` folder. It is most likely in the `main` folder if you are cloning this for the first time. For example:
     ```bash
     cd gvsu-cis350-Machine-Learners/main/src
     ```

### 5. Run the program.
   - Type the following command in the terminal:
     ```bash
     python3 main.py
     ```
   - If `python3` is not recognized, you can try:
     ```bash
     python main.py
     ```
