#data type interger
data_int = 20
print("data = ", data_int, "has type: ", type(data_int))

#data type float
data_float = 1.5
print("data = ", data_float, "has type: ", type(data_float))

#data type string
data_string = "diapit kutip"
print("data = ", data_string, "has type: ", type(data_string))

#data bool
data_bool = False
print("data = ", data_bool, "has type: ", type(data_bool))

#data complex
data_complex = complex(3,2)
print("data = ", data_complex, "has type: ", type(data_complex))

from ctypes import c_double

data_c_double = c_double(10.5)
print("data = ", data_c_double, "has type: ", type(data_c_double))