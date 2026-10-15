# Student Performance Analytics System

A beginner-friendly Python mini project for analyzing student marks and attendance using **Python, NumPy, and Pandas**.

## Features
- Reads 20 sample student records from `students.csv`.
- Uses a Pandas DataFrame to organize and analyze records.
- Uses NumPy for totals, averages, and subject calculations.
- Uses functions, loops, conditions, and data validation.
- Calculates each student's total and average marks.
- Assigns grades using the grading rules below.
- Determines Pass/Fail status.
- Reports class average, highest/lowest performers, pass percentage, and subject-wise performance.
- Displays the top 5 students.
- Saves the full results to `student_performance_results.csv`.

## Requirements
- Python 3.10 or newer recommended
- NumPy
- Pandas

## Install
Open Terminal / PowerShell in this folder and run:

```bash
python -m pip install numpy pandas
```

## Run
Keep `main.py` and `students.csv` in the same folder, then run:

```bash
python main.py
```

The program prints the analysis in the terminal and creates `student_performance_results.csv`.

## Dataset
The sample dataset has 20 fictional students and these columns:
- `Student_ID`, `Name`, `Department`
- `Python`, `Mathematics`, `Statistics`, `Data_Analysis` (marks out of 100)
- `Attendance` (percentage)

These are sample/fictitious records created for learning. Replace them with approved data if your instructor requires your own dataset.

## Rules used
### Grades (based on average marks)
| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 35–49.99 | E |
| Below 35 | F |

### Pass/Fail
A student passes only if they score **at least 35 in every subject**. Otherwise, the student fails.

## Project structure
```text
student-performance-analytics/
├── main.py
├── students.csv
├── README.md
├── Project_Documentation.md
└── requirements.txt
```

## Concepts demonstrated
Variables, data types, loops, functions, conditions, NumPy arrays, Pandas DataFrames, filtering, summary statistics, CSV file reading/writing.

## GitHub
Create a repository named `student-performance-analytics`, upload the project files, and copy the repository URL into the EWB Courses Google Form supplied by your trainer. Confirm the repository visibility requirements with your trainer.
