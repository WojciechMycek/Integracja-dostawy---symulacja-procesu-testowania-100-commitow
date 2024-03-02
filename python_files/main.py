from Environment_load_testing import Environment_load_testing
import ctypes
import time

TestingObject = Environment_load_testing()
TestingObject.return_cpu_count()
TestingObject.return_CPU_usage_WINDOWS()