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
    layers.append(matrix)
    previous_cut = current_cut
    current_cut += width * height

least_zeros = 999999999999
least_zeros_index = 0
for index, layer in enumerate(layers):
    unique, counts = np.unique(layer, return_counts=True)
    items = dict(zip(unique, counts))
    if items[0] < least_zeros:
        least_zeros_index = index
        least_zeros = items[0]

unique, counts = np.unique(layers[least_zeros_index], return_counts=True)
items = dict(zip(unique, counts))
print(items[1] * items[2])