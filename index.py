import psutil

def get_cpu_info():
    # Get CPU information
    cpu_info = f"CPU Usage: {psutil.cpu_percent()}%"
    return cpu_info

def get_memory_info():
    # Get memory information
    mem_info = psutil.virtual_memory()
    memory_info = f"Total Memory: {mem_info.total} bytes | "
    memory_info += f"Available Memory: {mem_info.available} bytes | "
    memory_info += f"Used Memory: {mem_info.used} bytes | "
    memory_info += f"Memory Percent: {mem_info.percent}%"
    return memory_info

def main():
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()

    print("CPU Information:")
    print(cpu_info)

    print("\nMemory Information:")
    print(memory_info)

if __name__ == "__main__":
    main()
