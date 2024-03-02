import os

class CPU_load_testing:
  def return_cpu_count(self):
    cpu_count = os.cpu_count
    print("CPU count: ", cpu_count)