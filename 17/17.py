with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("Register A:"):
            regA = int(line.split("Register A: ")[1])
        elif line.startswith("Register B:"):
            regB = int(line.split("Register B: ")[1])
        elif line.startswith("Register C:"):
            regC = int(line.split("Register C: ")[1])
        elif line.startswith("Program:"):
            program = [int(i) for i in line.split("Program: ")[1].split(",")]

inst_pointer = 0
output = []

def get_combo_operand_value(operand):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return regA
    elif operand == 5:
        return regB
    elif operand == 6:
        return regC

while inst_pointer < len(program):
    inst = program[inst_pointer]
    jmp = False
    if inst == 0:
        regA = int(regA / 2 ** get_combo_operand_value(program[inst_pointer + 1]))
    elif inst == 1:
        regB = regB ^ program[inst_pointer + 1]
    elif inst == 2:
        regB = get_combo_operand_value(program[inst_pointer + 1]) % 8
    elif inst == 3:
        if regA != 0:
            inst_pointer = program[inst_pointer + 1]
            jmp = True
    elif inst == 4:
        regB = regB ^ regC
    elif inst == 5:
        output.append(get_combo_operand_value(program[inst_pointer + 1]) % 8)
    elif inst == 6:
        regB = int(regA / 2 ** get_combo_operand_value(program[inst_pointer + 1]))
    elif inst == 7:
        regC = int(regA / 2 ** get_combo_operand_value(program[inst_pointer + 1]))

    if not jmp:
        inst_pointer += 2

print(",".join([str(i) for i in output]))