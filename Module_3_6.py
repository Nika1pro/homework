def sum_of_all(data):
    sum = 0
    if isinstance(data, int):
        sum += data
    elif isinstance(data, str):
        sum += len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            sum += sum_of_all(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            sum += sum_of_all(key)
            sum += sum_of_all(value)

    return sum

data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]

result = sum_of_all(data_structure)
print(result)



