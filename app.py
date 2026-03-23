import platform
import psutil

def get_system_info():
    info = ""

    info += "=== System Information ===\n"
    info += f"System: {platform.system()}\n"
    info += f"Node Name: {platform.node()}\n"

    info += "\n=== CPU Info ===\n"
    info += f"Physical cores: {psutil.cpu_count(logical=False)}\n"
    info += f"CPU Usage: {psutil.cpu_percent(interval=1)}%\n"

    info += "\n=== Memory Info ===\n"
    memory = psutil.virtual_memory()
    info += f"Total: {memory.total}\n"
    info += f"Used: {memory.used}\n"

    return info


if __name__ == "__main__":
    data = get_system_info()

    with open("system_log.txt", "w") as file:
        file.write(data)

    print("Log saved to system_log.txt")