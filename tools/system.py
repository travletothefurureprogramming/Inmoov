import psutil

def cpu():
    return psutil.cpu_percent(1)

def ram():
    return psutil.virtual_memory().percent