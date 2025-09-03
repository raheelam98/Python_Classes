print('Dimension in numpy (np)')
print('0D=scalar, 1D=Vecotr,  2D=Matrix, Tensor= 3D,4D,5D')
print('NumPy properties:- shape, size, itemsize, data, dtype')
# list take place in memory and then convert into hexadecimal and obj and reference (it is slow)
# why NumPy faster : directly work with bytes (e.g int is 8 bytes)

# shape :- size of each dimension of the array (form of tuple)
# shape :- one-dim array (elements,), two-dim (rows,columns), three_dim (matrices,rows, columns)
# size :- total number of elements in an array
# itemsize :- size of each element in bytes in the array.
# data :- give memory address 
# dtype (data type) :- data type of its elements
# dtype :- Create an array with specified data type (int32) e.g dtype=np.int32
# int (np.int8/16/32/64) , float, bool, str, object, type, complex types




import numpy as np
from nptyping import NDArray   # NDArray :- n dimension array


# pip install numpy
# pip install nptyping


# list 
list1 = [1,2,3,4]
print(list1)    # output:- [1, 2, 3, 4]

# ======= Numpy Properties =======

# 0D=scalar  (Zero Dimension Array)
print('\n zero dimension array')
zero_dim_array = np.array(2)
print(f'array : {zero_dim_array}')        #output:- 2
print(f'array shape: {zero_dim_array.shape}')  #output:- ()

# 1D=Vecotr  (One Dimension Array )
print('\n one dimension array')
one_dim_array = np.array([1,2,3,4])
print(f'array : {one_dim_array}')
print(f'array shape (elements,) : {one_dim_array.shape}')
print(f'total number of elements : {one_dim_array.size}')
print(f'size (in bytes) of each element : {one_dim_array.itemsize}')
print(f'memory address : {one_dim_array.data}')
print(f'data type : {one_dim_array.dtype}')

# 2D=Matrix (Two Dimension Array)
print('\n two dimension array:- note []tell how many dim')
two_dim_array = np.array([[1,2,3,4],
                          [5,6,7,8],
                          [9,10,11,12]])
print(f'array : {two_dim_array}')
print(f'array shape two-dim (rows,columns) : {two_dim_array.shape}')
print(f'total number of elements : {two_dim_array.size}')
print(f'size (in bytes) of each element : {two_dim_array.itemsize}')
print(f'memory address : {two_dim_array.data}')
print(f'data type : {two_dim_array.dtype}')

# 3D=Tensor (Three Dimension Array)
print('\n three dimension array:- note []tell how many dim')
three_dim_array :NDArray = np.array([ 
                                [[1,2,3], [4,5,6]],
                                [[7,8,9], [10,11,12]] 
                                 ])
print(f'array : {three_dim_array}')
print(f'array shape three-dim (matrices,rows,columns) : {three_dim_array.shape}')
print(f'total number of elements : {three_dim_array.size}')
print(f'size (in bytes) of each element : {three_dim_array.itemsize}')
print(f'memory address : {three_dim_array.data}')
print(f'data type : {three_dim_array.dtype}')

# ======= Numpy Math Opration =======

print('\n Numpy Math Opration  ')

nd_arr1 : NDArray = np.arange(1,13)
print(f"arange(1,13) : {nd_arr1}")

#nd_arr2 : NDArray = nd_arr2.reshape((3,3))
#nd_arr2: NDArray = nd_arr1.reshape((2, 2))
#print(f" {nd_arr2}")

list1: NDArray = np.arange(1, 10)
list2: NDArray = list1.reshape((3, 3))
print(f"\n list1.reshape((3, 3) of arange(1,10)")
print(list2)

list3: NDArray = np.arange(1, 13)
list4: NDArray = list3.reshape((2, 2, 3))
print(f"\n list3.reshape((2, 2, 3) of arange(1,13)")
print(list4)

# ======= Numpy Methods  =======

print("\n Numpy Methods")
my_list1 : NDArray = np.array([1, 2, 3, 4, 5])
print(f"Min value : {my_list1.min()}")
print(f"Min value : {my_list1.max()}")

my_list2 = np.ones((1,2,3), dtype=int)
print(f"np.ones((1,2,3), dtype=int ")
print(my_list2)