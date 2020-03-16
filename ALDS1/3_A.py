def calc_formula(formula_list: list):
    operator = formula_list.pop()
    # back
    if formula_list[-1] in ['+', '-', '*']:
        back = calc_formula(formula_list)
    else:
        back = int(formula_list.pop())

    #front
    if formula_list[-1] in ['+', '-', '*']:
        front = calc_formula(formula_list)
    else:
        front = int(formula_list.pop())
    
    # calc
    if operator == '+':
        return front + back

    if operator == '-':
        return front - back

    if operator == '*':
        return front * back

formula = input().split(' ')

res = calc_formula(formula)
print(res)