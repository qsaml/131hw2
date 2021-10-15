'''
Parses a user-given string into a mathematical expression.

Params:
  None
Returns:
  Nothing
'''


def parse_input():
    eqn = input('Enter equation: ')
    nums = []
    op = ''
    for t in eqn.split():
        try:
            nums.append(float(t))
        except ValueError:
            pass
    for i in range(0, len(eqn)):
        if not (eqn[i].isalnum() or eqn[i].isspace() or eqn[i] == '.'):
            op += eqn[i]
    if nums[1] == 0 and (op == '/' or op == '//'):
        print('False')
        quit()
    print(calculator(nums[0], nums[1], op))
    return


'''
Calculates a mathematical expression and returns its result.

Params:
  number1: Any number.
  number2: Any number.
  operator: The operation to use on the above numbers.
Operators:
  '+': Adds number1 and number2.
  '-': Subtracts number1 and number2.
  '*': Multiplies number1 and number2.
  '/': Divides number1 and number2.
  '**': Raises number1 to the number2 power.
  '//': Divides number1 and number2, then takes the floor of the quotient.
Returns:
  result: The result of the calculation.
'''


def calculator(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if not number2 == 0:
            return number1 / number2
    elif operator == '**':
        return number1 ** number2
    elif operator == '//':
        if not number2 == 0:
            return number1 // number2
