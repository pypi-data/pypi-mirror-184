# Converts a numpy string array with hex values to int 

```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install hexarray2decimal

from hexarray2decimal import numpy_hex_string_array_to_int

a1 = 20000 * ["0xffff", "0xa011", "0xb122", "0x99ff", "0x00ee", "0x0b54"]
a1r = numpy_hex_string_array_to_int(numpyarray=a1)
print(a1r)
# [65535 40977 45346 ... 39423   238  2900]


a1 = 20000 * ["0xff", "0xa0", "0xb1", "0x99", "0x00", "0x0b"]
a1r = numpy_hex_string_array_to_int(numpyarray=a1)
print(a1r)
# [255 160 177 ... 153   0  11]

a1 = 20000 * ["ff", "a0", "b1", "99", "00", "0b"]
a1r = numpy_hex_string_array_to_int(numpyarray=a1)
print(a1r)
# [255 160 177 ... 153   0  11]
a1 = 20000 * ["f", "a", "b", "9", "0", "c"]
a1r = numpy_hex_string_array_to_int(numpyarray=a1)
print(a1r)
# [15 10 11 ...  9  0 12]
a1 = 20000 * ["0xFF", "0xA1", "0xB2", "0x99", "0xE0", "0xCB"]
a1r = numpy_hex_string_array_to_int(numpyarray=a1)
print(a1r)
# [255 161 178 ... 153 224 203]


# Different string sizes may lead to unexpected behavior:
a1 = 20000 * ["fffff", "a", "b", "9", "0", "c"]
a1r = numpy_hex_string_array_to_int(numpyarray=a1)
print(a1r)
# [1048575  655360  720896 ...  589824       0  786432]
```
