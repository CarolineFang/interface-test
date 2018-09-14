from sys import argv

script, file_path = argv

def read_file(file_name):
  file_obj = open(file_name)
  print(file_obj.read())
  file_obj.close()

print(f"读取文件: {file_path}")
read_file(file_path)