'''
#22.2
def partial_sums(*a):
    res = [0]
    for i in range(len(a)):
        res.append(res[i] + a[i])
    return res

print(partial_sums(1, 0.5, 0.25, 0.125))
'''

'''
#22.4
def solve(*coefficients):
    if len(coefficients) == 3:
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        return roots_of_quadratic_equation(a, b, c)
    elif len(coefficients) == 2:
        b, c = coefficients[0], coefficients[1]
        return -c / b
    elif len(coefficients) == 1:
        return 0
    else:
        return None
'''
