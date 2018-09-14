from sys import argv
#打开文件的时候，’w’表示’write mode’，也就是写入模式的意思。
# 另外可以传入’r’，表示读取模式，以及’a’，表示’append mode’，也就是追加内容模式
script, case_number, case_name, assertion = argv

file_name = 'case002.txt'

print(f"用例编号: {case_number}")
print(f"用例名称: {case_name}")
print(f"断言: {assertion}")

target = open(file_name, 'w')

print("Truncating the file. Goodbye!")

print(f"write file: {file_name}")

target.write(f"用例编号: {case_number}")
target.write("\n")
target.write(f"用例名称: {case_name}")
target.write("\n")
target.write(f"断言: {assertion}")
target.write("\n")
target.close()