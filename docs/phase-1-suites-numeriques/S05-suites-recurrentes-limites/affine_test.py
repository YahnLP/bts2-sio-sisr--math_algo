assert point_fixe(0.5, 10) == 20
assert abs(point_fixe(0.8, 30) - 150) < 1e-9
assert abs(terme_affine(0.5, 10, 0, 10) - 19.98046875) < 1e-9
assert abs(terme_affine(0.8, 30, 50, 6) - 123.7856) < 1e-9
assert terme_affine(0.5, 10, 0, 0) == 0
