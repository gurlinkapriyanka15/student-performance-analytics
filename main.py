"""
Student Performance Analytics System
Python + NumPy + Pandas mini project
Run: python main.py
"""

import numpy as np
import pandas as pd


MARK_COLUMNS = ["Python", "Mathematics", "Statistics", "Data_Analysis"]
PASS_MARK = 35  # A student must score at least 35 in every subject to pass.


def calculate_grade(average):
    """Return a grade based on the student's average mark."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 35:
        return "E"
    else:
        return "F"


def add_student_results(data):
    """Calculate totals, averages, grades, and pass/fail status."""
    # NumPy is used for numerical calculations.
    marks_array = data[MARK_COLUMNS].to_numpy(dtype=float)
    data["Total_Marks"] = np.sum(marks_array, axis=1)
    data["Average_Marks"] = np.round(np.mean(marks_array, axis=1), 2)

    grades = []
    results = []
    for _, student in data.iterrows():
        grades.append(calculate_grade(student["Average_Marks"]))

        # Pass only when the student scores at least 35 in every subject.
        if all(student[subject] >= PASS_MARK for subject in MARK_COLUMNS):
            results.append("Pass")
        else:
            results.append("Fail")

    data["Grade"] = grades
    data["Result"] = results
    return data


def show_student_summary(data):
    """Display each student's calculated result."""
    print("\n" + "=" * 78)
    print("STUDENT PERFORMANCE SUMMARY")
    print("=" * 78)
    columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance"
    ]
    print(data[columns].to_string(index=False))


def show_overall_analysis(data):
    """Display class-level and subject-level statistics."""
    print("\n" + "=" * 78)
    print("OVERALL CLASS ANALYSIS")
    print("=" * 78)

    student_count = len(data)
    passed_count = int((data["Result"] == "Pass").sum())
    failed_count = student_count - passed_count
    class_average = data["Average_Marks"].mean()

    print(f"Total students       : {student_count}")
    print(f"Passed students      : {passed_count}")
    print(f"Failed students      : {failed_count}")
    print(f"Pass percentage      : {passed_count / student_count * 100:.2f}%")
    print(f"Overall class average: {class_average:.2f}")

    best_student = data.loc[data["Average_Marks"].idxmax()]
    lowest_student = data.loc[data["Average_Marks"].idxmin()]
    print(
        f"Highest performer    : {best_student['Name']} "
        f"({best_student['Average_Marks']:.2f})"
    )
    print(
        f"Lowest performer     : {lowest_student['Name']} "
        f"({lowest_student['Average_Marks']:.2f})"
    )


def show_subject_analysis(data):
    """Calculate average, highest, and lowest marks for each subject."""
    print("\n" + "=" * 78)
    print("SUBJECT-WISE PERFORMANCE")
    print("=" * 78)

    rows = []
    for subject in MARK_COLUMNS:
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(data[subject].to_numpy())), 2),
            "Highest": int(data[subject].max()),
            "Lowest": int(data[subject].min()),
        })

    subject_summary = pd.DataFrame(rows)
    print(subject_summary.to_string(index=False))

    best_subject = subject_summary.loc[subject_summary["Average"].idxmax()]
    print(
        f"\nBest subject by class average: {best_subject['Subject']} "
        f"({best_subject['Average']:.2f})"
    )


def show_top_performers(data, number=5):
    """Display the top students ranked by average marks."""
    print("\n" + "=" * 78)
    print(f"TOP {number} PERFORMING STUDENTS")
    print("=" * 78)

    top_students = data.nlargest(number, "Average_Marks")
    print(
        top_students[
            ["Student_ID", "Name", "Department", "Average_Marks", "Grade"]
        ].to_string(index=False)
    )


def save_results(data):
    """Save calculated results into a new CSV file."""
    output_file = "student_performance_results.csv"
    data.to_csv(output_file, index=False)
    print(f"\nDetailed results saved to: {output_file}")


def main():
    """Load the CSV dataset and run all project analyses."""
    try:
        data = pd.read_csv("students.csv")
    except FileNotFoundError:
        print("Error: students.csv was not found.")
        print("Keep students.csv in the same folder as main.py.")
        return

    required_columns = [
        "Student_ID", "Name", "Department", *MARK_COLUMNS, "Attendance"
    ]
    missing_columns = [column for column in required_columns if column not in data.columns]
    if missing_columns:
        print("Error: dataset is missing columns:", ", ".join(missing_columns))
        return

    if data.empty:
        print("Error: students.csv has no student records.")
        return

    # Check that marks are valid numbers between 0 and 100.
    for subject in MARK_COLUMNS:
        data[subject] = pd.to_numeric(data[subject], errors="coerce")
    if data[MARK_COLUMNS].isna().any().any():
        print("Error: subject marks must be numeric and cannot be blank.")
        return
    if ((data[MARK_COLUMNS] < 0) | (data[MARK_COLUMNS] > 100)).any().any():
        print("Error: marks must be between 0 and 100.")
        return

    data = add_student_results(data)
    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    show_student_summary(data)
    show_overall_analysis(data)
    show_subject_analysis(data)
    show_top_performers(data, number=5)
    save_results(data)


if __name__ == "__main__":
    main()
