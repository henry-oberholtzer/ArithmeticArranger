import re

def arithmetic_arranger(problems, show_answers=False):
  if 5 < len(problems):
    return "Error: Too many problems."
  top_operand = ''
  bottom_operand = ''
  dashes = ''
  answers = ''
  spaces = '    '
  for i, problem in enumerate(problems):
    parts = re.split(' ', problem)
    if re.search(r"[x/]", problem):
      return "Error: Operator must be '+' or '-'."
    if re.search("[0-9]{5,}", problem):
      return "Error: Numbers cannot be more than four digits."
    if re.search("[a-zA-Z]", problem):
      return "Error: Numbers must only contain digits."          
    # calculate the width of the problem
    width = 0
    if len(parts[0]) > len(parts[2]):
      width = len(parts[0]) + 2
    else:
      width = len(parts[2]) + 2
    # create top operator string
    top_operand += (width - len(parts[0])) * ' ' + parts[0]
    # create bottom operator string
    bottom_operand += parts[1] + ((width - len(parts[2])) - 1) * ' ' + parts[2]
    # create dashes
    dashes += '-' * width
    # calculate answer
    answer = 0
    if parts[1] == '+':
      answer = int(parts[0]) + int(parts[2])
    else:
      answer = int(parts[0]) - int(parts[2])
    answers += (width - len(str(answer))) * ' ' + str(answer)
    #add spacing
    if problems[-1] != problem:
      top_operand += spaces
      bottom_operand += spaces
      dashes += spaces
      answers += spaces

  formatted = f'{top_operand}\n{bottom_operand}\n{dashes}'
  if show_answers:
    return formatted + f'\n{answers}'
  return formatted
