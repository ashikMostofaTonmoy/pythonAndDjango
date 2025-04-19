# Python Day 4: String, JSON, Libraries, and Error Handling

This package contains comprehensive teaching materials for Day 4 of the Python course, covering String, JSON, Libraries, Iterators, Modules, Dates, Math, Regex, Try/Except, and String formatting.

## Contents

### 1. Lecture Material
- Comprehensive markdown document covering all Day 4 topics with detailed explanations and code examples
- Located in: `/lecture_material/python_day4_lecture.md`

### 2. Real-life Projects

#### Task Scheduler with Dates and JSON Data
- A command-line application for managing tasks with due dates
- Features include adding tasks, saving to JSON, filtering by date, and more
- Located in: `/project/task_scheduler/`
- Main file: `task_scheduler.py`
- Documentation: `README.md`

#### Regex-Based Log File Analyzer
- A command-line application for analyzing log files using regular expressions
- Features include parsing logs, generating statistics, and detecting anomalies
- Located in: `/project/log_analyzer/`
- Main file: `log_analyzer.py`
- Documentation: `README.md`

### 3. PowerPoint Presentation
- Colorful slides covering all Day 4 topics with code examples
- Located in: `/presentation/Python_Day4_Lecture.pptx`

## How to Use These Materials

### For Instructors

1. Review the lecture material in `/lecture_material/python_day4_lecture.md`
2. Use the PowerPoint presentation for classroom teaching
3. Demonstrate the real-life projects to show practical applications
4. Assign exercises based on the projects

### For Students

1. Follow along with the PowerPoint presentation during class
2. Read the detailed lecture material for in-depth understanding
3. Explore the real-life projects to see concepts in action
4. Modify the projects to practice and extend your skills

## Running the Projects

### Task Scheduler

1. Navigate to the project directory:
   ```
   cd project/task_scheduler
   ```

2. Run the application:
   ```
   python task_scheduler.py
   ```

3. Follow the on-screen menu to add tasks, view tasks, filter tasks, etc.

### Log File Analyzer

1. Navigate to the project directory:
   ```
   cd project/log_analyzer
   ```

2. Generate a sample log file for testing:
   ```
   python log_analyzer.py --generate-sample
   ```

3. Analyze the sample log file:
   ```
   python log_analyzer.py sample_log.txt
   ```

4. Try different options:
   ```
   python log_analyzer.py sample_log.txt --show-attacks --show-hourly --output report.json
   ```

## Learning Objectives

By the end of Day 4, students should be able to:

1. Work with strings and use different string formatting methods
2. Create and use iterators and generators
3. Import and create modules
4. Work with dates, times, and perform date arithmetic
5. Use mathematical functions and generate random numbers
6. Process JSON data and work with JSON files
7. Use regular expressions for pattern matching and text extraction
8. Handle exceptions properly with try-except blocks
9. Use various libraries and modules from Python's standard library
10. Apply these concepts to real-world problems
