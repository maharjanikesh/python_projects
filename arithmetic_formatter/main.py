import re

def arithmetic_arranger(problems, display = True):
    if len(problems) > 5:
        print('Error: Too many problems.')
    
    # Initializing list for each line
    first_operands = []
    second_operands = []
    lines = []
    results = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()
        
        # if the operator is not '+' or '-'
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # if the operands are not in digits
        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # if the lengths of operands are greater than 4
        if len(operand1) > 4 and len(operand2):
            return "Error: Numbers cannot be more than four digits."

        # Determining the max length for formatting
        max_length = max(len(operand1), len(operand2)) + 2

        first_operands.append(operand1.rjust(max_length))
        second_operands.append(operator + operand2.rjust(max_length-1))
        lines.append('-' * max_length)

        # Calculate the result if display is True
        if display:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            elif operator == '-':
                result = str(int(operand1) - int(operand2))
            results.append(result.rjust(max_length))

    # Join the lines into a single string with each problem separated by four spaces
    arranged_problems = '    '.join(first_operands) + '\n' + '    '.join(second_operands) + '\n' + '    '.join(lines)
    if display:
        arranged_problems += '\n' + "    ".join(results)

    return arranged_problems



print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "123 + 49", "45 + 43"],display=True)}')