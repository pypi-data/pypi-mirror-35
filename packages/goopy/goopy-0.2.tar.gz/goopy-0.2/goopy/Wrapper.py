import ctypes
from .__govars import *


ptrdiff_t = ctypes.c_int32


class Wrapper:
    def __init__(self, dll):
        self.dll = ctypes.cdll.LoadLibrary(dll)

        self.__funcdefs = {}

    def define(self, funcname, argtypes, restype):
        func = getattr(self.dll, funcname)
        func.argtypes = argtypes
        func.restype = restype
        self.__funcdefs[funcname] = [argtypes, restype, func]

    def __generic_function(self, funcdefs, *a):
        need = len(funcdefs[0])
        have = len(a)
        if need < have:
            raise ValueError("too many arguments")
        elif have > need:
            raise ValueError("too few arguments")

        corrected_args = []
        for i, arg in enumerate(a):
            exp_type = funcdefs[0][i]
            try:
                fixed_arg = exp_type(arg)
                corrected_args.append(fixed_arg)
            except TypeError as e:
                if exp_type == string:
                    try:
                        fixed_arg = exp_type()
                        fixed_arg.p = ctypes.c_char_p(arg.encode())
                        fixed_arg.n = ptrdiff_t(len(arg))
                        corrected_args.append(fixed_arg)
                        continue
                    except TypeError as e2:
                        raise e2
                raise e

        result = funcdefs[2](*corrected_args)

        try:
            return result.value
        except AttributeError:
            if type(result) == int:
                return result  # i guess it's an int / something that doesn't return anything?

            try:  # check if GoString method will work (aka the obj is pointer(GoString))
                second = ctypes.cast(result.p, ctypes.c_char_p)
                third = second.value
                final = third[:result.n]
                return final.decode()
            except AttributeError:  # probably doesn't have .p, ().value, .n, or .n.value
                raise ValueError("unknown object returned")

    def __getattr__(self, name):
        if name not in self.__funcdefs:
            raise AttributeError("no method '{}'".format(name))
        return lambda *a: self.__generic_function(self.__funcdefs[name], *a)
