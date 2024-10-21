def calculate_structure_sum(data_structure):
    s = 0
    if isinstance(data_structure, dict):
        for i, j in data_structure.items():
            s += calculate_structure_sum(i)
            s += calculate_structure_sum(j)
    elif isinstance(data_structure, str):
        s += len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            s += calculate_structure_sum(item)
    elif isinstance(data_structure, (int, float)):
        s += data_structure
    return s

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
