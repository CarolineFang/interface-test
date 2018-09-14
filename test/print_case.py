# *args跟之前argv差不多
def print_case(*args):
  case_number, case_name = args
  print(f"用例编号: {case_number}")
  print(f"用例名称: {case_name}")

# 2个参数
def print_case_again(case_number, case_name):
  print(f"用例编号: {case_number}")
  print(f"用例名称: {case_name}")

# 1个参数
def print_delimiter(delimiter):
  print(delimiter * 20)

# 没有参数
def print_end():
  print('打印结束')

print_case('001', '验证GET请求的返回状态码')
print_delimiter('*')
print_case_again('002', '验证GET请求的返回值')
print_delimiter('*')
print_end()