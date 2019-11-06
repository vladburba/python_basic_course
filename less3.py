# def ext_func(var_1):
#     print(var_1)
#     def int_func(var_2):
#         print(var_1)
#         print(var_2)
#         return var_1 + var_2
#     return int_func
#
# f_obj = ext_func(200) # f_obj - функция
# print(type(f_obj))
# print(f_obj(300))
# def my_func(*args):
#     return args
#
# print(my_func(10, 20, "text"))

# my_func = lambda p_1, p_2: p_1 + p_2
#
# print(my_func(2, 5))
# print(my_func("abra", "kadabra"))

# print((lambda p_1, p_2: p_1 + p_2)(2, 5))
# print((lambda p_1, p_2: p_1 + p_2)("abra", "kadabra"))
#
# new_func = lambda *args: args
# print(new_func(10, 20, 30, 40))
# for i in range(1, 100000):
#     print(i, chr(i), end=' ')
#     if i % 100 == 0:
#         print()
# print(list(range(7))) # целые числа в диапазоне [0, 7)
# print(list(range(2, 8))) # целые числа в диапазоне [2, 8)
# print(list(range(1, 9, 2))) # целые числа в диапазоне [1, 9) с шагом 2
# print(list(range(1, -7, -2))) # целые числа в диапазоне [1, -7) с шагом -2
# print(list(range(0))) # целые числа в диапазоне (0, 0)
# print(list(range(1, 0))) # целые числа в диапазоне (1, 0)


# for el in range(4, 20, 4):
#     res = el / 2
#     print(f"Результат деления {el} на 2: {int(res)}")


def ext_func():
    my_var = 0
    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var
    return int_func

func_obj = ext_func()
print(func_obj)
print(func_obj())
print(func_obj())
print(func_obj())