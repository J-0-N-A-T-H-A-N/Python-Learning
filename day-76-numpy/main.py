import numpy as np
from numpy.random import random
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image

# array_1d = np.array([1.1, 9.2, 8.1, 4.7])
#
# print(array_1d.shape)
# print(array_1d[2])
# print(array_1d.ndim)        # Number of dimensions
#
# array_2d = np.array([[1, 2, 3, 9],[5, 6, 7, 8]])
# print(array_2d.shape)
# print(array_2d[0, :])
# print(array_2d.ndim)
# print(array_2d)

# mystery_array = np.array([[[0, 1, 2, 3],
#                            [4, 5, 6, 7]],
#
#                           [[7, 86, 6, 98],
#                            [5, 1, 0, 4]],
#
#                           [[5, 36, 32, 48],
#                            [97, 0, 27, 18]]])
# #
# # print(mystery_array.ndim)
# print(mystery_array.shape)
# print(mystery_array[-1, -1, -1])
# print(mystery_array[-1, -1])
# print(mystery_array[-1])
# print(f"\n")
# print(mystery_array[:, :, 0])       # colon for axes

# a = np.arange(10, 30)
#
# print(a)
# last_three = a[-4:-1]
# print(last_three)
# selection = a[3:7]
# print(selection)
# except_twelve = np.delete(a,2)
# print(except_twelve)
#
# print(np.flip(a))       # Reverse order
#
# new_array = np.array([6, 0, 9, 0, 0, 5, 0])
# print(new_array)
# print(np.where(new_array > 0))
#
# # Generate random 3*3 matrix
# rand_matrix = np.random.random((3,3,3))
# print(rand_matrix)

# x = np.linspace(0, 100, 9)
# print(x)
# y = np.linspace(-3, 3, 9)
# print(y)
# plt.plot(x, y)
# plt.show()

# noise = np.random.random((128, 128, 3))
# print(noise.shape)
# plt.imshow(noise)
# plt.show()

# Vector Addition
# v1 = np.array([4, 5, 2, 7])
# v2 = np.array([2, 1, 3, 3])
# result = v1 + v2
# print(f"Addition: {result}")
# result = v1 * v2
# print(f"Multiplication: {result}")
# result = v1 - 1
# print(f"Broadcasting: {result}")
#
# a1 = np.array([[1, 3],
#                [0, 1],
#                [6, 2],
#                [9, 7]])
#
# b1 = np.array([[4, 1, 3],
#                [5, 8, 5]])
#
# result = np.matmul(a1, b1)      # Matrix Multiplication
# print(result)

img = misc.face()
print(type(img))
print(img.shape)
# plt.imshow(img)
# plt.show
sRGB = img / 255
grey_vals = np.array([0.2126, 0.7152, 0.0722])
grey_img = np.matmul(sRGB, grey_vals)
plt.imshow(grey_img, cmap="gray")
upside_down_grey_img = np.flip(grey_img)
rotated_color = np.rot90(img)
# plt.imshow(upside_down_grey_img, cmap="gray")   # cmap indicated greyscale
# plt.imshow(rotated_color)
solarised_color = np.invert(img)
plt.imshow(solarised_color)
plt.show()
