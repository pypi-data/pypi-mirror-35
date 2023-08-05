import ctypes


ptrdiff_t = ctypes.c_int32


class GoString(ctypes.Structure):
    _fields_ = [("p", ctypes.c_char_p),
                ("n", ptrdiff_t)]


def GoInt64(i):
    return ctypes.c_int64(i)


def GoInt32(i):
    return ctypes.c_int32(i)


def GoInt16(i):
    return ctypes.c_int16(i)


def GoInt8(i):
    return ctypes.c_int8(i)


def GoUint64(i):
    return ctypes.c_uint64(i)


def GoUint32(i):
    return ctypes.c_uint32(i)


def GoUint16(i):
    return ctypes.c_uint16(i)


def GoUint8(i):
    return ctypes.c_uint8(i)


def GoInt(i):
    return GoInt64(i)


def GoUint(i):
    return GoUint64(i)


def GoFloat32(i):
    return ctypes.c_float(i)


def GoFloat64(i):
    return ctypes.c_double(i)


string_return = GoString
# string = lambda x: ctypes.pointer(GoString(x))
string = GoString
int64 = GoInt64
int32 = GoInt32
int16 = GoInt16
int8 = GoInt8
uint64 = GoUint64
uint32 = GoUint32
uint16 = GoUint16
uint8 = GoInt8
goint = GoInt  # really no other thing to name this...
uint = GoUint
gofloat = GoFloat32
float32 = GoFloat32
float64 = GoFloat64
void = ctypes.c_long  # idk why this is...
