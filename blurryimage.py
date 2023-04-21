import numpy as np
from PIL import Image

#image = Image.open("Heart.png")
#img_array = np.array(image)
#image.show()
# kernel convolution


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

            buffer_array = np.divide(buffer_array,   square.size / 3)

            new_array[row][column] = buffer_array

    return new_array

def kernel_convolution_with_iterator(array, radius=1):
    amount_rows = len(array)
    amount_columns = len(array[0])
    new_array = np.zeros(dtype="u1", shape=(amount_rows, amount_columns, 3))

    for index, x in np.ndenumerate(array):
        buffer_array = np.zeros(shape=3, dtype="i8")
        square = np.asarray(array[np.max([0, index[0] - radius]): np.min([index[0] + radius + 1, amount_rows]),
                            np.max([0, index[1] - radius]): np.min([index[1] + radius + 1, amount_columns])])

        red = square[:, :, 0].sum()
        green = square[:, :, 1].sum()
        blue = square[:, :, 2].sum()
        buffer_array[0:3] = [red, green, blue]
        buffer_array = np.divide(buffer_array, square.size / 3)
        new_array[index[0]][index[1]] = buffer_array

    return new_array


def kernel_convolution_element(array, radius=1):
    # TODO np.convolve() documenation nachschauen
    pass


#print(img_array.shape)
#mean_pixel_value(img_array)
#new_img_array = kernel_convolution_with_iterator(img_array, 50)
#new_image = Image.fromarray(new_img_array)
#new_image.show()
#new_img_array = kernel_convolution_loop(img_array, 50)
#new_image = Image.fromarray(new_img_array)
#new_image.show()

#new_image.save("blurredHeart.png")
#jessi_img = Image.open("Jessi_und_Molly.jpg")
#jessi_array = np.asarray(jessi_img)
#blurred_jessi_img = Image.fromarray(kernel_convolution_slice(jessi_array, radius=80))
#blurred_jessi_img.show()
#blurred_jessi_img.save("Jessi_und_Molly_r80.jpg")
exit()
