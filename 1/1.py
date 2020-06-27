import math

fuel_required = 0


def calculate_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    global fuel_required
    if fuel > 0:
        fuel_required += fuel
        calculate_fuel(fuel)


with open("1/input_1.txt") as file:
    mass_list = file.readlines()
    for item in mass_list:
        calculate_fuel(int(item))

print(fuel_required)
