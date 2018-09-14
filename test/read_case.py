from sys import argv

script, file_path = argv

print(f"读取文件: {case001}")
print()
file_obj = open(file_path)
print(file_obj.read())
file_obj.close()