# method - 1
import importlib
import os
import sys
import importlib.util


def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class_1_obj = module_from_file('anil',
                               'C:\\Users\\Anil Kumar G-2780\\PycharmProjects\\Anil\\Robotframework_Practice\\test\\listeners.py')

if __name__ == '__main__':
    class_1_obj.muthu()

# method - 2


def callfunc(myfile, myfunc, *args):
    pathname, filename = os.path.split(myfile)
    sys.path.append(os.path.abspath(pathname))
    modname = os.path.splitext(filename)[0]
    mymod = importlib.import_module(modname)
    result = getattr(mymod, myfunc)(*args)
    return result


arg1 = None
arg2 = None
# result = callfunc("C:\\Users\\Anil Kumar G-2780\\PycharmProjects\\Anil\\Robotframework_Practice\\test\\listeners.py",
#                   "anil", arg1, arg2)
result = callfunc("C:\\Users\\Anil Kumar G-2780\\PycharmProjects\\Anil\\Robotframework_Practice\\test\\listeners.py", "anil")

# method - 3
# direct import
sys.path.insert(0, 'C:\\Users\\Anil Kumar G-2780\\PycharmProjects\\Anil\\Robotframework_Practice\\test\\listeners.py.py')