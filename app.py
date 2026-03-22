import os
import platform

print("=== System Info Tool ===")

# Username
print("User:", os.getlogin())

# OS info
print("OS:", platform.system(), platform.release())

# Machine name
print("Machine:", platform.node())
