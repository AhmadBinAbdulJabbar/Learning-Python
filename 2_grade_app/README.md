# Grade App

A simple terminal-based Python application to manage student grades, generate reports, and identify top and lowest performers.

## Features

- **Add Students:** Input student names, subjects, and their marks.
- **View Report:** See a formatted report of all students, their subject-wise marks, and average grades.
- **Show Top & Lowest Performer:** Instantly find the student with the highest and lowest average.
- **Input Validation:** Ensures marks are between 0 and 100.
- **User-Friendly Menu:** Easy-to-use menu-driven interface.

## How to Use

1. **Run the Application**
   ```bash
   python grade_app.py
   ```

2. **Menu Options**
   - `1. Add Students`  
     Enter the number of students and subjects, then input names and marks for each subject.
   - `2. View Report`  
     Displays all students with their marks and average.
   - `3. Show Top & Lowest Performer`  
     Shows the student with the highest and lowest average grade.
   - `4. Exit`  
     Exits the application.

## Example

```
📘 Welcome to Grade App

📚 Menu
1. Add Students
2. View Report
3. Show Top & Lowest Performer
4. Exit
Enter your choice: 1
How many students? 2
How many subjects? 3
Enter subject name 1: math
Enter subject name 2: english
Enter subject name 3: science
Enter name of student 1: alice
Enter Marks of subject Math for Alice: 90
Enter Marks of subject English for Alice: 85
Enter Marks of subject Science for Alice: 95
✅ Alice was added successfully!
...
```

## Requirements

- Python 3.x

## Notes

- All data is stored in memory for the current session only.
- Marks must be integers between 0 and 100.