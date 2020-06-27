import sys

with open("input_intcode.txt") as file:
    data = file.readline()
    instructions = [int(item) for item in data.split(",")]
for i in range(0, 100):
    for j in range(0, 100):
        index = 0
        if instructions[0] == 19690720:
            print(100*instructions[1]+instructions[2])
            sys.exit()
        with open("input_intcode.txt") as file:
            data = file.readline()
            instructions = [int(item) for item in data.split(",")]
        instructions[1] = i
        instructions[2] = j
        try:
            while index < len(instructions):
                instruction = instructions[index]
                if instruction == 1:
                    input_1_index = instructions[index + 1]
                    input_2_index = instructions[index + 2]
                    store_index = instructions[index + 3]
                    input_1 = instructions[input_1_index]
                    input_2 = instructions[input_2_index]
                    instructions[store_index] = input_1 + input_2
                elif instruction == 2:
                    input_1_index = instructions[index + 1]
                    input_2_index = instructions[index + 2]
                    store_index = instructions[index + 3]
                    input_1 = instructions[input_1_index]
                    input_2 = instructions[input_2_index]
                    instructions[store_index] = input_1 * input_2

                elif instruction == 99:
                    break
                index += 4
        except IndexError:
            pass
