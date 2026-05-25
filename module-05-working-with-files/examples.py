# Module 5: Working with Files - Code Examples

import os
from datetime import datetime

print("=" * 50)
print("MODULE 5: WORKING WITH FILES - EXAMPLES")
print("=" * 50)

# Example 1: Create sample log file
print("\n1. CREATING SAMPLE LOG FILE")
print("-" * 50)

sample_logs = """2024-01-30 10:00:00 INFO Server started successfully
2024-01-30 10:00:05 INFO Request received from 192.168.1.10
2024-01-30 10:00:10 ERROR Database connection failed
2024-01-30 10:00:15 WARNING High CPU usage detected: 85%
2024-01-30 10:00:20 INFO Request processed successfully
2024-01-30 10:00:25 ERROR Timeout while connecting to API
2024-01-30 10:00:30 WARNING Memory usage at 78%
2024-01-30 10:00:35 INFO Backup completed
2024-01-30 10:00:40 ERROR Failed to write to disk
2024-01-30 10:00:45 INFO Server health check passed
"""

with open('sample.log', 'w') as file:
    file.write(sample_logs)
print("Created sample.log")

# Example 2: Read entire file
print("\n2. READ ENTIRE FILE")
print("-" * 50)

with open('sample.log', 'r') as file:
    content = file.read()
    print(content[:200] + "...")  # Print first 200 chars

# Example 3: Read line by line
print("\n3. READ LINE BY LINE")
print("-" * 50)

with open('sample.log', 'r') as file:
    line_count = 0
    for line in file:
        line_count += 1
        if line_count <= 3:
            print(f"Line {line_count}: {line.strip()}")
    print(f"Total lines: {line_count}")

# Example 4: Count log levels
print("\n4. COUNT LOG LEVELS")
print("-" * 50)

def count_log_levels(log_file):
    counts = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}
    
    with open(log_file, 'r') as file:
        for line in file:
            for level in counts.keys():
                if level in line:
                    counts[level] += 1
                    break
    
    return counts

counts = count_log_levels('sample.log')
print("Log Level Statistics:")
for level, count in counts.items():
    print(f"  {level}: {count}")

# Example 5: Extract errors
print("\n5. EXTRACT ERRORS")
print("-" * 50)

def extract_errors(log_file):
    errors = []
    with open(log_file, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                errors.append(line.strip())
    return errors

errors = extract_errors('sample.log')
print(f"Found {len(errors)} errors:")
for error in errors:
    print(f"  {error}")

# Example 6: Write report to file
print("\n6. WRITE REPORT TO FILE")
print("-" * 50)

servers = [
    {'name': 'web-01', 'cpu': 45, 'memory': 60, 'status': 'healthy'},
    {'name': 'web-02', 'cpu': 78, 'memory': 75, 'status': 'warning'},
    {'name': 'db-01', 'cpu': 55, 'memory': 80, 'status': 'healthy'}
]

with open('server_report.txt', 'w') as file:
    file.write("SERVER HEALTH REPORT\n")
    file.write("=" * 60 + "\n")
    file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    for server in servers:
        line = f"{server['name']}: CPU {server['cpu']}%, MEM {server['memory']}% - {server['status']}\n"
        file.write(line)
    
    file.write("\n" + "=" * 60 + "\n")
    file.write(f"Total servers: {len(servers)}\n")

print("Report written to server_report.txt")

# Example 7: Append to file
print("\n7. APPEND TO FILE")
print("-" * 50)

with open('server_report.txt', 'a') as file:
    file.write("\nAdditional Notes:\n")
    file.write("- All systems operational\n")
    file.write("- Next check in 5 minutes\n")

print("Appended to server_report.txt")

# Example 8: Parse config file
print("\n8. PARSE CONFIG FILE")
print("-" * 50)

config_content = """# Application Configuration
host=localhost
port=8080
timeout=30
debug=true
# Database settings
db_host=db.example.com
db_port=5432
"""

with open('app.config', 'w') as file:
    file.write(config_content)

def parse_config(config_file):
    config = {}
    with open(config_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    return config

config = parse_config('app.config')
print("Parsed configuration:")
for key, value in config.items():
    print(f"  {key}: {value}")

# Example 9: Filter logs by keyword
print("\n9. FILTER LOGS BY KEYWORD")
print("-" * 50)

def filter_logs(input_file, output_file, keyword):
    count = 0
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if keyword in line:
                outfile.write(line)
                count += 1
    return count

count = filter_logs('sample.log', 'errors_only.log', 'ERROR')
print(f"Filtered {count} error lines to errors_only.log")

# Example 10: Check file existence
print("\n10. CHECK FILE EXISTENCE")
print("-" * 50)

files_to_check = ['sample.log', 'server_report.txt', 'nonexistent.txt']

for filename in files_to_check:
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"✓ {filename} exists ({size} bytes)")
    else:
        print(f"✗ {filename} not found")

# Example 11: Real DevOps - Log analyzer
print("\n11. REAL DEVOPS - LOG ANALYZER")
print("-" * 50)

def analyze_log_file(log_file):
    stats = {
        'total_lines': 0,
        'errors': 0,
        'warnings': 0,
        'info': 0,
        'error_messages': []
    }
    
    try:
        with open(log_file, 'r') as file:
            for line in file:
                stats['total_lines'] += 1
                
                if 'ERROR' in line:
                    stats['errors'] += 1
                    stats['error_messages'].append(line.strip())
                elif 'WARNING' in line:
                    stats['warnings'] += 1
                elif 'INFO' in line:
                    stats['info'] += 1
    except FileNotFoundError:
        print(f"Error: {log_file} not found")
        return None
    
    return stats

stats = analyze_log_file('sample.log')
if stats:
    print(f"Total lines: {stats['total_lines']}")
    print(f"Errors: {stats['errors']}")
    print(f"Warnings: {stats['warnings']}")
    print(f"Info: {stats['info']}")

# Example 12: Write structured report
print("\n12. WRITE STRUCTURED REPORT")
print("-" * 50)

def generate_analysis_report(log_file, output_file):
    stats = analyze_log_file(log_file)
    
    if not stats:
        return
    
    with open(output_file, 'w') as file:
        file.write("LOG ANALYSIS REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Source: {log_file}\n")
        file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        file.write("STATISTICS\n")
        file.write("-" * 60 + "\n")
        file.write(f"Total Lines: {stats['total_lines']}\n")
        file.write(f"Errors: {stats['errors']}\n")
        file.write(f"Warnings: {stats['warnings']}\n")
        file.write(f"Info: {stats['info']}\n\n")
        
        if stats['error_messages']:
            file.write("ERROR DETAILS\n")
            file.write("-" * 60 + "\n")
            for error in stats['error_messages']:
                file.write(f"{error}\n")

generate_analysis_report('sample.log', 'analysis_report.txt')
print("Analysis report written to analysis_report.txt")

print("\n" + "=" * 50)
print("END OF MODULE 5 EXAMPLES")
print("=" * 50)
print("\nFiles created:")
print("  - sample.log")
print("  - server_report.txt")
print("  - app.config")
print("  - errors_only.log")
print("  - analysis_report.txt")
