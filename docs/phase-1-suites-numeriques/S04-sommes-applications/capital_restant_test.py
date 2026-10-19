assert capital_restant(12000, 0.5, 24, 0) == 12000.0
assert capital_restant(12000, 0.5, 24, 1) == 11528.15
assert capital_restant(12000, 0.5, 24, 3) == 10577.37
assert abs(capital_restant(12000, 0.5, 24, 24)) < 0.01
assert capital_restant(1200, 0, 12, 6) == 600.0
