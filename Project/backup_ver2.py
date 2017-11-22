import os
import time

# 按年月日区分备份文件
source = ['"D:\\test\\my_python_back_file.txt"']

target_dir = 'D:\\jarvix\\python\\backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Successful create dir to',target_dir)

# 年月日目录
today  =    target_dir + os.sep + \
            time.strftime('%Y%m%d')

# 判断目录是否存在
if not os.path.exists(today):
    os.mkdir(today)

target = today + os.sep + time.strftime('%H%M%S') + '.zip'

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print("Zip command is:")
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
print(os.sep)
