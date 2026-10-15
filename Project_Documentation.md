# Project Documentation: Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**

Student Name: ____________________  
Student ID: ____________________  
Course: Python with AI — EWB Courses

## 2. Objective
The objective is to build a Python program that reads student marks and attendance, calculates totals and averages, assigns grades, identifies pass/fail status, and summarizes class and subject performance. It helps present student performance in a clear and organized way.

## 3. Technologies Used
- Python
- NumPy
- Pandas
- CSV dataset

## 4. Dataset Description
The sample file `students.csv` contains 20 fictional student records. Columns include Student ID, Name, Department, marks in Python, Mathematics, Statistics and Data Analysis, and Attendance percentage. Marks are out of 100.

## 5. Implementation
1. Imported NumPy and Pandas.
2. Loaded `students.csv` into a Pandas DataFrame.
3. Checked that required columns exist and that subject marks are numeric and between 0 and 100.
4. Used NumPy to calculate each student's total and average marks.
5. Used a function and conditional statements to assign grades.
6. Used a loop and a condition to determine Pass/Fail status. A student must score at least 35 in every subject to pass.
7. Used Pandas and NumPy to calculate class-level and subject-level statistics.
8. Displayed the top five students by average marks.
9. Saved all calculated results to `student_performance_results.csv`.

## 6. Key Features
- Student result summary
- Total and average marks
- Grade assignment
- Pass/Fail identification
- Overall class average and pass percentage
- Highest and lowest performers
- Subject-wise average, highest and lowest marks
- Top five performers
- Export of analysis results to CSV

## 7. Output / Screenshots
After running `python main.py`, take a screenshot of:
- Student Performance Summary
- Overall Class Analysis
- Subject-wise Performance
- Top 5 Performing Students

Paste your actual screenshots here before final submission.

## 8. Final Outcome
The project processes a sample student dataset and produces readable student-level and class-level performance summaries. It also exports the calculated data to a CSV file for later review.

## 9. Challenges & Learning
Complete this section honestly after running the project. Example topics to discuss: installing NumPy and Pandas, keeping the CSV file in the correct folder, checking marks for invalid values, and learning to use functions, loops, NumPy arrays, and Pandas DataFrames.

## 10. GitHub Repository
Repository URL: ____________________

After creating your repository, paste the actual URL above and submit it through the Google Form provided by EWB Courses.
