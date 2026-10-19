assert atteignables({'R1': ['R2', 'R3'], 'R2': ['R4'], 'R3': ['R4'], 'R4': [], 'R5': ['R1']}, 'R1') == ['R1', 'R2', 'R3', 'R4']
assert atteignables({'R1': ['R2', 'R3'], 'R2': ['R4'], 'R3': ['R4'], 'R4': [], 'R5': ['R1']}, 'R5') == ['R1', 'R2', 'R3', 'R4', 'R5']
assert atteignables({'A': []}, 'A') == ['A']
assert atteignables({'A': ['B'], 'B': ['A']}, 'A') == ['A', 'B']
