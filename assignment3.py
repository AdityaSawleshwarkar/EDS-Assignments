import numpy as np

data = np.array([
    [43.05, 27.79, 28.7, 27.79],
    [43.47, 28.52, 28.98, 27.89],
    [42.24, 28.16, 28.16, 25.63],
    [39.24, 26.16, 26.16, 26.16],
    [40.9, 26.03, 27.27, 25.65],
    [39.47, 26.31, 26.31, 25.21],
    [41.68, 25.63, 27.79, 25.46],
    [42.19, 27.61, 28.13, 26.21],
    [44.75, 28.35, 29.83, 28.21],
    [46.95, 28.88, 31.3, 28.53]
])

# Horizontal stacking
horizontal_stack = np.hstack((data[:, :2], data[:, 3:]))
print("Horizontal stacking:")
print(horizontal_stack)

# Vertical stacking
vertical_stack = np.vstack((data[1:3, :], data[7:9, :]))
print("Vertical stacking:")
print(vertical_stack)

# Sequence generation
sequence = np.arange(10, 101, 10)
print("Custom sequence generation:")
print(sequence)

# Arithmetic operations
mean = np.mean(data, axis=0)
sum = np.sum(data, axis=1)
max = np.max(data)
min = np.min(data)

print("Arithmetic operations:")
print("Mean:", mean)
print("Sum:", sum)
print("Max:", max)
print("Min:", min)

# Mathematical operations
sqrt = np.sqrt(data)
exp = np.exp(data)
log = np.log(data)

print("Mathematical operations:")
print("Square root:")
print(sqrt)
print("Exponential:")
print(exp)
print("Natural logarithm:")
print(log)


# Bitwise operators
bitwise_and = np.bitwise_and(data.astype(int), 5)
bitwise_or = np.bitwise_or(data.astype(int), 3)
bitwise_xor = np.bitwise_xor(data.astype(int), 9)

print("Bitwise operators:")
print("Bitwise AND:")
print(bitwise_and)
print("Bitwise OR:")
print(bitwise_or)
print("Bitwise XOR:")
print(bitwise_xor)


# Copying arrays
copy = np.copy(data)

# Viewing arrays
view = data.view()

print("Copying and viewing arrays:")
print("Copy:")
print(copy)
print("View:")
print(view)

# Data stacking
data_stack = np.dstack((data, data))
print("Data stacking:")
print(data_stack)

# Searching
indexes = np.where(data > 30)
print("Indexes where data > 30:")
print(indexes)

# Sorting
sorted_data = np.sort(data, axis=0)
print("Sorted data:")
print(sorted_data)

# Counting
count = np.count_nonzero(data > 28)
print("Count of elements > 28:", count)

# Broadcasting
broadcasted_data = data * 2
print("Broadcasted data (multiplied by 2):")
print(broadcasted_data)