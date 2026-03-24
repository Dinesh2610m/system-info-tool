import platform
import psutil
import time

def get_system_info():
    info = ""

    info += "=== System Information ===\n"
    info += f"System: {platform.system()}\n"
    info += f"Node Name: {platform.node()}\n"

    info += "\n=== CPU Info ===\n"
    info += f"CPU Usage: {psutil.cpu_percent(interval=1)}%\n"

    memory = psutil.virtual_memory()
    info += "\n=== Memory Info ===\n"
    info += f"Memory Usage: {memory.percent}%\n"

    return info


if __name__ == "__main__":
    while True:
        data = get_system_info()

        with open("system_log.txt", "a") as file:
            file.write(data + "\n\n")

        print("Logged system data...")

        time.sleep(5)