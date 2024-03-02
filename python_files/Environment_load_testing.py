import os
import time
import ctypes

from SYSTEM_PERFORMANCE_INFORMATION import SYSTEM_PERFORMANCE_INFORMATION
class Environment_load_testing:

  def return_cpu_count(self):
    cpu_count = os.cpu_count
    print("CPU count: ", cpu_count)
  
  def return_CPU_usage_WINDOWS(self):
    kernel32 = ctypes.windll.kernel32
    GetSystemTimes = kernel32.GetSystemTimes
    GetSystemTimes.argtypes = [ctypes.POINTER(SYSTEM_PERFORMANCE_INFORMATION), ctypes.POINTER(SYSTEM_PERFORMANCE_INFORMATION), ctypes.POINTER(SYSTEM_PERFORMANCE_INFORMATION)]
    GetSystemTimes.restype = ctypes.c_int

    system_performance_info = SYSTEM_PERFORMANCE_INFORMATION()
    GetSystemTimes(ctypes.byref(system_performance_info), None, None)
    
    idle_time = sum(system_performance_info.IdleTime)
    total_time = sum(system_performance_info.IdleTime) + sum(system_performance_info.KernelTime) + sum(system_performance_info.UserTime)
    
    if total_time != 0:
        cpu_usage = (total_time - idle_time) * 100.0 / total_time
    else:
        cpu_usage = 0.0
        
    return cpu_usage
  
    cpu_usage = get_cpu_usage()
    print(f"CPU Usage: {cpu_usage:.2f}%")
    time.sleep(1)

