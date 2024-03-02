import ctypes

class SYSTEM_PERFORMANCE_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('IdleTime', ctypes.c_int64 * 4),
        ('KernelTime', ctypes.c_int64 * 4),
        ('UserTime', ctypes.c_int64 * 4),
        ('Reserved1', ctypes.c_int32 * 4),
        ('Reserved2', ctypes.c_int32 * 4)
    ]