# Module 13: Logging & Monitoring

## 📖 What You'll Learn
- Python logging module
- Production-ready logging
- Log levels and formatting
- Monitoring scripts
- Alerting systems

---

## 1. Python Logging Module

### Code Example

```python
import logging

# Basic logging
logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.warning("High memory usage")
logging.error("Database connection failed")

# Configure logging with format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)
logger.info("This is an info message")
logger.error("This is an error message")

# Log to file
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Multiple handlers (console + file)
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_format)

# File handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

---

## 2. Production-Ready Logging

### Code Example

```python
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import json

class JSONFormatter(logging.Formatter):
    """Format logs as JSON"""
    def format(self, record):
        log_data = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName
        }
        
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)

def setup_logging(log_file='app.log', level=logging.INFO):
    """Setup production logging configuration"""
    logger = logging.getLogger()
    logger.setLevel(level)
    
    # Rotating file handler (max 10MB, keep 5 backups)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,
        backupCount=5
    )
    file_handler.setFormatter(JSONFormatter())
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_format)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Usage
logger = setup_logging()
logger.info("Application started")
logger.error("An error occurred", exc_info=True)
```

---

## 3. Monitoring Scripts

### Code Example

```python
import psutil
import logging
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def get_cpu_usage(self):
        """Get CPU usage percentage"""
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self):
        """Get memory usage"""
        memory = psutil.virtual_memory()
        return {
            'total': memory.total,
            'used': memory.used,
            'percent': memory.percent
        }
    
    def get_disk_usage(self, path='/'):
        """Get disk usage"""
        disk = psutil.disk_usage(path)
        return {
            'total': disk.total,
            'used': disk.used,
            'percent': disk.percent
        }
    
    def check_thresholds(self):
        """Check if metrics exceed thresholds"""
        cpu = self.get_cpu_usage()
        memory = self.get_memory_usage()
        disk = self.get_disk_usage()
        
        alerts = []
        
        if cpu > 80:
            alerts.append(f"High CPU: {cpu}%")
            self.logger.warning(f"CPU usage high: {cpu}%")
        
        if memory['percent'] > 80:
            alerts.append(f"High Memory: {memory['percent']}%")
            self.logger.warning(f"Memory usage high: {memory['percent']}%")
        
        if disk['percent'] > 80:
            alerts.append(f"High Disk: {disk['percent']}%")
            self.logger.warning(f"Disk usage high: {disk['percent']}%")
        
        return alerts
    
    def generate_report(self):
        """Generate monitoring report"""
        cpu = self.get_cpu_usage()
        memory = self.get_memory_usage()
        disk = self.get_disk_usage()
        
        report = f"""
System Monitoring Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'=' * 50}

CPU Usage: {cpu}%
Memory Usage: {memory['percent']}% ({memory['used'] / 1024**3:.2f} GB / {memory['total'] / 1024**3:.2f} GB)
Disk Usage: {disk['percent']}% ({disk['used'] / 1024**3:.2f} GB / {disk['total'] / 1024**3:.2f} GB)
"""
        return report

# Usage
monitor = SystemMonitor()
alerts = monitor.check_thresholds()
if alerts:
    print("⚠ Alerts:")
    for alert in alerts:
        print(f"  - {alert}")
else:
    print("✅ All systems normal")

print(monitor.generate_report())
```

---

## 4. Alerting System

### Code Example

```python
import requests
import logging

class AlertManager:
    def __init__(self, slack_webhook=None, email_config=None):
        self.slack_webhook = slack_webhook
        self.email_config = email_config
        self.logger = logging.getLogger(__name__)
    
    def send_slack_alert(self, message, severity='warning'):
        """Send alert to Slack"""
        if not self.slack_webhook:
            return False
        
        emoji = {
            'info': ':information_source:',
            'warning': ':warning:',
            'critical': ':rotating_light:'
        }.get(severity, ':bell:')
        
        payload = {
            'text': f"{emoji} *{severity.upper()}*\n{message}",
            'username': 'Monitoring Bot'
        }
        
        try:
            response = requests.post(self.slack_webhook, json=payload)
            return response.status_code == 200
        except Exception as e:
            self.logger.error(f"Failed to send Slack alert: {e}")
            return False
    
    def send_alert(self, message, severity='warning'):
        """Send alert through all configured channels"""
        self.logger.log(
            logging.WARNING if severity == 'warning' else logging.CRITICAL,
            message
        )
        
        if self.slack_webhook:
            self.send_slack_alert(message, severity)

# Usage
alert_manager = AlertManager(
    slack_webhook='https://hooks.slack.com/services/YOUR/WEBHOOK'
)

# Send alerts
alert_manager.send_alert("CPU usage exceeded 90%", severity='critical')
alert_manager.send_alert("Deployment completed", severity='info')
```

---

## 📝 Key Takeaways

✅ **Use logging module** - Don't use print()
✅ **Log levels** - DEBUG, INFO, WARNING, ERROR, CRITICAL
✅ **Structured logging** - JSON format for parsing
✅ **Rotate logs** - Prevent disk fill
✅ **Monitor metrics** - CPU, memory, disk
✅ **Alert on thresholds** - Proactive monitoring

---

## Next Module

Ready for **Module 14: Testing & Debugging**? 🎯
