import numpy as np
import scipy
from PIL import Image

# image to array conversion
image = Image.open("test.jpg")
img_array = np.array(image)
image.show()


# kernel convolution

# first idea with horrible runtime
def kernel_convolution_loop(array, radius=1):
    amount_rows = len(array)
    amount_columns = len(array[0][:])
    new_array = np.zeros(dtype="u1", shape=(amount_rows, amount_columns, 3))
    for row in range(0, amount_rows):
        for column in range(0, amount_columns):
            amount_of_values = 0
            buffer_array = np.zeros(shape=3, dtype="i8")

            for m in range(-radius, radius + 1):
                for n in range(-radius, radius + 1):
                    if -1 < row + m < amount_rows:
                        if -1 < column + n < amount_columns:
                            amount_of_values += 1
                            buffer_array[:] = np.add(buffer_array, array[row + m][column + n])
            if amount_of_values > 1:
                new_array[row][column] = np.divide(buffer_array, amount_of_values)
            else:
                new_array[row][column] = buffer_array

    return new_array


# second idea with long runtime
def kernel_convolution_slice(array, radius=1):
    amount_rows = len(array)
    amount_columns = len(array[0])
    new_array = np.zeros(dtype="u1", shape=(amount_rows, amount_columns, 3))
    for row in range(0, amount_rows):
        for column in range(0, amount_columns):
            buffer_array = np.zeros(shape=3, dtype="i8")
            square = np.asarray(array[np.max([0, row - radius]): np.min([row + radius + 1, amount_rows]),
                                np.max([0, column - radius]): np.min([column + radius + 1, amount_columns])])
            red = square[:, :, 0].sum()
            green = square[:, :, 1].sum()
            blue = square[:, :, 2].sum()
            buffer_array[0:3] = [red, green, blue]

            buffer_array = np.divide(buffer_array, square.size / 3)

            new_array[row][column] = buffer_array

    return new_array


# third idea with scipy.signal.convolve
def kernel_convolution(array, radius=1):
    kernel = np.divide(np.ones((radius + 2, radius + 2, 1)), (radius + 2) ** 2)
    new_image = scipy.signal.convolve(array, kernel, mode='same')
    new_image = np.asarray(new_image, dtype='u1')
    return new_image


# third idea but with gaussian kernel
def gaussian_convolution(array, radius: int = 1, a=1.0):
    kernel = np.reshape(np.exp(-np.power(np.linspace(-radius * a, radius * a, num=2 * radius + 1), 2)),
                        (2 * radius + 1, 1))
    kernel = kernel @ np.transpose(kernel)

    kernel = np.reshape(kernel, (2 * radius + 1, 2 * radius + 1, 1))
    new_image = scipy.signal.convolve(array, kernel / kernel.sum(keepdims=False), mode='same')
    new_image = np.asarray(new_image, dtype='u1')
    return new_image


# parameter chosen through experimentation
#new_img_array = gaussian_convolution(img_array, 128, 0.032)
new_img_array = gaussian_convolution(img_array, 160, 0.0090)
new_image = Image.fromarray(new_img_array)
new_image.show()
new_img_array = gaussian_convolution(img_array, 40, 0.0010)
new_image = Image.fromarray(new_img_array)
new_image.show()
# new_image.save("blurred_test.png")
