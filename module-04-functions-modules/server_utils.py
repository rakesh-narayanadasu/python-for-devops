# Module 4: Example Module - Server Utilities

def check_health(server_name, cpu, memory):
    """
    Check if server is healthy based on resource usage.
    
    Args:
        server_name (str): Name of the server
        cpu (int): CPU usage percentage
        memory (int): Memory usage percentage
    
    Returns:
        str: Health status message
    """
    if cpu > 90 or memory > 90:
        return f"{server_name}: CRITICAL"
    elif cpu > 80 or memory > 80:
        return f"{server_name}: WARNING"
    else:
        return f"{server_name}: OK"


def format_uptime(hours):
    """
    Convert hours to days and hours format.
    
    Args:
        hours (int): Total hours
    
    Returns:
        str: Formatted uptime string
    """
    days = hours // 24
    remaining_hours = hours % 24
    return f"{days}d {remaining_hours}h"


def validate_ip(ip):
    """
    Basic IP address validation.
    
    Args:
        ip (str): IP address to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True


def validate_port(port):
    """
    Validate port number.
    
    Args:
        port (int): Port number to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(port, int):
        return False
    return 1 <= port <= 65535


def format_bytes(bytes_value):
    """
    Convert bytes to human-readable format.
    
    Args:
        bytes_value (int): Number of bytes
    
    Returns:
        str: Formatted string (KB, MB, GB, TB)
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0
    value = float(bytes_value)
    
    while value >= 1024 and unit_index < len(units) - 1:
        value /= 1024
        unit_index += 1
    
    return f"{value:.2f} {units[unit_index]}"


def calculate_percentage(part, total):
    """
    Calculate percentage.
    
    Args:
        part (float): Part value
        total (float): Total value
    
    Returns:
        float: Percentage rounded to 2 decimals
    """
    if total == 0:
        return 0.0
    return round((part / total) * 100, 2)


if __name__ == "__main__":
    print("Server Utilities Module")
    print("=" * 50)
    
    print("\nTesting functions:")
    print(check_health("web-01", 85, 70))
    print(format_uptime(72))
    print(f"Valid IP: {validate_ip('192.168.1.1')}")
    print(f"Valid port: {validate_port(8080)}")
    print(f"Formatted bytes: {format_bytes(1536000)}")
    print(f"Percentage: {calculate_percentage(45, 100)}%")
