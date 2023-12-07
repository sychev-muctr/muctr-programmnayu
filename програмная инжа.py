z = lambda: float(input("Введите значение z: "))
func_x = lambda z: z ** 2 + z ** 3
func_y = lambda z: z + z * 2
func_f = lambda x, y, z: print(x(z) + y(z))

number_z = z()

func_f(func_x, func_y, number_z)