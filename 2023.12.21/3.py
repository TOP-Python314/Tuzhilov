def math_function_resolver(func_obj:'function', *args: float, res_to_str = False) ->list:
    results = []
    for elem in args:
        if func_obj(elem):
            results.append(round(func_obj(elem)))
    return results
    
# >>> math_function_resolver(lambda x: 0.5*x + 2, *range(1, 10))
# [2, 3, 4, 4, 4, 5, 6, 6, 6]
# >>> math_function_resolver(lambda x: -0.5*x + 2, *range(1, 10))
# [2, 1, 0, 0, -1, -2, -2, -2]
# >>> math_function_resolver(lambda x: 2.72**x, *range(1, 10), res_to_str=True)
# [3, 7, 20, 55, 149, 405, 1101, 2996, 8149]

# >>> math_function_resolver(lambda x: 3.5*x + 10, *range(3, 15))
# [20, 24, 28, 31, 34, 38, 42, 45, 48, 52, 56, 59]
