import pathlib
import ctypes
from ctypes import c_double, c_int, c_bool, CFUNCTYPE, POINTER

class SDOF_Peaks(ctypes.Structure):
    _fields_ = [
        ("max_displ",      c_double),
        ("max_accel",      c_double),
        ("time_max_accel", c_double)
    ]

class SDOF_Config(ctypes.Structure):
    _fields_ = [
        ("alpha_m",      c_double),
        ("alpha_f",      c_double),
        ("beta",         c_double),
        ("gamma",        c_double)
    ]


try:
    lib = ctypes.cdll.LoadLibrary(pathlib.Path(__file__).parents[0]/"_fsdof.so")
    conf = lib.CONF
    _fsdof_peaks = lib.fsdof_peaks
    _fsdof_peaks.restype = c_int
    _fsdof_peaks.argtypes = (
        POINTER(SDOF_Config),
        c_double,  c_double,  c_double,
        c_double, c_int, POINTER(c_double), c_double,
        POINTER(SDOF_Peaks)
    )

    CONFIG = SDOF_Config()

except:
    raise

#   elastic_sdof()
#   plastic


def sdof(m,c,k,f,dt):
    pass

def peaks(m,c,k, f, dt):
    response = SDOF_Peaks()
    _fsdof_peaks(CONFIG, m, c, k, 1.0, len(f), f.ctypes.data_as(POINTER(c_double)), dt, response)
    return response



# import numpy as np
# r = fsdof(1.,1.,1., 0.01, np.sin(np.linspace(0, 5, 100)))
# print(r.max_displ)


