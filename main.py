import re

def arithmetic_arranger(problems, show_answers=False):
  if 5 < len(problems):
    return "Error: Too many problems."
  top_operand = ''
  bottom_operand = ''
  dashes = ''
  answers = ''
  for problem in problems:
    parts = re.split(problem, ' ')
    if re.search("[x/]", problem):
      return "Error: Operator must be '+' or '-'"
    if re.search("[0-9]{5,}", problem):
      return "Error: Numbers cannot be more than four digits."
    if re.search("[a-zA-Z]", problem):
      return "Error: Numbers must only contain digits."          
    # create top operator string
    # create bottom operator string
    # create dashes
    # calculate answer
  print = f'{top_operand}\n{bottom_operand}\n{dashes}'
  if show_answers:
    return print + f'\n{answers}'
  return print

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'\n{arithmetic_arranger(["24 + 5f15", "3801 / 2", "45 + 43", "123 + 49"])}')
