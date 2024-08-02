from os.path import exists, isfile
import sys
import inspect

def equals_(data1, data2):
    return data1 == data2

def add_(data1, data2):
    return data1 + data2

def in_list_(value, value_list):
    return value in value_list

def non_empty_string_(value):
    return len(value) > 0

def valid_file_on_disc_(value):
    return exists(value) and isfile(value)

def positive_value_(value):
    return value > 0

def min_(value, check):
    return value >= check

def max_(value, check):
    return value <= check

def range_(value, check1, check2):
    return min_(value, check1) and max_(value, check2)

def unique_name_(value):
    return True

function_map = {}
__functions = [obj for name, obj in inspect.getmembers(sys.modules[__name__])
                if (inspect.isfunction(obj) and not name.startswith("_"))]

for i in range(len(__functions)):
    function_map[__functions[i].__name__[0:-1]] = __functions[i]
