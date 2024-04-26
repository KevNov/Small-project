def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"
print(calculate(make_float=True, operation='multiply', first=4.5, second=7.5))
