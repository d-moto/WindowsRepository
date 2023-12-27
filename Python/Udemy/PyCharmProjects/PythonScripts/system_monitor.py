import psutil
import time


def get_system_status():
    """Retrieve basic system status including CPU, memory, and disk usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        'CPU Usage': f'{cpu_usage}%',
        'Memory Usage': f'{memory.percent}%',
        'Disk Usage': f'{disk.percent}%'
    }


# Monitor the system status in a loop
print("Monitoring system status... (Press Ctrl+C to stop)")
try:
    while True:
        status = get_system_status()
        print(f"CPU Usage: {status['CPU Usage']}, Memory Usage: {status['Memory Usage']}, Disk Usage: {status['Disk Usage']}")
        time.sleep(2)  # Update every 5 seconds
except KeyboardInterrupt:
    print("Monitoring stopped.")

