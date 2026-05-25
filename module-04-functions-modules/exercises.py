# Module 4: Functions & Modules - Practice Exercises

print("=" * 50)
print("MODULE 4 EXERCISES")
print("=" * 50)

# Exercise 1: Basic Function
print("\nExercise 1: Basic Function")
print("-" * 50)
print("Create a function called 'ping_server' that:")
print("- Takes server_name as parameter")
print("- Prints 'Pinging {server_name}...'")
print("- Returns True")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 2: Function with Return Value
print("\nExercise 2: Function with Return Value")
print("-" * 50)
print("Create a function 'check_disk_space' that:")
print("- Takes disk_usage (percentage) as parameter")
print("- Returns 'OK' if < 80, 'WARNING' if 80-90, 'CRITICAL' if > 90")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 3: Multiple Parameters
print("\nExercise 3: Multiple Parameters")
print("-" * 50)
print("Create a function 'check_server' that:")
print("- Takes: server_name, cpu, memory")
print("- Returns status message with all values")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 4: Default Arguments
print("\nExercise 4: Default Arguments")
print("-" * 50)
print("Create a function 'deploy' that:")
print("- Takes: environment, version")
print("- Has default parameters: rollback=True, notify=True")
print("- Prints deployment details")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 5: Multiple Return Values
print("\nExercise 5: Multiple Return Values")
print("-" * 50)
print("Create a function 'get_metrics' that:")
print("- Takes server_name")
print("- Returns three values: cpu, memory, disk (make up values)")
print("- Call it and unpack the values")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 6: Lambda Function
print("\nExercise 6: Lambda Function")
print("-" * 50)
print("Given: servers = [")
print("    {'name': 'web-01', 'cpu': 75},")
print("    {'name': 'web-02', 'cpu': 45},")
print("    {'name': 'web-03', 'cpu': 90}")
print("]")
print("\nSort servers by CPU using lambda")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 7: Filter with Lambda
print("\nExercise 7: Filter with Lambda")
print("-" * 50)
print("Using the same servers list from Exercise 6:")
print("Filter servers with CPU > 70 using lambda and filter()")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 8: Variable Arguments
print("\nExercise 8: Variable Arguments")
print("-" * 50)
print("Create a function 'check_ports' that:")
print("- Takes any number of port numbers (*ports)")
print("- Prints each port with 'Checking port {port}'")
print("- Test with different numbers of ports")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 9: Keyword Arguments
print("\nExercise 9: Keyword Arguments")
print("-" * 50)
print("Create a function 'create_vm' that:")
print("- Takes **config as parameter")
print("- Prints all configuration key-value pairs")
print("- Test with: name='vm-01', cpu=4, memory=8")
print("\nYour code here:")
print()

# TODO: Write your code here




# Exercise 10: Advanced - Validation Function
print("\nExercise 10: Advanced - Validation Function")
print("-" * 50)
print("Create a function 'validate_config' that:")
print("- Takes: environment, version, tests_passed, approval")
print("- For 'production': requires tests_passed AND approval")
print("- For others: no requirements")
print("- Returns tuple: (can_deploy, message)")
print("\nYour code here:")
print()

# TODO: Write your code here




print("\n" + "=" * 50)
print("Check solutions.py for answers!")
print("=" * 50)
