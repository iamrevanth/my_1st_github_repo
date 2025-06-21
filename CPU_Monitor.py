print("""\n
      ************************************
          CPU Health Monitoring Program
      ************************************\n""")

import psutil
import time

THRESHOLD = 80  # CPU usage percentage threshold

def monitor_cpu():
    print("Monitoring CPU usage. Press Ctrl+C to stop.")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {cpu_usage}%")
            if cpu_usage > THRESHOLD:
                print(f"ALERT! CPU usage exceeds threshold: {cpu_usage}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu()