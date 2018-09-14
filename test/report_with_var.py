# 打印出本次测试的测试结果
# A: 27/30 B: 40/40 C: 30/30
module_count = 3

case_count_of_module_a = 30.0
success_case_count_of_module_a = 27

case_count_of_module_b = 40.0
success_case_count_of_module_b = 40

case_count_of_module_c = 30.0
success_case_count_of_module_c = 30

print('本次测试覆盖了',module_count ,'个模块')
print('测试用例总数为: ', case_count_of_module_a + case_count_of_module_b + case_count_of_module_c)
print('执行的测试用例总数为: ', case_count_of_module_a + case_count_of_module_b + case_count_of_module_c)
print('用例最多的模块是B模块，B模块比A模块多出的用例数为', case_count_of_module_b - case_count_of_module_a)
print('A模块执行成功', success_case_count_of_module_a, '个用例，执行失败的用例数为', case_count_of_module_a - success_case_count_of_module_a)
print('A模块用例通过率为百分之', success_case_count_of_module_a / case_count_of_module_a * 100)
print('B模块的用例全部执行通过， 通过率为百分之', (success_case_count_of_module_b / case_count_of_module_b) * 100)
print('C模块的用例全部执行通过， 通过率为百分之', (success_case_count_of_module_b / case_count_of_module_b) * 100)
print('B模块的用例比C模块多吗?', case_count_of_module_b > case_count_of_module_c)
print('A模块的用例比C模块多吗?', case_count_of_module_a > case_count_of_module_c)
print('B模块的用例比C模块少吗?', case_count_of_module_b < case_count_of_module_c)

# 结束打印
print('回归不通过')