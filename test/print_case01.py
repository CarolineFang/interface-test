
def print_case_count(success, failed):
    total_count = success + failed
    print(f"一共{total_count}个用例, 成功{success}个, 失败{failed}个")

def print_end():
  print('打印结束')

print('第一次运行')
print_case_count(95, 5)

print('第二次运行')
success = 101
failed = 0
print_case_count(success, failed)

print('第三次运行')
total = 100
failed = 7
print_case_count(total - failed, failed)

print_end()
