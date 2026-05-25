# Module 5: Working with Files - Practice Exercises

print("=" * 50)
print("MODULE 5 EXERCISES")
print("=" * 50)

# First, create a sample log file for exercises
sample_log = """2024-01-30 10:00:00 INFO Server started
2024-01-30 10:00:05 ERROR Database connection failed
2024-01-30 10:00:10 WARNING High memory usage
2024-01-30 10:00:15 INFO Request processed
2024-01-30 10:00:20 ERROR Timeout occurred
2024-01-30 10:00:25 INFO Backup completed
2024-01-30 10:00:30 WARNING Disk space low
2024-01-30 10:00:35 ERROR Failed to send email
"""

with open('exercise.log', 'w') as f:
    f.write(sample_log)

print("Created exercise.log for practice\n")

# Exercise 1: Read and Print
print("Exercise 1: Read and Print")
print("-" * 50)
print("Read 'exercise.log' and print all lines")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 2: Count Lines
print("\nExercise 2: Count Lines")
print("-" * 50)
print("Count total number of lines in 'exercise.log'")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 3: Count Errors
print("\nExercise 3: Count Errors")
print("-" * 50)
print("Count how many ERROR lines are in 'exercise.log'")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 4: Extract Errors
print("\nExercise 4: Extract Errors")
print("-" * 50)
print("Create a list of all ERROR messages from 'exercise.log'")
print("Print each error")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 5: Write to File
print("\nExercise 5: Write to File")
print("-" * 50)
print("Write the following servers to 'servers.txt':")
print("web-01, web-02, db-01")
print("Each on a new line")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 6: Append to File
print("\nExercise 6: Append to File")
print("-" * 50)
print("Append 'cache-01' to 'servers.txt'")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 7: Parse Config
print("\nExercise 7: Parse Config")
print("-" * 50)
print("Create a config file 'test.config' with:")
print("host=localhost")
print("port=8080")
print("timeout=30")
print("\nThen read and parse it into a dictionary")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 8: Filter Logs
print("\nExercise 8: Filter Logs")
print("-" * 50)
print("Read 'exercise.log' and write only WARNING lines")
print("to 'warnings.log'")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 9: Count by Level
print("\nExercise 9: Count by Level")
print("-" * 50)
print("Count ERROR, WARNING, and INFO in 'exercise.log'")
print("Store in a dictionary and print")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 10: Advanced - Generate Report
print("\nExercise 10: Advanced - Generate Report")
print("-" * 50)
print("Create a function that:")
print("1. Reads 'exercise.log'")
print("2. Counts ERROR, WARNING, INFO")
print("3. Writes a report to 'log_report.txt' with:")
print("   - Title")
print("   - Statistics")
print("   - List of all errors")
print("\nYour code here:")
print()

# TODO: Write your code here




print("\n" + "=" * 50)
print("Check solutions.py for answers!")
print("=" * 50)
