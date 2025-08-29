# 🧑‍🎓 Student Situation Checker

A command-line tool that takes a student's name and grade average, determines if they have passed or failed, and displays all the information in a summary.

## Features

* **Student Data Input**: Collects a single student's name and average grade.
* **Situation Logic**: Automatically determines if a student's situation is "Passed" (average >= 7) or "Failed".
* **Dictionary Storage**: Uses a Python dictionary to store and organize the student's data (name, average, situation).
* **Clear Summary**: Prints a clean key-value summary of the student's final record.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `student_list_average.py`).
3.  Run the script from your terminal:
    ```sh
    python student_list_average.py
    ```
4.  The program will prompt you to enter a name and then that student's average.
5.  The script will immediately display the final record, including the calculated situation.

### Example Session

```sh
> python student_list_average.py
Name:
John
John Average:
8.5
  - name: John
  - average: 8.5
  - situation: Passed
```
