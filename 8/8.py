import numpy as np
from PIL import Image

width = 25
height = 6

layers = []
with open("image_1.txt") as file:
    data = list(file.read())

previous_cut = 0
current_cut = width * height
index = 0
while current_cut <= len(data):
    working_data = data[previous_cut:current_cut]
    matrix = np.array(working_data, dtype=int)
    layers.append(matrix.reshape(height, width))
    previous_cut = current_cut
    current_cut += width * height

im = Image.new("1", (height, width), color=0)
current_level = 0
pixel = []
amount_of_whites = 0
for i in range(width):
    for j in range(height):
        value = layers[current_level][j,i]
        while value == 2:
            current_level += 1
            value = layers[current_level][j,i]
        pixel.append(value)
        if value == 1:
            amount_of_whites += 1
        current_level = 0

print(pixel)
print(amount_of_whites)
im.putdata(pixel)
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out = out.rotate(270, expand=True)
out.save("test.png")
