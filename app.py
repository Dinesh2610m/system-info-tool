import os
import platform
import shutil

print("=== System Info Tool ===\n")

# Username
print("User:", os.getlogin())

# OS info
print("OS:", platform.system(), platform.release())

# Machine name
print("Machine:", platform.node())

# CPU info
print("Processor:", platform.processor())

# Disk usage
total, used, free = shutil.disk_usage("/")
print("\nDisk Usage:")
print("Total:", total // (2**30), "GB")
print("Used:", used // (2**30), "GB")
print("Free:", free // (2**30), "GB")
