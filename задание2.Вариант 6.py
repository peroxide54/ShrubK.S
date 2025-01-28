import math
x = 16.55 * 10**-3
y = -2.75
z = 0.15
cube_root_x = x ** (1/3)
x_pow_y_plus_2 = x ** (y + 2)
arcsin_z_squared = (math.asin(z)) ** 2
abs_x_minus_y = abs(x - y)
s = math.sqrt(10 * (cube_root_x + x_pow_y_plus_2)) * (arcsin_z_squared - abs_x_minus_y)
print(f"s = {s}")