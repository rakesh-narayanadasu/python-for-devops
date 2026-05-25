# Module 5: Working with Files - Exercise Solutions

from datetime import datetime

print("=" * 50)
print("MODULE 5 EXERCISE SOLUTIONS")
print("=" * 50)

# Solution 1: Read and Print
print("\nSolution 1: Read and Print")
print("-" * 50)

with open('exercise.log', 'r') as file:
    for line in file:
        print(line.strip())

# Solution 2: Count Lines
print("\nSolution 2: Count Lines")
print("-" * 50)

with open('exercise.log', 'r') as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")

# Alternative method
with open('exercise.log', 'r') as file:
    count = sum(1 for line in file)
    print(f"Total lines (method 2): {count}")

# Solution 3: Count Errors
print("\nSolution 3: Count Errors")
print("-" * 50)

error_count = 0
with open('exercise.log', 'r') as file:
    for line in file:
        if 'ERROR' in line:
            error_count += 1

print(f"Total errors: {error_count}")

# Solution 4: Extract Errors
print("\nSolution 4: Extract Errors")
print("-" * 50)

errors = []
with open('exercise.log', 'r') as file:
    for line in file:
        if 'ERROR' in line:
            errors.append(line.strip())

print("Error messages:")
for error in errors:
    print(f"  {error}")

# Solution 5: Write to File
print("\nSolution 5: Write to File")
print("-" * 50)

servers = ['web-01', 'web-02', 'db-01']

with open('servers.txt', 'w') as file:
    for server in servers:
        file.write(server + '\n')

print("Written to servers.txt")

# Solution 6: Append to File
print("\nSolution 6: Append to File")
print("-" * 50)

with open('servers.txt', 'a') as file:
    file.write('cache-01\n')

print("Appended to servers.txt")

# Verify
with open('servers.txt', 'r') as file:
    print("Current servers.txt content:")
    print(file.read())

# Solution 7: Parse Config
print("\nSolution 7: Parse Config")
print("-" * 50)

# Create config file
config_content = """host=localhost
port=8080
timeout=30
"""

with open('test.config', 'w') as file:
    file.write(config_content)

# Parse config
config = {}
with open('test.config', 'r') as file:
    for line in file:
        line = line.strip()
        if line and '=' in line:
            key, value = line.split('=', 1)
            config[key.strip()] = value.strip()

print("Parsed configuration:")
for key, value in config.items():
    print(f"  {key}: {value}")

# Solution 8: Filter Logs
print("\nSolution 8: Filter Logs")
print("-" * 50)

warning_count = 0
with open('exercise.log', 'r') as infile, open('warnings.log', 'w') as outfile:
    for line in infile:
        if 'WARNING' in line:
            outfile.write(line)
            warning_count += 1

print(f"Wrote {warning_count} warnings to warnings.log")

# Solution 9: Count by Level
print("\nSolution 9: Count by Level")
print("-" * 50)

counts = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}

with open('exercise.log', 'r') as file:
    for line in file:
        for level in counts.keys():
            if level in line:
                counts[level] += 1
                break

print("Log level counts:")
for level, count in counts.items():
    print(f"  {level}: {count}")

# Solution 10: Advanced - Generate Report
print("\nSolution 10: Advanced - Generate Report")
print("-" * 50)

def generate_log_report(log_file, report_file):
    counts = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}
    errors = []
    
    # Analyze log file
    with open(log_file, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                counts['ERROR'] += 1
                errors.append(line.strip())
            elif 'WARNING' in line:
                counts['WARNING'] += 1
            elif 'INFO' in line:
                counts['INFO'] += 1
    
    # Write report
    with open(report_file, 'w') as file:
        file.write("LOG ANALYSIS REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Source: {log_file}\n")
        file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        file.write("STATISTICS\n")
        file.write("-" * 60 + "\n")
        for level, count in counts.items():
            file.write(f"{level}: {count}\n")
        
        file.write("\nERROR DETAILS\n")
        file.write("-" * 60 + "\n")
        if errors:
            for error in errors:
                file.write(f"{error}\n")
        else:
            file.write("No errors found\n")
        
        file.write("\n" + "=" * 60 + "\n")

generate_log_report('exercise.log', 'log_report.txt')
print("Report generated: log_report.txt")

# Display the report
print("\nReport content:")
with open('log_report.txt', 'r') as file:
    print(file.read())

print("\n" + "=" * 50)
print("END OF SOLUTIONS")
print("=" * 50)
print("\nFiles created:")
print("  - servers.txt")
print("  - test.config")
print("  - warnings.log")
print("  - log_report.txt")
