import os
import time

class Environment_load_testing:

  def return_cpu_count(self):
    cpu_count = os.cpu_count
    print("CPU count: ", cpu_count)
  

