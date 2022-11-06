#arrays are similar to list the only diff is in list u can have different data types in 1 list but an array contains same datatype.
from array import array


a= array("i",[5,8,9,6,4]) #syntax and here i indicates integer values
print(a)
print(a.buffer_info()) # provides length of array with the adress value
