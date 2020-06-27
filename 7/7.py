import sys


def run_instructions(instructions, inputs):
    index = 0
    current_input = 0
    try:
        while index < len(instructions):
            opcode = str(instructions[index]).zfill(5)
            instruction = int(opcode[3:5])
            first_mode = int(opcode[2])
            second_mode = int(opcode[1])
            third_mode = int(opcode[0])
            if instruction == 1:
                input_1_index = instructions[index + 1]
                input_2_index = instructions[index + 2]
                store_index = instructions[index + 3]
                if first_mode == 0:
                    input_1 = instructions[input_1_index]
                else:
                    input_1 = input_1_index
                if second_mode == 0:
                    input_2 = instructions[input_2_index]
                else:
                    input_2 = input_2_index
                instructions[store_index] = input_1 + input_2
                index += 4
            elif instruction == 2:
                input_1_index = instructions[index + 1]
                input_2_index = instructions[index + 2]
                store_index = instructions[index + 3]
                if first_mode == 0:
                    input_1 = instructions[input_1_index]
                else:
                    input_1 = input_1_index
                if second_mode == 0:
                    input_2 = instructions[input_2_index]
                else:
                    input_2 = input_2_index

                instructions[store_index] = input_1 * input_2
                index += 4
            elif instruction == 3:
                to_save = inputs[current_input]
                current_input += 1
                save_location = int(instructions[index + 1])
                instructions[save_location] = to_save
                index += 2
            elif instruction == 4:
                output_index = instructions[index + 1]
                if first_mode == 0:
                    to_output = instructions[output_index]
                else:
                    to_output = output_index
                return to_output
            elif instruction == 5:
                if_check = instructions[index + 1]
                if first_mode == 0:
                    if_check = instructions[if_check]
                pointer = instructions[index + 2]
                if if_check is not 0:
                    if second_mode is 0:
                        pointer = instructions[pointer]
                    index = pointer
                else:
                    index += 3
            elif instruction == 6:
                if_check = instructions[index + 1]
                if first_mode == 0:
                    if_check = instructions[if_check]
                pointer = instructions[index + 2]
                if if_check is 0:
                    if second_mode is 0:
                        pointer = instructions[pointer]
                    index = pointer
                else:
                    index += 3

            elif instruction == 7:
                input_1 = instructions[index + 1]
                input_2 = instructions[index + 2]
                input_3 = instructions[index + 3]
                if first_mode == 0:
                    input_1 = instructions[input_1]

                if second_mode == 0:
                    input_2 = instructions[input_2]

                if input_1 < input_2:
                    instructions[input_3] = 1
                else:
                    instructions[input_3] = 0

                index += 4
            elif instruction == 8:
                input_1 = instructions[index + 1]
                input_2 = instructions[index + 2]
                input_3 = instructions[index + 3]
                if first_mode == 0:
                    input_1 = instructions[input_1]

                if second_mode == 0:
                    input_2 = instructions[input_2]

                if input_1 == input_2:
                    instructions[input_3] = 1
                else:
                    instructions[input_3] = 0

                index += 4
            elif instruction == 99:
                break
            else:

                sys.exit(1)
    except IndexError:
        pass


with open("input_intcode.txt") as file:
    data = file.readline()
    original_ins = [int(item) for item in data.split(",")]

best_result = 0
for a in range(0, 5):
    a_ins = list.copy(original_ins)
    a_result = run_instructions(a_ins, [a, 0])
    for b in range(0, 5):
        b_ins = list.copy(original_ins)
        b_result = run_instructions(b_ins, [b, a_result])
        for c in range(0, 5):
            c_ins = list.copy(original_ins)
            c_result = run_instructions(c_ins, [c, b_result])
            for d in range(0, 5):
                d_ins = list.copy(original_ins)
                d_result = run_instructions(d_ins, [d, c_result])
                for e in range(0, 5):
                    e_ins = list.copy(original_ins)
                    e_result = run_instructions(e_ins, [e, d_result])
                    if len({a, b, c, d, e}) == 5:
                        best_result = max(best_result, e_result)

print(best_result)
