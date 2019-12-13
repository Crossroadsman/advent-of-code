

class Instruction:
    pass


class BinaryInstruction(Instruction):

    def operation(self) -> int:
        """Concrete classes must implement this method"""
        pass

    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right

        self.operand_count = 2

        self.result = self.operation()

    def __repr__(self):
        return f'{self.left} <operation> {self.right} = {self.result}'

    def __str__(self):
        return self.result


class Add(BinaryInstruction):

    def operation(self) -> int:
        return self.left + self.right

    def __repr__(self):
        return f'{self.left} + {self.right} = {self.result}'
        

class Multiply(BinaryInstruction):

    def operation(self) -> int:
        return self.left * self.right

    def __repr__(self):
        return f'{self.left} * {self.right} = {self.result}'


def compute(program: [int], entry_point=0) -> int:

    halted = False
    instruction_pointer_address = entry_point

    live_program = program.copy()

    while not halted:
        opcode = live_program[instruction_pointer_address]

        if opcode == 99:
            break
        
        elif opcode == 1:
            operation_type = Add

        elif opcode == 2:
            operation_type = Multiply

        else:
            raise ValueError(f'Invalid opcode: {opcode}')

        if instruction_pointer_address  + 3 >= len(live_program):
            raise ValueError(f'increasing program length is not supported')

        a_address = live_program[instruction_pointer_address + 1]
        b_address = live_program[instruction_pointer_address + 2]
        x_address = live_program[instruction_pointer_address + 3]
        a = live_program[a_address]
        b = live_program[b_address]

        if x_address >= len(live_program):
            raise ValueError(f'increasing program length is not supported')

        operation = operation_type(a, b)

        live_program[x_address] = operation.result

        instruction_pointer_address += (operation.operand_count + 2)

    return live_program
           

