# todo.py 

Process Description :

Console-Based To-Do List Application (todo.py)

Objective : 

The objective of this project is to develop a simple command-line To-Do List Manager using Python. The application allows users to add, view, and remove tasks while storing them persistently in a text file.


🔄 Development Process :

1️
!!! Requirement Analysis :

First, the basic requirements of the application were identified :

Store tasks in a list Allow users to:

* Add tasks

* View tasks

* Remove tasks


Store tasks permanently using a text file

Display a menu-driven interface in the terminal


2️⃣ Program Design

The application was structured into modular functions for better readability and maintainability:

load_tasks() → Reads tasks from file

save_tasks() → Saves tasks to file

add_task() → Adds new task

view_tasks() → Displays all tasks

remove_task() → Deletes selected task

main() → Controls program flow


The program uses a while loop to continuously show the menu until the user chooses to exit.




3️⃣ File Handling Implementation

To make the application persistent:

A file named tasks.txt is created automatically.


**When the program starts:

It loads existing tasks from the file.


When tasks are added or removed:

The file is updated immediately.

This ensures that tasks remain saved even after closing the program.


4️⃣ Error Handling

Basic error handling was implemented to improve user experience:

FileNotFoundError handled when the file does not exist.

ValueError handled when the user enters invalid input.

Validation checks prevent removing non-existing tasks.


5️⃣ User Interaction Flow

@ Program starts.


@ Tasks are loaded from file.


@ Menu is displayed:

1.Add Task

2.View Tasks

3.Remove Task

4.Exit

@ User selects an option.


@ Corresponding function executes.


@ Loop continues until Exit is chosen.


*** Data Persistence Process

User Action → List Updated → File Updated → Data Saved

When the program restarts:

File Read → List Recreated → Tasks Available


*** Concepts Used

- Python Lists

- Functions

- Loops (while loop)

- Conditional Statements

- File Handling (open(), read(), write())

- Exception Handling

- Modular Programming



*** Outcome

The final outcome is a fully functional persistent console-based To-Do List application that:

Stores tasks permanently

Provides a clean menu interface

Handles invalid inputs safely

Demonstrates core Python programming

📄 Viva questions & answers for this project 
