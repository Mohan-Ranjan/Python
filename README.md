Python

Student Progression Prediction Program
This Python program helps predict and display the progression outcomes of students based on their academic credits in the categories of Pass, Defer, and Fail. 
The program allows input for multiple students, calculates their progression outcomes, and generates histograms to visualize the results.

Features
Student Progression Outcome Prediction
The program prompts the user for the number of credits in Pass, Defer, and Fail.
Based on the inputs, the program determines the student's progression outcome:
Progress: 120 Pass credits, no Fail or Defer.
Module Trailer: 100 Pass credits, small number of Fail credits.
Module Retriever: 80 or fewer Pass credits, significant Fail credits.
Exclude: More than 80 Fail credits.

Input Validation
Ensures inputs are integers and are within the valid range (0, 20, 40, 60, 80, 100, 120).
Displays error messages if inputs are invalid or if the total credits do not add up to 120.

Multiple Student Prediction
The program allows entering multiple students' credit data.
The user can continue entering data for new students until 'q' is entered to quit, or 'y' to continue.

Histogram Visualization
The program generates a horizontal histogram that shows the number of students in each progression category.
An extension adds a vertical histogram for easier comparison.

Data Storage (Extensions)
Part 3: Stores progression data in a list, tuple, or dictionary.
Part 4: Saves progression data to a text file, which can be later read to display the results.
